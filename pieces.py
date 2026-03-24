from enum import Enum
Cord = tuple[int,int] 
class Color(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"
class PieceName(Enum):
    ROOK = "Rook"
    BISHOP = "BIshop"
    QUEEN = "Queen"
    PAWN = "Pawn"
    KING = "King"
    KNIGHT = "Knight"


Piece = dict[str:Color,str:PieceName]
Move = tuple[Cord,Cord]
#region Basic Functions

def in_bounds(cord: Cord,x_max=7,y_max=7):
    under_max = (cord[0] <= x_max) and (cord[1] <= y_max)
    over_min = (cord[0] >= 0) and (cord[1] >= 0)
    return under_max and over_min

def add_cord(cord_1: Cord, cord_2: Cord):

    return (cord_1[0] + cord_2[0],cord_1[1] + cord_2[1])
#endregion

def pawn(cord,Board,self_color: Color):
    
    steps = 1
    double_rank = 1
    if self_color == Color.BLACK:
        step = -1
        double_rank = 6
    
    if cord[1] == double_rank:
        step *= 2
    
        

def rook(cord,Board,self_color: Color):
    moves = []
    offsets = [-1,1]
    for axe_iter in range(2):
        for off in offsets:
            for step in range(8):
                
                move_to = cord
                move_to[axe_iter] += off*step
                if in_bounds(move_to):
                    
                    on_move_to = Board.read(move_to)
                    this_move = (cord, move_to)
                    if on_move_to = None:
                        moves.append(this_move))
                    elif on_move_to.color != self_color:
                        moves.append(this_move)
                        break
                    else:
                        break
    return moves                                     
def bishop(cord,Board, self_color: Color):
    moves = []
    offsets = [-1,1]
    for off_x in offsets:
        for off_y in offsets:
            for step in range(8):
                move_to = cord
                move_to[0] += step * off_x
                move_to[1] += steo * off_y
                if in_bounds(move_to):
                    
                    on_move_to = Board.read(move_to)
                    this_move = (cord, move_to)
                    if on_move_to = None:
                        moves.append(this_move))
                    elif on_move_to.color != self_color:
                        moves.append(this_move)
                        break
                    else:
                        break
    return moves
def queen(cord,Board, self_color: Color):
    
    bishop_moves: list[Move] = bishop(cord,Board,self_color)
    rook_moves: list[Move] = rook(cord,Board,self_color)
    moves: list[Move] = bishop_moves
    for rook_move in rook_moves:
        moves.append(rook_move)
    return moves 

def knight(cord,Board,self_color: Color): # worth 3 pieces

    raw_raw_moves = []
    trunk_offsets = [-2,2]
    branch_offsets = [-1,1]
    for ax_iter in range(2):
        for trunk_off in trunk_offsets:
            for branch_off in branch_offsets:
                destination: Cord = cord
                destination[ax_iter] += trunk_off

                destination[int((1-ax_iter)==1)] += branch_off
                raw_raw_moves.append((cord,destination))
    raw_moves = []
    for move in raw_raw_moves:
        if in_bounds(move[0]):
            raw_moves.append(move)

    
    moves = []
    for move in raw_moves:
        if Board.read(move[1])["color"] != self_color:
            moves.append(move)
    return moves
 
    

                

              