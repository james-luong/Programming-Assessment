"""
02_Help_GUI_v3
Disable help button in Main window when instructions window has popped up
To prevent opening multiple instruction windows
"""

from tkinter import *

class Main:
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

        # disable help button once clicked
        partner.help_button.config(state=DISABLED)

        # set up child window (i.e. help box)
        self.help_box = Toplevel()

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up help heading (row 0)
        self.help_heading = Label(self.help_frame, text='Help/Instructions',
                                 font='arial 11 bold', bg=background)
        self.help_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text='', justify=LEFT,
                               width=50, bg=background, pady=10, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text='Dismiss', width=10,
                                  bg='orange', font='arial 10 bold',
                                  command=self.close_help)
        self.dismiss_btn.grid(row=2, pady=10)

    # close window function
    def close_help(self):
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Main()
    root.mainloop()
