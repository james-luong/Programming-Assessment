"""01_Start_GUI_v1
Create one main frame and one sub frame,
Use sub frame to organise text and buttons"""

from tkinter import *

class Start:
    def __init__(self):

        #Formatting variables
        background_colour = 'light blue'

        self.main_frame = Frame(width=800, height=600, bg=background_colour,
                           pady=10)
        self.main_frame.grid()

        Label(self.main_frame, text='Te Reo Maori Quiz', font='Arial 16 bold',
              bg=background_colour, padx=10, pady=10).grid(row=0)

        self.sub_frame = Frame(self.main_frame, bg=background_colour)
        self.sub_frame.grid(row=1)

        Label(self.sub_frame, bg=background_colour, text='Number of questions',
              font='Arial 14 bold', padx=10, pady=10).grid(row=0, column=0)
        Label(self.sub_frame, bg=background_colour, text='Number of lifelines',
              font='Arial 14 bold', padx=10, pady=10).grid(row=0, column=1)

        question_number_1 = Button(self.sub_frame, text='15',
                                   font='Arial 16 bold')
        question_number_2 = Button(self.sub_frame, text='20',
                                   font='Arial 16 bold')

        question_number_1.grid(row=1, column=0, pady=10)
        question_number_2.grid(row=2, column=0, pady=10)

        lifeline_1 = Button(self.sub_frame, text='1', font='Arial 16 bold')
        lifeline_2 = Button(self.sub_frame, text='2', font='Arial 16 bold')
        lifeline_3 = Button(self.sub_frame, text='3', font='Arial 16 bold')

        lifeline_1.grid(row=1, column=1, pady=10)
        lifeline_2.grid(row=2, column=1, pady=10)
        lifeline_3.grid(row=3, column=1, pady=10)

        Button(self.main_frame, text='Start', font='Arial 18 bold').grid(row=2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori")
    program = Start()
    root.mainloop()