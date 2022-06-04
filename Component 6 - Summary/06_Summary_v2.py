"""
06_Summary_v2
Create basic frame with two buttons, replay and end game
Replay button bring back to Instructions
End game button shows farewell words
"""

from tkinter import *

score = int(input('Number of correct answers: '))
chosen_quest_num = int(input('Chosen number of questions: '))

# instructions
class Instruction:
    def __init__(self):
        # instructions background
        self.background = 'light blue'

        # main frame
        self.main_frame = Frame(height=400, width=300, bg=self.background)
        self.main_frame.grid()

        # instruction label
        self.instruction_label = Label(self.main_frame,
                                       text='Back to Instructions',
                                       font='arial 16 bold',
                                       bg=self.background)
        self.instruction_label.grid(row=0, padx=10, pady=10)

# summary user's scores
class Summary:
    def __init__(self):
        # summary background
        self.background = 'orange'

        # main frame
        self.main_frame = Frame(height=400, width=300, bg=self.background)
        self.main_frame.grid()

        # congrats label
        self.main_label = Label(self.main_frame, text='CONGRATULATIONS',
                                font='arial 16 bold', bg=self.background)
        self.main_label.grid(row=0, padx=10, pady=10)

        # show user's scores
        self.scores = Label(self.main_frame, font='arial 14',
                            bg=self.background,
                            text=f'You got {score}/{chosen_quest_num}')
        self.scores.grid(row=1, pady=10, padx=10)

        # sub frame for buttons
        self.sub_frame = Frame(self.main_frame, bg=self.background)
        self.sub_frame.grid(row=2)

        # end game button
        self.end_game = Button(self.sub_frame, text='End Game',
                               command= self.end_game, font='arial 13')
        self.end_game.grid(row=0, padx=10, pady=10)

        # replay button
        self.restart = Button(self.sub_frame, text='Replay',
                              command = self.replay, font='arial 13')
        self.restart.grid(row=0, column=1, padx=10, pady=10)

    def replay(self):
        # delete old main frame
        self.main_frame.grid_forget()
        self.main_frame.destroy()
        Instruction()

    def end_game(self):
        # delete old main frame
        self.main_frame.destroy()

        # new main frame
        self.main_frame = Frame(height=400, width=300, bg=self.background)
        self.main_frame.grid()

        # farewell label
        farewell_label = Label(self.main_frame, text='Thank you for playing',
                                font='arial 16 bold', bg=self.background)
        farewell_label.grid(row=0, padx=10, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Summary()
    root.mainloop()