import random
import string
from models.cartesian_utilities import *
from config import USE_STR_IDS

class Board():
    def __init__(self, board_state, board_id='root', parent_id=None):
        self.state, empty_tile_index = _calculate_state(board_state)
        self.empty_tile = to_cartesian_coords(empty_tile_index)
        self.parent_id = parent_id
        self.board_id = board_id
        
    
    def get_hash(self):
        # very very lazy hash, shouldn't be repeated, and shouldn't take long to compare
        return str(self.state)


    def calc_num_moves(self, hueristic):
        '''
            Takes a hueristic, which is a function which takes a state

            Returns the result of the hueristic
        '''
        return hueristic(self.state)
    
    def get_possible_moves(self):
        '''
            Returns all legal moves for the board as a tuple with the following format:

            (tile_moved, new_state, (move_x, move_y))

            Where 
                tile_moved is the number assigned to the move coordinates

                New_state is the resulting Board

                (move_x, move_y) are the cartesian coordinates of the tile moved in the current Board
        '''
        # Move left, right, down, up respectively
        tile_x, tile_y = self.empty_tile
        moves = [
            (tile_x + 1, tile_y),
            (tile_x - 1, tile_y),
            (tile_x, tile_y + 1),
            (tile_x, tile_y - 1)
        ]

        # filter out invalid moves
        valid_moves = [(x, y) for x,y in moves if x >= 0 and x < ROWS and y >= 0 and y < COLS]

        final_result = []
        # Represent tile move as (tile_moved, new_state, move)
        for move in valid_moves:
            tile_moved = self.state[from_cartesian_coords(move)]
            new_state = self.state.copy()

            # swap the states
            new_state[from_cartesian_coords(self.empty_tile)] = tile_moved
            new_state[from_cartesian_coords(move)] = None

            # Create the board
            new_board = Board(new_state, _generate_board_id(self.board_id), self.board_id)

            final_result.append((tile_moved, new_board, move))
        return final_result

    def __str__(self):
        result = f'Board Id:\t{self.board_id}\n'
        for i in range(len(self.state)):
            # Print the board as a grid
            if (i % COLS) == 0:
                if i > 0:
                    result += '\n'
                result += str(self.state[i])
            else:
                result += '\t'
                result += str(self.state[i])
        return result

def _generate_board_id(parent_id):
    # a relatively unique identifier, would not work for large n, but should work here
    if USE_STR_IDS:
        choices = string.ascii_lowercase +'0123456789'
        return parent_id + '-' + random.choice(choices)
    return parent_id * 100 + random.randint(0,99)

def _calculate_state(board_state):
    '''
        Helper function that returns the state of the board

        Can be passed the state as either a list or as a string in format "[a b c d ... z]" where a-z are numbers

        The board size must be less than SIZE
    '''
    if type(board_state) == str:
        if board_state[0] != '[' or board_state [-1] != ']':
            raise ValueError('Format invalid. The program expects there to be an opening and a closing square bracket for each state')
        values = [int(v) for v in board_state[1:-1].split(" ") if v != '']

        if len(values) != SIZE:
            raise ValueError(f'Format Invalid, the board expects exactly {SIZE} tiles. It recieved {len(values)}.\n The values parsed were {values}')
        if values.index(0) < 0:
            raise ValueError('No empty tile found')
        index_empty = values.index(0)
        values[index_empty] = None
        return values, index_empty

    elif type(board_state) == list:
        # Assume it has already been parsed
        index_empty = board_state.index(None)

        if len(board_state) != 20:
            raise ValueError(f'Format Invalid, the board expects exactly {SIZE} tiles. It recieved {len(board_state)}.\n The values parsed were {board_state}')

        if index_empty < 0:
            raise ValueError('No empty tile found')
        return board_state, index_empty
    else:
        raise ValueError('Invalid Type for Board State. It must be either a list or a string')
