from enum import Enum
Cord = tuple[int,int] 
class ColorName(Enum):
    WHITE = 0
    BLACK = 1
    NONE = 2
class PieceName(Enum):
    ROOK = 6
    BISHOP = 5
    QUEEN = 4
    PAWN = 3
    KING = 2
    KNIGHT = 1
    NONE = 0


Piece = dict[str:ColorName,str:PieceName]
Move = tuple[Cord,Cord,str] # str is for promotion
#region Basic Functions

def in_bounds(cord: Cord,x_max=7,y_max=7):
    under_max = (cord[0] <= x_max) and (cord[1] <= y_max)
    over_min = (cord[0] >= 0) and (cord[1] >= 0)
    return under_max and over_min

def add_cord(cord_1: Cord, cord_2: Cord):

    return (cord_1[0] + cord_2[0],cord_1[1] + cord_2[1])
#endregion
a = 1
class square_reaction(Enum):
    STOP = "STOP"
    CAPTURE = "CAPTURE"
    CONTINUE = "CONTINUE"
def check_square(square_cord,Board, self_color: ColorName):
    
    if in_bounds(square_cord):
        on_move_to = Board.read(square_cord)
        if on_move_to == None:
            return square_reaction.CONTINUE
        elif on_move_to.color != self_color:
            return square_reaction.CAPTURE
        else:
            return square_reaction.STOP
    else:
        return square_reaction.STOP
        

def king(cord,Board,self_color: ColorName):
    moves = []
    offsets = [0,-1,1]
    for off_x in offsets:
        for off_y in offsets:
            if (off_x == off_y) and off_y == 0:
                continue
            move_to = cord
            move_to[0] += off_x
            move_to[1] += off_y

            this_move = (cord,move_to)
            match check_square(move_to,Board=Board,self_color=self_color):
                case square_reaction.STOP:
                    continue
                case square_reaction.CAPTURE:
                    moves.append(this_move)
                case square_reaction.CONTINUE:
                    moves.append(this_move)
    return moves
def pawn(cord,Board,self_color: ColorName):
    no_promotion_moves = []
    #region just forward move
    
    steps = 1
    
    if self_color == ColorName.BLACK:
        direction = -1
        double_rank = 6
        promotion_rank = 0
    else: # self_color == Color.WHITE
        direction = 1
        double_rank = 1
        promotion_rank = 7

    if cord[1] == double_rank:
        steps *= 2
    
    for step in range(1,3):
        move_to = cord
        move_to[1] += step * direction
        
        
        if in_bounds(move_to):
            if Board.read(move_to) == None:
                this_move = (cord,move_to)
                no_promotion_moves.append(tuple([this_move]))
    #endregion
    #region attack
    left_right_offsets = [-1,1]
    for offset in left_right_offsets:
        move_to = cord 
        
        
        move_to[0] += direction
        move_to[1] += left_right_offsets
        on_move_to = Board.read(move_to)
        this_move = (cord,move_to)
        if in_bounds(move_to) and on_move_to != None:
            if on_move_to.color != self_color:
                no_promotion_moves.append(this_move)
    #endregion
    #region promotion
    moves = []

    promotion_options = [PieceName.ROOK,PieceName.BISHOP,PieceName.KNIGHT,PieceName.QUEEN]
    for np_move in no_promotion_moves:
        if np_move[1][1] == promotion_rank:
            
            for option in promotion_options:
                moves.append((np_move + (option)))
        else:
            moves.append(np_move)
    #endregion
    return moves # (:
def rook(cord,Board,self_color: ColorName):
    moves = []
    offsets = [-1,1]
    for axe_iter in range(2):
        for off in offsets:
            for step in range(8):
                
                move_to = cord
                move_to[axe_iter] += off*step
                if in_bounds(move_to):
                    this_move = (cord, move_to)
                    
                    match check_square(move_to,Board=Board,self_color=self_color):
                        case square_reaction.STOP:
                            break
                        case square_reaction.CAPTURE:
                            moves.append(this_move)
                            break
                        case square_reaction.CONTINUE:
                            moves.append(this_move)
                            continue


    return moves                                     
def bishop(cord,Board, self_color: ColorName):
    moves = []
    offsets = [-1,1]
    for off_x in offsets:
        for off_y in offsets:
            for step in range(8):
                move_to = cord
                move_to[0] += step * off_x
                move_to[1] += step * off_y
                
                this_move = (cord, move_to)
                match check_square(move_to,Board=Board,self_color=self_color):
                    case square_reaction.STOP:
                        break
                    case square_reaction.CAPTURE:
                        moves.append(this_move)
                        break
                    case square_reaction.CONTINUE:
                        moves.append(this_move)
                        continue
    return moves
def queen(cord,Board, self_color: ColorName):
    
    bishop_moves: list[Move] = bishop(cord,Board,self_color)
    rook_moves: list[Move] = rook(cord,Board,self_color)
    moves: list[Move] = bishop_moves
    for rook_move in rook_moves:
        moves.append(rook_move)
    return moves 
def knight(cord,Board,self_color: ColorName): # worth 3 pieces

    raw_raw_moves = []
    trunk_offsets = [-2,2]
    branch_offsets = [-1,1]
    for ax_iter in range(2):
        for trunk_off in trunk_offsets:
            for branch_off in branch_offsets:
                destination = cord
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
 
    

                

              