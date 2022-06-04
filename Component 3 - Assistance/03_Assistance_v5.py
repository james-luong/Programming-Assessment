"""
03_Assistance_v4
Using dictionary to check correct answers
Shuffle answer positions so that correct answers don't stay at the same
position for all questions
"""

from tkinter import *
import random
from random import shuffle

# questions and answers will be in the list similar to this list
quest_ans_list = [['Questions'], ['correct answer', 'answer 2', 'answer 3',
                  'answer 4']]
quest_ans_dict = {'Questions': 'correct answer'}

class Main:
    def __init__(self):
        self.background = 'light green'

        # quiz main screen GUI
        self.main_frame = Frame(width=500, height=300, bg=self.background)
        self.main_frame.grid()

        # number of assists user can use
        self.num_assist = 10

        # main label
        Label(self.main_frame, text='Te Reo Maori Quiz', bg=self.background,
              font='Arial 14 bold').grid(row=0, pady=10)

        # assist button
        self.assist_button = Button(self.main_frame,
                                    text=f'Assistance (50/50): '
                                         f'{self.num_assist}',
                                    command=self.assist)
        self.assist_button.grid(row=1)

        # next question button
        self.next_quest_button = Button(self.main_frame, text='Next question',
                                        command=self.next_quest)
        self.next_quest_button.grid(row=1, column=1, padx=5)

        # answer frame
        self.answer_frame = Frame(self.main_frame, bg=self.background)
        self.answer_frame.grid(row=2, pady=10)

        # answer buttons
        # using config to make fixed button size
        self.answer_1 = Button(self.answer_frame, text=quest_ans_list[1][0],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_1.grid(row=0, column=0, padx=5, pady=5)
        self.answer_1.config(width=7)

        self.answer_2 = Button(self.answer_frame, text=quest_ans_list[1][1],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_2.grid(row=0, column=1, padx=5, pady=5)
        self.answer_2.config(width=7)

        self.answer_3 = Button(self.answer_frame, text=quest_ans_list[1][2],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)
        self.answer_3.config(width=7)

        self.answer_4 = Button(self.answer_frame, text=quest_ans_list[1][3],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)
        self.answer_4.config(width=7)

    def assist(self):
        # decrease number of assist when user click assist button
        self.num_assist -= 1

        # update new number of assist left for user
        self.assist_button.configure(text=f'Assistance (50/50): '
                                          f'{self.num_assist}')

        # disable assist button for now
        self.assist_button.config(state=DISABLED)

        # list of answers can be removed (i.e. not correct answers)
        to_delete = set(random.sample(range(len(quest_ans_list[1])), 2))
        remain_list = [x for i, x in enumerate(quest_ans_list[1]) if not i in \
                                                                 to_delete]

        # disable answer that is not correct
        if self.answer_1['text'] not in remain_list:
            self.answer_1.config(state=DISABLED)

        if self.answer_2['text'] not in remain_list:
            self.answer_2.config(state=DISABLED)

        if self.answer_3['text'] not in remain_list:
            self.answer_3.config(state=DISABLED)

        if self.answer_4['text'] not in remain_list:
            self.answer_4.config(state=DISABLED)

    def next_quest(self):
        quest_ans_list[1] = [i for i in quest_ans_list[1]]
        shuffle(quest_ans_list[1])
        print(quest_ans_list)
        self.answer_1.config(state=NORMAL, text=quest_ans_list[1][0])
        self.answer_2.config(state=NORMAL, text=quest_ans_list[1][1])
        self.answer_3.config(state=NORMAL, text=quest_ans_list[1][2])
        self.answer_4.config(state=NORMAL, text=quest_ans_list[1][3])

        if self.num_assist > 0:
            self.assist_button.config(state=NORMAL)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Main()
    root.mainloop()
