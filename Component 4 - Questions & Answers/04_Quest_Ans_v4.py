"""
04_Quest_Ans_v4
Make buttons that user click red if it's wrong, and make correct answer green
at the same time
Disable all answer buttons once an answer button is clicked, and re-activate it
after next question button is clicked.
"""

from tkinter import *
from random import shuffle
import csv

quest_ans_list = []
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

chosen_num_quest = 20
quest_num = 0

class Quiz:
    def __init__(self):
        self.background = 'light green'

        # quiz main screen GUI
        self.main_frame = Frame(width=500, height=300, bg=self.background)
        self.main_frame.grid()

        # main label
        Label(self.main_frame, text='Te Reo Maori Quiz', bg=self.background,
              font='Arial 14 bold').grid(row=0, pady=10)

        # quest label
        self.quest_label = Label(self.main_frame, bg='red', justify=LEFT,
                                 text=quest_ans_list[0][0],
                                 font='Arial 16 bold', wrap=380)
        self.quest_label.grid(row=1)
        self.quest_label.config(width=28, height=3)

        # next question button
        self.next_quest_button = Button(self.main_frame, text='Next question',
                                        command=self.next_quest)
        self.next_quest_button.grid(row=1, column=1, padx=5)

        # question number label
        self.no_quest = Label(self.main_frame,
                              text=f'Question: {quest_num + 1}/'
                                   f'{chosen_num_quest}')
        self.no_quest.grid(row=2, column=1, padx=5)

        # answer frame
        self.answer_frame = Frame(self.main_frame, bg=self.background)
        self.answer_frame.grid(row=2, pady=10)

        # answer buttons
        # using config to make fixed button size
        # add command to buttons
        self.answer_1 = Button(self.answer_frame,
                               text=quest_ans_list[0][1][0],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][0]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_1.grid(row=0, column=0, padx=5, pady=5)
        self.answer_1.config(width=7)

        self.answer_2 = Button(self.answer_frame,
                               text=quest_ans_list[0][1][1],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][1]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_2.grid(row=0, column=1, padx=5, pady=5)
        self.answer_2.config(width=7)

        self.answer_3 = Button(self.answer_frame,
                               text=quest_ans_list[0][1][2],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][2]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)
        self.answer_3.config(width=7)

        self.answer_4 = Button(self.answer_frame,
                               text=quest_ans_list[0][1][3],
                               command=lambda: self.check_ans(quest_ans_list[0]
                                                              [1][3]),
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)
        self.answer_4.config(width=7)

    def next_quest(self):
        # make quest_num, quest_ans_list global
        global quest_num, quest_ans_list

        # increase number of questions whenever user click next question button
        quest_num += 1

        # when the number of questions reach the maximum (chosen question
        # number), disable all buttons
        if quest_num == chosen_num_quest:
            self.answer_1.config(state=DISABLED)
            self.answer_2.config(state=DISABLED)
            self.answer_3.config(state=DISABLED)
            self.answer_4.config(state=DISABLED)
            self.next_quest_button.config(state=DISABLED)

        else:
            # delete the first question & answers list so that it does not
            # repeat
            quest_ans_list.pop(0)

            # shuffle all questions so that they will not be shown in the
            # same order every time
            quest_ans_list = [i for i in quest_ans_list]
            shuffle(quest_ans_list)

            # also shuffle answers in a question so that they will not be in
            # the same position every time
            quest_ans_list[0][1] = [i for i in quest_ans_list[0][1]]
            shuffle(quest_ans_list[0][1])
            print(quest_ans_list)

            # display number of questions users are up to
            self.no_quest.config(text=f'Question: {quest_num + 1}/'
                                      f'{chosen_num_quest}')

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
        # turn correct answer buttons to green when user click one of the
        # answer buttons
        if self.answer_1['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_1.config(bg='green')

        elif self.answer_2['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_2.config(bg='green')

        elif self.answer_3['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_3.config(bg='green')

        elif self.answer_4['text'] == quest_ans_dict[quest_ans_list[0][0]]:
            self.answer_4.config(bg='green')

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
    program = Quiz()
    root.mainloop()
