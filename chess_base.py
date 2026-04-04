from enum import Enum
from pieces import ColorName
from pieces import PieceName
from pieces import Move
from copy import deepcopy
# tells where it can move to 
# legality is handled with Game
import pieces
cord = tuple(int,int)


class Square:
    def __init__(self,piece_name: PieceName=None,color_name: ColorName=None):
        
        if ((piece_name == None) and( color_name == None)) or ((piece_name != None) and (color_name != None))
            self.piece_name = piece_name
            self.color_name = color_name
        else:
            raise "Square init error"
# Board does not store individual instances of "Piece" it only stores pointes to a piece
class Board: # only data storage of pieces, writing reading
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
    BLACK_WON = ColorName.BLACK
    WHITE_WON = ColorName.WHITE
    DRAW = 2
    ACTIV_GAME = 3
PieceName_to_movable_moves_func: dict = {
    1:1
    # TODO 
}



def get_board_after_move(board: Board,move: Move):
    
    moving_Square_cord = move[0]


    moving_Square: Square = board.readSquare(moving_Square_cord)
    
    
    if len(Move) == 3: 
        moving_Square.piece_name = move[2] # is a promoting pawn
    

    # piece on moving square lands on destination
    destination_cord = move[1]
    board.writeSquare(moving_Square.piece_name,destination_cord,moving_Square.color_name)
    

    # moving gets cleared to avoid duplicates
    board.writeSquare(PieceName.NONE,moving_Square_cord,ColorName.NONE)



    return board


def is_attacked(board: Board, cord, attacked_color: ColorName):
    
    make_move_PieceName: PieceName 
    movable_moves_func: function 
    for make_move_PieceName, movable_moves_func in PieceName_to_movable_moves_func.items():
        
        movable_moves = movable_moves_func(cord=cord,board=board,self_color=attacked_color)
        
        # iter through movable moves 
        for move in movable_moves:
            
            destination_cord = move[1]

            destination_piece: Square = board.readSquare(destination_cord)
            
            if destination_piece.color_name == ColorName.NONE:
                continue
            elif destination_piece.color_name != attacked_color: # this is redundant 
                if destination_piece.piece_name == make_move_PieceName:
                    return True
                if make_move_PieceName == PieceName.ROOK or make_move_PieceName == PieceName.BISHOP:
                    if  destination_piece.piece_name == PieceName.QUEEN:
                        return True
    
    return False
def isBoardLegal(board: Board,turn_color: ColorName)->bool:

    # do black and white both have a king?
    white_kings: int = 0 
    black_kings: int = 0

    not_moiving_king: Square
    not_moiving_king_cord: tuple[int,int]
    for i in range(8):
        for j in range(8):
            cord = (i,j)
            square: Square = board.readSquare(cord=cord)
            
            if square.piece_name == PieceName.KING:
                if square.color_name == ColorName.WHITE:
                    white_kings += 1
                else:
                    black_kings += 1
                if square.color_name != turn_color:
                    not_moiving_king = square
                    not_moiving_king_cord = cord
    
    if white_kings != 1 or black_kings != 1:
        return False 
    if is_attacked(board=board,cord=not_moiving_king_cord,attacked_color=not_moiving_king.color_name):
        return False

    
    return True
def isInCheck(board: Board, turn_color: ColorName) -> bool: 
    king_cord: tuple[int,int]
    for i in range(8):
        for j in range(8):
            cord = (i,j)
            square: Square = board.readSquare(cord=cord)
            if square.piece_name == PieceName.KING and square.color_name == turn_color:
                king_cord = cord
                break
    return is_attacked(board=board,cord=king_cord,attacked_color=turn_color)
class ChessBoard: # handles legality, execution of moves, win condition. Dosent enforce anything just tells whats legal
    def __init__(self,isNormalSetup = True):
        self.turn_color: ColorName = ColorName.WHITE
        
        if isNormalSetup == True:
            board = Board() 
            white_black_pawn_range = [1,6]
            white_black_color_name = [ColorName.WHITE,ColorName.BLACK]
            
            white_black_king_range = [0,7]
            piece_sequence = [PieceName.ROOK,PieceName.KNIGHT,PieceName.BISHOP,PieceName.KING,PieceName.QUEEN,PieceName.BISHOP,PieceName.KNIGHT,PieceName.ROOK]
            for i in range(8):
                for color_iter in range(2):
                    pawn_cord = (i,white_black_pawn_range[color_iter])
                    board.writeSquare(PieceName.PAWN,pawn_cord,white_black_color_name[color_iter])
                    piece_cord = (i,white_black_king_range[color_iter]) 
                    board.writeSquare(piece_sequence[i],piece_cord,white_black_color_name[color_iter])
    def get_movable_moves(self) -> list[Move]:
        moves = []
        for i in range(8):
            for j in range(8):
                cord = (i,j)

                square: Square = self.board.readSquare(cord)
            
                if square.color_name == self.turn.color:
                    movable_moves_func = PieceName_to_movable_moves_func[square.piece_name]
                    moves = moves + movable_moves_func(self.Board,square.color_name)
                
        return moves
    def get_legal_moves(self):

        legal_moves = []
        movable_moves = self.get_movable_moves()
        for move in movable_moves:

            board_after_move: Board = get_board_after_move(board=self.board,move=move)
            if isBoardLegal(board=board_after_move,turn_color=self.turn_color):
                legal_moves.append(move)
        return legal_moves
    def ChessBoard_after_move(self,move: Move) -> "ChessBoard":
        pass
    def do_next_state(self,move: Move) -> None:
        self = self.ChessBoard_after_move(move=move)
    def getWinState(self) -> WinState:
        #1 checks if no moves are avaible for
        
        legal_moves = self.get_legal_moves()
        if len(legal_moves) == 0:
            if isInCheck(board=self.board,turn_color=self.turn_color):
                win_state = self.turn_color
            else:
                win_state = WinState.DRAW
        else:
            win_state = WinState.ACTIV_GAME
        return win_state
