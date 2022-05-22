"""01_Start_GUI_v4
Create instructions GUI, explaining game rules
Save number of questions and number of assistance after pressing 'Start'
Print error if user does not choose either questions or assistance
"""

from tkinter import *
from colour import Color

assist_list = [0]
quest_list = [0]
quest_assist = [0, 0]

class Instruction:
    def __init__(self):
        # Formatting variables
        self.background_colour = 'light blue'

        self.main_frame = Frame(width=500, height=300,
                                bg=self.background_colour)
        self.main_frame.grid(row=0, column=0)

        Label(self.main_frame, text='WELCOME TO TE REO MAORI QUIZ',
              bg=self.background_colour, font='Arial 20 bold').grid(padx=20,
                                                                   pady=10)

        Label(self.main_frame, bg=self.background_colour,
              text='Before starting, you can choose either 15 or 20 questions.'
                   '\nThere is a 50/50 assistance and you can choose to have 1'
                   ' or 2 or 3 of them', font='Arial 12').grid(padx=20,pady=10)

        self.start_button = Button(self.main_frame, text='Start', width=10,
               command=lambda: self.another_class())
        self.start_button.grid(padx=20, pady=10)

    def another_class(self):
        self.main_frame.grid_forget()
        self.main_frame.destroy()
        Start()

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

        question_number_1 = Button(self.sub_frame, text='15',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(15, False))
        question_number_2 = Button(self.sub_frame, text='20',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(20, False))

        question_number_1.grid(row=1, column=0, pady=10)
        question_number_2.grid(row=2, column=0, pady=10)

        lifeline_1 = Button(self.sub_frame, text='1', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 1))
        lifeline_2 = Button(self.sub_frame, text='2', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 2))
        lifeline_3 = Button(self.sub_frame, text='3', font='Arial 16 bold',
                            command=lambda: self.print_txt(False, 3))

        lifeline_1.grid(row=1, column=1, pady=10)
        lifeline_2.grid(row=2, column=1, pady=10)
        lifeline_3.grid(row=3, column=1, pady=10)

        Button(self.main_frame, text='Start', font='Arial 18 bold',
               command=lambda: self.confirm(quest_list[-1],
                                            assist_list[-1])).grid(row=3)

        self.quest_assist_txt = ''

    def print_txt(self, quest, assist):
        if not quest:
            assist_list.append(assist)

        elif not assist:
            quest_list.append(quest)

        assist_txt = f'{assist_list[-1]} assistance'
        quest_txt = f'{quest_list[-1]} questions'

        self.quest_assist_txt = Label(self.main_frame, font='Arial 14',
                                     bg=self.background_colour,
              text=f'You have chosen {quest_txt} and {assist_txt}')
        self.quest_assist_txt.grid(row=2)

    def confirm(self, quest, assist):
        if quest == 0 or assist == 0:
            self.quest_assist_txt.configure(text='Please choose both '
                                                 'questions and assistance',
                                            fg='Red', font='bold')
        else:
            quest_assist[0] = quest
            quest_assist[1] = assist
            print(quest_assist)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori")
    root.columnconfigure(0, weight=1)  # Set weight to row and
    root.rowconfigure(0, weight=1)  # column where the widget is
    program = Instruction()
    root.mainloop()
