from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board_state):
        """Every player must define its own move"""
        pass


class HumanPlayer(Player):
    def get_move(self, board_state):
        return None