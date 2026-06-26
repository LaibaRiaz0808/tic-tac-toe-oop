import random
from player import Player


class AIPlayer(Player):
    def get_move(self, board_state):

        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        # Rule 1: Win if possible
        for w in wins:
            line = [board_state[w[0]], board_state[w[1]], board_state[w[2]]]

            if line.count(self.symbol) == 2 and line.count('') == 1:
                for index in w:
                    if board_state[index] == '':
                        return index

        # Rule 2: Block Human
        human_symbol = 'X' if self.symbol == 'O' else 'O'

        for w in wins:
            line = [board_state[w[0]], board_state[w[1]], board_state[w[2]]]

            if line.count(human_symbol) == 2 and line.count('') == 1:
                for index in w:
                    if board_state[index] == '':
                        return index

        # Rule 3: Random Move
        available = [i for i, x in enumerate(board_state) if x == '']

        return random.choice(available) if available else None