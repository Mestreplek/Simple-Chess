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
def rook(cord,Board):
    pass
def bishop(cord,Board):
    pass
def queen(cord,Board):
    pass

def knight(cord,Board): # worth 3 pieces

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

    self_color = Board.read(cord)["color"]
    moves = []
    for move in raw_moves:
        if Board.read(move[1])["color"] != self_color:
            moves.append(move)
    return moves
 
    

                

              