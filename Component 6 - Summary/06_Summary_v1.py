from tkinter import *

class Summary:
    def __init__(self):
        self.background = 'orange'

        self.main_frame = Frame(height=400, width=300, bg=self.background)
        self.main_frame.grid()

        self.main_label = Label(self.main_frame, text='CONGRATULATIONS',
                                font='arial 16 bold', bg=self.background)
        self.main_label.grid(row=0, padx=10, pady=10)

        self.scores = Label(self.main_frame, text='You got ?/15',
                            font='arial 14', bg=self.background)
        self.scores.grid(row=1, pady=10, padx=10)

        self.sub_frame = Frame(self.main_frame, bg=self.background)
        self.sub_frame.grid(row=2)

        self.end_game = Button(self.sub_frame, text='End Game',
                               font='arial 13')
        self.end_game.grid(row=0, padx=10, pady=10)

        self.restart = Button(self.sub_frame, text='Restart',
                               font='arial 13')
        self.restart.grid(row=0, column=1, padx=10, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Maori Quiz")
    program = Summary()
    root.mainloop()