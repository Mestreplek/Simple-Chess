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

def get_opposite_color(color:ColorName) -> ColorName:
        if color == ColorName.WHITE:
            return ColorName.BLACK
        else:
            return ColorName.WHITE 
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
def check_square(square_cord,board, self_color: ColorName):
    
    if in_bounds(square_cord):
        on_move_to = board.readSquare(square_cord)
        if on_move_to.piece_name == PieceName.NONE:
            return square_reaction.CONTINUE 
        elif on_move_to.color_name == get_opposite_color(self_color):
            return square_reaction.CAPTURE
        else:
            return square_reaction.STOP
    else:
        return square_reaction.STOP
def get_king_movable_moves(cord,board,self_color: ColorName):
    moves = []
    offsets = [0,-1,1]
    for off_x in offsets:
        for off_y in offsets:
            if (off_x == off_y) and off_y == 0:
                continue
            move_to = list(cord)
            move_to[0] += off_x
            move_to[1] += off_y

            this_move = (cord,move_to)
            match check_square(move_to,board=board,self_color=self_color):
                case square_reaction.STOP:
                    continue
                case square_reaction.CAPTURE:
                    moves.append(this_move)
                case square_reaction.CONTINUE:
                    moves.append(this_move)
    return moves
def get_pawn_movable_moves(cord,board,self_color: ColorName):
    no_promotion_moves = []
    #region just forward move
    cord = list(cord)
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
    
    for step in range(1,steps+1):
        move_to = list(cord)
        move_to[1] += step * direction
        
        
        if in_bounds(move_to):
            if board.readSquare(move_to).piece_name == PieceName.NONE:
                this_move = [cord,move_to]
                no_promotion_moves.append(this_move)
    #endregion
    #region attack
    left_right_offsets = [-1,1]
    for offset in left_right_offsets:
        move_to = list(cord) 
        
        
        move_to[0] += direction
        move_to[1] += offset
        
        
        if in_bounds(move_to):
            
            on_move_to = board.readSquare(move_to)
            if on_move_to.piece_name != PieceName.NONE:
                if on_move_to.color_name != self_color:
                    this_move = (cord,move_to)
                    no_promotion_moves.append(this_move)
    #endregion
    #region promotion
    moves = []

    promotion_options = [PieceName.ROOK,PieceName.BISHOP,PieceName.KNIGHT,PieceName.QUEEN]
    for no_promotion_move in no_promotion_moves:
        if no_promotion_move[1][1] == promotion_rank:
            
            for option in promotion_options:
                moves.append((list(no_promotion_move )+ [option]))
        else:
            moves.append(no_promotion_move)
    #endregion
    return moves # (:
def get_rook_movable_moves(cord,board,self_color: ColorName):
    moves = []
    offsets = [-1,1]
    for axe_iter in range(2): # cord[axe_iter]
        for off in offsets:
            for step in range(1,8):
                
                move_to = list(cord)
                move_to[axe_iter] += off*step
                if in_bounds(move_to):
                    this_move = (cord, move_to)
                    
                    match check_square(move_to,board=board,self_color=self_color):
                        case square_reaction.STOP:
                            break
                        case square_reaction.CAPTURE:
                            moves.append(this_move)
                            break
                        case square_reaction.CONTINUE:
                            moves.append(this_move)
                            continue


    return moves                                     
def get_bishop_movable_moves(cord,board, self_color: ColorName):
    moves = []
    offsets = [-1,1]
    for off_x in offsets:
        for off_y in offsets:
            for step in range(1,8):
                move_to = list(cord)
                move_to[0] += step * off_x
                move_to[1] += step * off_y
                
                this_move = (cord, move_to)
                match check_square(move_to,board=board,self_color=self_color):
                    case square_reaction.STOP:
                        break
                    case square_reaction.CAPTURE:
                        moves.append(this_move)
                        break
                    case square_reaction.CONTINUE:
                        moves.append(this_move)
                        continue
    return moves
def get_queen_movable_moves(cord,board, self_color: ColorName):
    
    bishop_moves: list[Move] = get_bishop_movable_moves(cord,board,self_color)
    rook_moves: list[Move] = get_rook_movable_moves(cord,board,self_color)
    moves: list[Move] = bishop_moves
    for rook_move in rook_moves:
        moves.append(rook_move)
    return moves 
def get_knight_movable_moves(cord,board,self_color: ColorName): # worth 3 pieces

    moves = []
    trunk_offsets = [-2,2]
    branch_offsets = [-1,1]
    for ax_iter in range(2):
        for trunk_off in trunk_offsets:
            for branch_off in branch_offsets:
                destination = list(cord)
                destination[ax_iter] += trunk_off

                other_ax = int((1-ax_iter)==1)
                destination[other_ax] += branch_off

                move = (cord,destination)
                
                
                if in_bounds(destination):
                    piece_on_destination = board.readSquare(destination)
                    if (piece_on_destination.color_name != self_color):

                        moves.append(move)
    return moves
