from models.cartesian_utilities import to_cartesian_coords

def create_hueristic_1_func(goal_board):
    '''
        Factory function to generate the first hueristic function in the homework
    '''
    goal_state = goal_board.state
    def h(board):
        '''
            Return count of tiles out of place
        '''
        state = board.state
        tiles_out_of_place = 0
        for i in range(len(goal_state)):
            if state[i] != goal_state[i]:
                tiles_out_of_place += 1
        return tiles_out_of_place
    return h

def create_hueristic_2_func(goal_board):
    '''
        Factory function to generate second hueristic function from the homework
    '''
    goal_state = goal_board.state
    def h(board):
        curr_state = board.state
        move_sum = 0
        for i in range(len(curr_state)):
            tile_val = curr_state[i]
            tile_coords = to_cartesian_coords(i)

            goal_coords = to_cartesian_coords(goal_state.index(tile_val))
            delta_x = abs(tile_coords[0] - goal_coords[0])
            delta_y = abs(tile_coords[1] - goal_coords[1])
            move_sum += (delta_x + delta_y)
        return move_sum
    return h
