"""01_Start_GUI_v3
Fix text display error - used to be printing either number questions or
number assistance only
Print both number questions and number assistance
"""

from tkinter import *

# assist & quest list to store assist & quest chosen by user
assist_list = [0]
quest_list = [0]

class Start:
    def __init__(self):

        #Formatting variables
        self.background_colour = 'light blue'

        # main frame
        self.main_frame = Frame(width=800, height=600, bg=self.background_colour,
                           pady=10)
        self.main_frame.grid()

        # main label
        Label(self.main_frame, text='Te Reo Maori Quiz', font='Arial 16 bold',
              bg=self.background_colour, padx=10, pady=10).grid(row=0)

        # sub frame for questions and assistance labels & buttons
        self.sub_frame = Frame(self.main_frame, bg=self.background_colour)
        self.sub_frame.grid(row=1)

        # question & assistance labels
        Label(self.sub_frame, bg=self.background_colour,
              text='Number of questions', font='Arial 14 bold', padx=10,
              pady=10).grid(row=0, column=0)
        Label(self.sub_frame, bg=self.background_colour,
              text='Number of assistance', font='Arial 14 bold', padx=10,
              pady=10).grid(row=0, column=1)

        # question buttons
        # add function to store number of questions using lambda
        question_number_15 = Button(self.sub_frame, text='15',
                                    font='Arial 16 bold',
                                    command=lambda: self.print_txt(15, False))
        question_number_20 = Button(self.sub_frame, text='20',
                                    font='Arial 16 bold',
                                    command=lambda: self.print_txt(20, False))

        question_number_15.grid(row=1, column=0, pady=10)
        question_number_20.grid(row=2, column=0, pady=10)

        # assistance buttons
        # add function to store number of assistance using lambda
        assist_1 = Button(self.sub_frame, text='1', font='Arial 16 bold',
                          command=lambda: self.print_txt(False, 1))
        assist_2 = Button(self.sub_frame, text='2', font='Arial 16 bold',
                          command=lambda: self.print_txt(False, 2))
        assist_3 = Button(self.sub_frame, text='3', font='Arial 16 bold',
                          command=lambda: self.print_txt(False, 3))

        assist_1.grid(row=1, column=1, pady=10)
        assist_2.grid(row=2, column=1, pady=10)
        assist_3.grid(row=3, column=1, pady=10)

        Button(self.main_frame, text='Start', font='Arial 18 bold').grid(row=3)

    # function to print out number of questions and assist user choose
    # fixed error to print both questions and assistance (can only print
    # either before)
    def print_txt(self, quest, assist):

        if not quest: # if quest is false, the value is assist
            assist_list.append(assist) # append to assist list
        elif not assist: # if assist is false, the value is quest
            quest_list.append(quest) # append to quest list

        # use the last value chosen by user
        assist_txt = f'{assist_list[-1]} assistance'
        quest_txt = f'{quest_list[-1]} questions'

        # display number of questions and assist
        Label(self.main_frame, bg=self.background_colour,
              text=f'You are selecting {quest_txt} and '
                   f'{assist_txt}').grid(row=2)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori")
    program = Start()
    root.mainloop()
