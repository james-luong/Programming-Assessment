"""01_Start_GUI_v2
Add function to print out how many questions and assistance user has chosen
in row 2
Change 'Start' button to row 3"""

from tkinter import *

class Start:
    def __init__(self):

        #Formatting variables
        self.background_colour = 'light blue'

        self.main_frame = Frame(width=800, height=600,
                                bg=self.background_colour, pady=10)
        self.main_frame.grid()

        Label(self.main_frame, text='Te Reo Maori Quiz', font='Arial 16 bold',
              bg=self.background_colour, padx=10, pady=10).grid(row=0)

        self.sub_frame = Frame(self.main_frame, bg=self.background_colour)
        self.sub_frame.grid(row=1)

        Label(self.sub_frame, bg=self.background_colour,
              text='Number of questions', font='Arial 14 bold', padx=10,
              pady=10).grid(row=0, column=0)
        Label(self.sub_frame, bg=self.background_colour,
              text='Number of lifelines', font='Arial 14 bold', padx=10,
              pady=10).grid(row=0, column=1)

        question_number_15 = Button(self.sub_frame, text='15',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(15, False))
        question_number_20 = Button(self.sub_frame, text='20',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(20, False))

        question_number_15.grid(row=1, column=0, pady=10)
        question_number_20.grid(row=2, column=0, pady=10)

        lifeline_1 = Button(self.sub_frame, text='1', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 1))
        lifeline_2 = Button(self.sub_frame, text='2', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 2))
        lifeline_3 = Button(self.sub_frame, text='3', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 3))

        lifeline_1.grid(row=1, column=1, pady=10)
        lifeline_2.grid(row=2, column=1, pady=10)
        lifeline_3.grid(row=3, column=1, pady=10)

        Button(self.main_frame, text='Start', font='Arial 18 bold').grid(row=3)

    def print_txt(self, quest, assist):
        assist_txt = ''
        quest_txt = ''

        if not quest:
            assist_txt = f'{assist} assistance'

        elif not assist:
            quest_txt = f'{quest} questions'

        Label(self.main_frame, bg=self.background_colour,
              text=f'You are choosing {quest_txt} and {assist_txt}').grid(row=2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori")
    program = Start()
    root.mainloop()