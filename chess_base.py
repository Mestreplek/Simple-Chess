from enum import Enum
# tells where it can move to 
# legality is handled with Game
class Move: # just data.
    pass

cord = tuple(int,int)

class Piece: 
    def __init__(self):
        pass
    def get_movable_moves(self,location) -> list[Move]: # movable_moves are moves wich are legall if you ignore checks
        pass

# Board does not store individual instances of "Piece" it only stores pointes to a piece
class Board: # only data storage, writing reading
    def __init__(self):
        pass
    def read(self):
        pass
    def write(self):
        pass

class WinState(Enum):
    BLACK_WON = "Black won"
    WHITE_WON = "White won"
    DRAW = "Draw"
    ACTIV_GAME = "Activ game"

class ChessBoard: # handles legality, execution of moves, win condition. Dosent enforce anything just tells whats legal
    def __init__(self):
        pass
    def get_movable_moves(self) -> list[Move]:
        pass
    def state_after_move(self,move: Move) -> "ChessBoard":
        pass
    def do_next_state(self,move: Move) -> None:
        self = self.state_after_move(move=move)
    def winner() -> WinState:
        pass
