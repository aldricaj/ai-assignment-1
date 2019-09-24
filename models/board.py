ROWS = 5
COLS = 4
SIZE = ROWS * COLS
class Board():
    def __init__(self, board_state):
        self.state, self.empty_tile = calculate_state(board_state)
    
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
        # Move left, right, down, up respectively
        moves = [self.empty_tile - 1, self.empty_tile + 1, 
                 self.empty_tile + ROWS, self.empty_tile - ROWS]

    def __str__(self):
        result = ''

        for i in range(len(self.state)):
            
            if (i % COLS) == 0:
                result += '\n'
                result += str(self.state[i])
            else:
                result += '\t'
                result += str(self.state[i])
                
        return result

def calculate_state(board_state):
    print(str(board_state))
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
        index_empty = board_state.index(0)

        if len(board_state) != 20:
            raise ValueError(f'Format Invalid, the board expects exactly {SIZE} tiles. It recieved {len(board_state)}.\n The values parsed were {board_state}')

        if index_empty < 0:
            raise ValueError('No empty tile found')
        return board_state, index_empty
    else:
        raise ValueError('Invalid Type for Board State. It must be either a list or a string')
