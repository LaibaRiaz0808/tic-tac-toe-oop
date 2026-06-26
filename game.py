import tkinter as tk
from tkinter import messagebox

from player import HumanPlayer
from ai_player import AIPlayer


class TicTacToe:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart OOP Tic Tac Toe")

        self.board = [''] * 9

        self.player1 = HumanPlayer('X')
        self.player2 = AIPlayer('O')

        self.current_player = self.player1

        self.buttons = []

        self.create_board()

    def create_board(self):

        for i in range(9):

            btn = tk.Button(
                self.root,
                text='',
                font=('Arial',24),
                width=5,
                height=2,
                command=lambda i=i:self.make_move(i)
            )

            btn.grid(row=i//3,column=i%3)

            self.buttons.append(btn)

    def make_move(self,index):

        if self.board[index]=='' and self.current_player==self.player1:

            self.update_board(index)

            if not self.check_game_over():

                self.switch_player()

                ai_move=self.player2.get_move(self.board)

                if ai_move is not None:

                    self.update_board(ai_move)

                    self.check_game_over()

                    self.switch_player()

    def update_board(self,index):

        self.board[index]=self.current_player.symbol

        self.buttons[index].config(text=self.current_player.symbol)

    def switch_player(self):

        if self.current_player==self.player1:

            self.current_player=self.player2

        else:

            self.current_player=self.player1

    def check_game_over(self):

        wins=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for w in wins:

            if self.board[w[0]]==self.board[w[1]]==self.board[w[2]]!='':

                messagebox.showinfo(
                    "Game Over",
                    f"Player {self.current_player.symbol} Wins!"
                )

                self.reset()

                return True

        if '' not in self.board:

            messagebox.showinfo(
                "Game Over",
                "It's a Draw!"
            )

            self.reset()

            return True

        return False

    def reset(self):

        self.board=['']*9

        for btn in self.buttons:

            btn.config(text='')

        self.current_player=self.player1