"""
02_Help_GUI_v1
Create an initial window for help button - has no effects yet
"""

from tkinter import *

class Main:
    def __init__(self):
        #Formatting variables
        self.background_colour = 'light blue'

        # Help main screen GUI
        self.help_frame = Frame(width=300, height=300,
                                bg=self.background_colour)
        self.help_frame.grid()

        # Help heading (row 0)
        self.quiz_label = Label(self.help_frame, text='Te Reo Maori Quiz',
                                font='Arial 16 bold',
                                bg=self.background_colour, padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # help button
        self.help_button = Button(self.help_frame, text='Help',
                                  font='Arial 12 bold', padx=5, pady=5)
        self.help_button.grid(row=1, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Main()
    root.mainloop()
