"""
05_Main_quiz_v1
Combination of 01_Start_GUI_v4, 03_Assistance_v4, 04_Quest_Ans_v4
Disable all answer buttons and assist button after user click an answer button
to prevent user click correct answer again which can increase the score
"""

from tkinter import *
import random
from random import shuffle
import csv

# list to store all questions + answers
quest_ans_list = []
# dictionary to store questions + correct answers
quest_ans_dict = {}

# questions & answers from tepapa.govt.nz and testyourlanguage.com
with open('maori quiz.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # append items to quest_ans_list as
        # ['question', [ans1, ans2, ans3, ans4]] format
        # left last item as it is correct answer and add it in dictionary
        quest_ans_list.append([row[0].capitalize(), row[1:-1]])

        # add questions & correct answers to dict (*note: last items in each
        # list are correct answers by default)
        quest_ans_dict[row[0].capitalize()] = row[-1]

quest_num = 0

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
              text='Before you start, you can choose either 15 or 20 '
                   'questions. Assistance 50/50 help you eliminate 2 wrong '
                   'answers and you can choose to have 1, 2 or 3 of them',
              font='Arial 12', wrap=400).grid(row=1, padx=20, pady=10)

        # start button to get to questions&assist frame
        self.start_button = Button(self.main_frame, text='Continue', width=10,
               command=lambda: self.another_class())
        self.start_button.grid(padx=20, pady=10)

        # function to delete Instruction UI and get to Start UI
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

        assist_txt = f'{assist_list[-1]} assistance'
        quest_txt = f'{quest_list[-1]} questions'
        # display number of questions and assist
        self.quest_assist_txt = Label(self.main_frame, font='Arial 14 bold',
                                      bg=self.background_colour,
                                      text=f'You have chosen {quest_txt} and '
                                           f'{assist_txt}')
        self.quest_assist_txt.grid(row=2)

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
        self.quest_assist_txt.configure(text=f'You have chosen {quest_txt} and'
                                             f' {assist_txt}', fg='black')

    # confirm function to
    def confirm(self, quest, assist):
        # print error if user only choose either questions or assist
        if quest == 0 or assist == 0:
            self.quest_assist_txt.configure(text='Please choose both '
                                                 'questions and assistance',
                                            fg='Red', font='Arial 14 bold')
        else: # store the last value to quest_assist list
            quest_assist[0] = quest
            quest_assist[1] = assist
            self.main_frame.grid_forget()
            self.main_frame.destroy()
            Quiz()

class Quiz:
    def __init__(self):
        self.background = 'light green'

        self.num_assist = quest_assist[1]

        # quiz main screen GUI
        self.main_frame = Frame(width=500, height=300, bg=self.background)
        self.main_frame.grid()

        # main label
        Label(self.main_frame, text='Te Reo Maori Quiz', bg=self.background,
              font='Arial 14 bold').grid(row=0, pady=10)

        # sub frame 1
        self.sub_frame = Frame(self.main_frame, bg=self.background)
        self.sub_frame.grid(row=1)

        # quest label
        self.quest_label = Label(self.sub_frame, bg='#FF4444',
                                 justify=LEFT, text=quest_ans_list[0][0],
                                 font='Arial 16 bold', wrap=380)
        self.quest_label.grid(row=0)
        self.quest_label.config(width=28, height=3)

        # question number labels frame
        self.quest_no_frame = Frame(self.sub_frame, bg=self.background)
        self.quest_no_frame.grid(row=0, column=1)

        # question number label
        self.quest_no = Label(self.quest_no_frame,
                              text=f'Question: {quest_num + 1}/'
                                   f'{quest_assist[0]}')
        self.quest_no.grid(row=0, pady=5)

        # assist frame
        self.assist_frame = Frame(self.sub_frame, bg=self.background)
        self.assist_frame.grid(row=1, column=1)

        # next question button
        self.next_quest_button = Button(self.assist_frame, text='Next question',
                                        command=self.next_quest)
        self.next_quest_button.grid(row=0, padx=5, pady=5)

        # assist button
        self.assist_button = Button(self.assist_frame, text=f'Assistance (50/50):'
                                                         f' {self.num_assist}',
                                    command=self.assist)
        self.assist_button.grid(row=1, padx=5, pady=5)

        # answer frame
        self.answers_frame = Frame(self.sub_frame, bg=self.background)
        self.answers_frame.grid(row=1, pady=10)

        # answer buttons
        # using config to make fixed button size
        self.answer_1 = Button(self.answers_frame,
                               text=quest_ans_list[0][1][0],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][0]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_1.grid(row=0, column=0, padx=5, pady=5)
        self.answer_1.config(width=6)

        self.answer_2 = Button(self.answers_frame,
                               text=quest_ans_list[0][1][1],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][1]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_2.grid(row=0, column=1, padx=5, pady=5)
        self.answer_2.config(width=6)

        self.answer_3 = Button(self.answers_frame,
                               text=quest_ans_list[0][1][2],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][2]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)
        self.answer_3.config(width=6)

        self.answer_4 = Button(self.answers_frame,
                               text=quest_ans_list[0][1][3],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][3]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)
        self.answer_4.config(width=6)

    def assist(self):
        # decrease number of assist when user click assist button
        self.num_assist -= 1

        # update new number of assist left for user
        self.assist_button.configure(text=f'Assistance (50/50): '
                                          f'{self.num_assist}')

        # disable assist button for now
        self.assist_button.config(state=DISABLED)
        # list of answers can be removed (i.e. not correct answers)
        ans_to_del = []

        for answer in range(4):
            # append to ans_to_del list if answer is not correct
            if quest_ans_list[0][1][answer] != \
                    quest_ans_dict[quest_ans_list[0][0]]:
                ans_to_del.append(quest_ans_list[0][1][answer])

        # delete random wrong answers
        ans_to_del.remove(random.choice(ans_to_del))

        # disable answer that is not correct
        if self.answer_1['text'] in ans_to_del:
            self.answer_1.config(state=DISABLED)

        if self.answer_2['text'] in ans_to_del:
            self.answer_2.config(state=DISABLED)

        if self.answer_3['text'] in ans_to_del:
            self.answer_3.config(state=DISABLED)

        if self.answer_4['text'] in ans_to_del:
            self.answer_4.config(state=DISABLED)

    def next_quest(self):
        # make quest_num, quest_ans_list global
        global quest_num, quest_ans_list

        # increase number of questions whenever user click next question button
        quest_num += 1

        # enable assist button if there's still number of assist
        if self.num_assist > 0:
            self.assist_button.config(state=NORMAL)

        # when the number of questions reach the maximum (chosen question
        # number), disable all buttons
        if quest_num == quest_assist[0]:
            self.answer_1.config(state=DISABLED)
            self.answer_2.config(state=DISABLED)
            self.answer_3.config(state=DISABLED)
            self.answer_4.config(state=DISABLED)
            self.assist_button.config(state=DISABLED)
            self.next_quest_button.config(state=DISABLED)

        else:
            # delete the first question & answers list
            quest_ans_list.pop(0)

            # shuffle all questions so that they will not be shown in the
            # same order every time
            quest_ans_list = [i for i in quest_ans_list]
            shuffle(quest_ans_list)
            print(quest_ans_list)

            # also shuffle answers in a question so that they will not be in
            # the same position every time
            quest_ans_list[0][1] = [i for i in quest_ans_list[0][1]]
            shuffle(quest_ans_list[0][1])

            # display number of questions users are up to
            self.quest_no.config(text=f'Question: {quest_num + 1}/'
                                      f'{quest_assist[0]}')

            # change question and answers
            # change buttons background to white as correct answer has been
            # changed green before
            self.quest_label.config(text=quest_ans_list[0][0])
            self.answer_1.config(state=NORMAL, bg='white',
                                 text=quest_ans_list[0][1][0])
            self.answer_2.config(state=NORMAL, bg='white',
                                 text=quest_ans_list[0][1][1])
            self.answer_3.config(state=NORMAL, bg='white',
                                 text=quest_ans_list[0][1][2])
            self.answer_4.config(state=NORMAL, bg='white',
                                 text=quest_ans_list[0][1][3])

    def check_ans(self, click_btn):
        # disable answer and assist buttons when user click one answer
        # to prevent user clicking correct answers after getting a wrong answer
        self.answer_1.config(state=DISABLED)
        self.answer_2.config(state=DISABLED)
        self.answer_3.config(state=DISABLED)
        self.answer_4.config(state=DISABLED)
        self.assist_button.config(state=DISABLED)

        # turn correct answer buttons to green when user click one of the
        # answer buttons
        if self.answer_1['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_1.config(bg='#2BFF34')

        elif self.answer_2['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_2.config(bg='#2BFF34')

        elif self.answer_3['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_3.config(bg='#2BFF34')

        elif self.answer_4['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_4.config(bg='#2BFF34')

        # if answer user clicked is wrong, make background colour red
        if click_btn == self.answer_1['text']:
            if self.answer_1['text'] != quest_ans_dict[quest_ans_list[0][0]]:
                self.answer_1.config(bg='red')

        if click_btn == self.answer_2['text']:
            if self.answer_2['text'] != quest_ans_dict[quest_ans_list[0][0]]:
                self.answer_2.config(bg='red')

        if click_btn == self.answer_3['text']:
            if self.answer_3['text'] != quest_ans_dict[quest_ans_list[0][0]]:
                self.answer_3.config(bg='red')

        if click_btn == self.answer_4['text']:
            if self.answer_4['text'] != quest_ans_dict[quest_ans_list[0][0]]:
                self.answer_4.config(bg='red')


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Instruction()
    root.mainloop()
