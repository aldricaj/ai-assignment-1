
class Board():
    def __init__(self, board_state):
        self.state, self.empty_tile = calculate_state(board_state)

def calculate_state(board_state):
    if type(board_state) == str:
        if board_state[0] != '[' or board_state [-1] != ']':
            raise ValueError('Format invalid. The program expects there to be an opening and a closing square bracket for each state')
        values = [int(v) for v in board_state[1:-1].split(" ") if v != '']

        if len(values) != 20:
            raise ValueError(f'Format Invalid, the board expects exactly 20 tiles. It recieved {len(values)}.\n The values parsed were {values}')
        if values.find(0) < 0:
            raise ValueError('No empty tile found')
        index_empty = values.find(0)
        values[index_empty] = None
        return values, index_empty
    elif type(board_state) == list:
        # Assume it has already been parsed
        index_empty = board_state.find(0)

        if len(board_state) != 20:
            raise ValueError(f'Format Invalid, the board expects exactly 20 tiles. It recieved {len(board_state)}.\n The values parsed were {board_state}')

        if index_empty < 0:
            raise ValueError('No empty tile found')
        return board_state, index_empty
    else:
        raise ValueError('Invalid Type for Board State. It must be either a list or a string')
