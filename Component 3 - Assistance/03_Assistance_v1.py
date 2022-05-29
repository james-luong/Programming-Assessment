"""
03_Assistance_v1
Create assistance button that allows use to eliminate 2 wrong answers
Disable 2 wrong answer buttons randomly
"""

from tkinter import *
import random

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Main()
    root.mainloop()
