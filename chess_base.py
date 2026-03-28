from enum import Enum
from pieces import ColorName
from pieces import PieceName
# tells where it can move to 
# legality is handled with Game

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
    BLACK_WON = 0
    WHITE_WON = 1
    DRAW = 2
    ACTIV_GAME = 3

class ChessBoard: # handles legality, execution of moves, win condition. Dosent enforce anything just tells whats legal
    def __init__(self,isNormalSetup = True):

        if isNormalSetup == True:
            board = Board() 
            white_black_pawn_range = [1,6]
            white_black_color_name = [ColorName.WHITE,ColorName.BLACK]
            
            white_black_king_range = [0,7]
            piece_sequence = [PieceName.ROOK,PieceName.KNIGHT,PieceName.BISHOP,PieceName.KING,PieceName.QUEEN,PieceName.BISHOP,PieceName.KNIGHT,PieceName.ROOK]
            for i in range(8):
                for c in range(2)
                    pawn_cord = (white_black_pawwn_range[c],i)
                    board.writeSquare(PieceName.PAWN,pawn_cord,white_black_color_name[c])
                    piece_cord = (white_black_[c],
                    board.writeSquare(piece_sequence[i],piece_cord,white_blak_color_name[c])
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
