"""01_Start_GUI_v4
Create instructions GUI, explaining game rules
Save number of questions and number of assistance after pressing 'Start'
Print error if user does not choose either questions or assistance
"""

from tkinter import *

# assist & quest list to store assist & quest chosen by user
# quest_assist list to store final value chosen by user
assist_list = [0]
quest_list = [0]
quest_assist = [0, 0]

# Instruction before letting user choose questions and assistance
class Instruction:
    def __init__(self):
        # Formatting variables
        self.background_colour = 'light blue'

        # main frame
        self.main_frame = Frame(width=500, height=300,
                                bg=self.background_colour)
        self.main_frame.grid(row=0, column=0)

        # main title
        Label(self.main_frame, text='WELCOME TO TE REO MAORI QUIZ',
              bg=self.background_colour, font='Arial 20 bold').grid(padx=20,
                                                                   pady=10)

        # brief instruction
        Label(self.main_frame, bg=self.background_colour,
              text='Before starting, you can choose either 15 or 20 questions.'
                   '\nThere is a 50/50 assistance and you can choose to have 1'
                   ' or 2 or 3 of them', font='Arial 12').grid(padx=20,pady=10)

        # start button to get to questions&assist frame
        self.start_button = Button(self.main_frame, text='Start', width=10,
               command=lambda: self.another_class())
        self.start_button.grid(padx=20, pady=10)

    # delete Instruction UI and get to Start UI
    def another_class(self):
        self.main_frame.grid_forget()
        self.main_frame.destroy()
        Start()

class Start:
    def __init__(self):

        #Formatting variables
        self.background_colour = 'light blue'

        # main frame
        self.main_frame = Frame(width=800, height=600,
                                bg=self.background_colour, pady=10)
        self.main_frame.grid()

        # main title
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
        question_number_1 = Button(self.sub_frame, text='15',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(15, False))
        question_number_2 = Button(self.sub_frame, text='20',
                                   font='Arial 16 bold', command=lambda:
            self.print_txt(20, False))

        question_number_1.grid(row=1, column=0, pady=10)
        question_number_2.grid(row=2, column=0, pady=10)

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

        # add confirm function to button
        # after user press 'Start', store the last value of questions & assist
        Button(self.main_frame, text='Start', font='Arial 18 bold',
               command=lambda: self.confirm(quest_list[-1],
                                            assist_list[-1])).grid(row=3)

        self.quest_assist_txt = ''

    # function to print out number of questions and assist user choose
    # fixed error to print both questions and assistance (can only print
    # either before)
    def print_txt(self, quest, assist):
        if not quest: # if quest is false, the value is assist
            assist_list.append(assist) # append value to assist list

        elif not assist: # if assist is false, the value is quest
            quest_list.append(quest) # append value to quest list

        # use the last value chosen by user
        assist_txt = f'{assist_list[-1]} assistance'
        quest_txt = f'{quest_list[-1]} questions'

        # display number of questions and assist
        self.quest_assist_txt = Label(self.main_frame, font='Arial 14',
                                     bg=self.background_colour,
              text=f'You have chosen {quest_txt} and {assist_txt}')
        self.quest_assist_txt.grid(row=2)

    # confirm function to 
    def confirm(self, quest, assist):
        # print error if user only choose either questions or assist
        if quest == 0 or assist == 0:
            self.quest_assist_txt.configure(text='Please choose both '
                                                 'questions and assistance',
                                            fg='Red', font='bold')
        else: # store the last value to quest_assist list
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
