from enum import Enum
# tells where it can move to 
# legality is handled with Game

cord = tuple(int,int)



# Board does not store individual instances of "Piece" it only stores pointes to a piece
class Board: # only data storage, writing reading
    def __init__(self,data):
        self.data = data 
    def read(self,cord):
        return self.data[cord[0]][cord[1]
    def write(self,cord,new_value):
        self.data[cord[0]][cord[1] = new_value




class WinState(Enum):
    BLACK_WON = 0
    WHITE_WON = 1
    DRAW = 2
    ACTIV_GAME = 3

class ChessBoard: # handles legality, execution of moves, win condition. Dosent enforce anything just tells whats legal
    def __init__(self):
        pass
    def get_movable_moves(self) -> list[Move]:
        pass
    def get_legal_moves():
        pass
    def state_after_move(self,move: Move) -> "ChessBoard":
        pass
    def do_next_state(self,move: Move) -> None:
        self = self.state_after_move(move=move)
    def winner() -> WinState:
        pass
