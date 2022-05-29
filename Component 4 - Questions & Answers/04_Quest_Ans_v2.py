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
        quest_ans_dict[row[0]] = row[-1]

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
                                 text=quest_ans_list[quest_num][0],
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
        self.answer_1 = Button(self.answer_frame,
                               text=quest_ans_list[quest_num][1][0],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_1.grid(row=0, column=0)
        self.answer_1.config(width=7)

        self.answer_2 = Button(self.answer_frame,
                               text=quest_ans_list[quest_num][1][1],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_2.grid(row=0, column=1)
        self.answer_2.config(width=7)

        self.answer_3 = Button(self.answer_frame,
                               text=quest_ans_list[quest_num][1][2],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)
        self.answer_3.config(width=7)

        self.answer_4 = Button(self.answer_frame,
                               text=quest_ans_list[quest_num][1][3],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)
        self.answer_4.config(width=7)

    def next_quest(self):
        global quest_num, quest_ans_list
        quest_num += 1

        if quest_num == chosen_num_quest:
            self.answer_1.config(state=DISABLED)
            self.answer_2.config(state=DISABLED)
            self.answer_3.config(state=DISABLED)
            self.answer_4.config(state=DISABLED)
            self.next_quest_button.config(state=DISABLED)

        else:
            quest_ans_list.pop(0)
            print(quest_ans_list)

            quest_ans_list = [i for i in quest_ans_list]
            shuffle(quest_ans_list)

            quest_ans_list[0][1] = [i for i in quest_ans_list[0][1]]
            shuffle(quest_ans_list[0][1])

            self.no_quest.config(text=f'Question: {quest_num + 1}/'
                                      f'{chosen_num_quest}')

            self.quest_label.config(text=quest_ans_list[0][0])
            self.answer_1.config(state=NORMAL,
                                 text=quest_ans_list[0][1][0])
            self.answer_2.config(state=NORMAL,
                                 text=quest_ans_list[0][1][1])
            self.answer_3.config(state=NORMAL,
                                 text=quest_ans_list[0][1][2])
            self.answer_4.config(state=NORMAL,
                                 text=quest_ans_list[0][1][3])

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Quiz()
    root.mainloop()
