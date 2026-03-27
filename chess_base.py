from enum import Enum
from pieces import ColorName
from pieces import PieceName
# tells where it can move to 
# legality is handled with Game
class Move: # just data.
    pass

cord = tuple(int,int)


class Square:
    def __init__(self,piece_name: PieceName=None,color_name: ColorName=None):
        
        if ((piece_name == None) and( color_name == None)) or ((piece_name != None) and (color_name != None))
            self.piece_name = piece_name
            self.color_name = color_name
        else:
            raise "Square init error"
# Board does not store individual instances of "Piece" it only stores pointes to a piece
class Board: # only data storage, writing reading
    def __init__(self,data=None):
        side_length = 8
        if data == None:
            self.data = []
            for i in range(side_length):
                self.data.append([Square() for i in range(side_length)])
        else:
            self.data = data 
    def readSquare(self,cord):
        return self.data[cord[0]][cord[1]]
    def writeSquare(self,piece_name: PieceName,cord,color_name: ColorName):
        self.data[cord[0]][cord[1]] = Square(piece_name,color_name)




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
