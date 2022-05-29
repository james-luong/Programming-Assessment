"""
03_Assistance_v2
In 03_Assistance_v1 user can click assist button multiple time which can
eliminate all wrong answers
Make assist button disabled after one click
Add 'next question' button and click to restore assist and answer buttons
"""

from tkinter import *
import random

# questions and answers will be in the list similar to this list
quest_ans_list = ['Questions', 'correct answer', 'answer 2', 'answer 3',
                  'answer 4']

class Main:
    def __init__(self):
        self.background = 'light green'

        # quiz main screen GUI
        self.main_frame = Frame(width=500, height=300, bg=self.background)
        self.main_frame.grid()

        # main label
        Label(self.main_frame, text='Te Reo Maori Quiz', bg=self.background,
              font='Arial 14 bold').grid(row=0, pady=10)

        # assist button
        self.assist_button = Button(self.main_frame, text='Assistance',
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
        self.answer_1 = Button(self.answer_frame, text=quest_ans_list[1],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_1.grid(row=0, column=0)
        self.answer_1.config(width=7)

        self.answer_2 = Button(self.answer_frame, text=quest_ans_list[2],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_2.grid(row=0, column=1)
        self.answer_2.config(width=7)

        self.answer_3 = Button(self.answer_frame, text=quest_ans_list[3],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_3.grid(row=1, column=0, padx=5, pady=5)
        self.answer_3.config(width=7)

        self.answer_4 = Button(self.answer_frame, text=quest_ans_list[4],
                               font='arial 10 bold', padx=60, pady=10)
        self.answer_4.grid(row=1, column=1, padx=5, pady=5)
        self.answer_4.config(width=7)

    def assist(self):
        # disable assist button for now
        self.assist_button.config(state=DISABLED)
        # list of answers can be removed (i.e. not correct answers)
        ans_to_del = []

        for answer in range(1, 5):
            # append to ans_to_del list if answer is not correct
            if quest_ans_list[answer] != 'correct answer':
                ans_to_del.append(quest_ans_list[answer])

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
        self.answer_1.config(state=NORMAL)
        self.answer_2.config(state=NORMAL)
        self.answer_3.config(state=NORMAL)
        self.answer_4.config(state=NORMAL)
        self.assist_button.config(state=NORMAL)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Main()
    root.mainloop()
