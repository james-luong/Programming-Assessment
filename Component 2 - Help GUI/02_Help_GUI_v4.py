"""
02_Help_GUI_v4
Fix help button disabled permanently after being clicked once
Disable help button when instructions window is on and enable it when
instructions window is closed
"""

from tkinter import *
from functools import partial # to prevent unwanted windows

class Convertor:
    def __init__(self):
        # Formatting variables
        self.background_colour = 'light blue'

        # Help main screen GUI
        self.main_frame = Frame(width=300, height=300,
                                bg=self.background_colour)
        self.main_frame.grid()

        # Help heading (row 0)
        self.quiz_label = Label(self.main_frame, text='Te Reo Maori Quiz',
                                font='Arial 16 bold',
                                bg=self.background_colour, padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # help button
        self.help_button = Button(self.main_frame, text='Help',
                                  font='Arial 12 bold', padx=5, pady=5,
                                  command=self.help_activate)
        self.help_button.grid(row=1, pady=10)

    def help_activate(self):
        get_help = Help(self)
        get_help.help_text.configure(text='A question about Maori word will '
                                          'pop up, you then need to choose '
                                          'one of the answers below and then '
                                          'click confirm if you are certain '
                                          'about your answer. You can use '
                                          'assistance which can eliminate two '
                                          'wrong answers, but you can use '
                                          'them for a limited time so use '
                                          'them wisely.')


class Help:
    def __init__(self, partner):
        background = 'orange'

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (i.e. help box)
        self.help_box = Toplevel()

        # if users press cross of top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 1)
        self.help_heading = Label(self.help_frame, text='Export/Instructions',
                                  font='arial 10 bold', bg=background)
        self.help_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text='', justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text='Dismiss', width=10,
                                  bg='orange', font='arial 10 bold',
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
