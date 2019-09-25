from search_algorithims.utilities import *

def breadth_first_search(start_state, end_state, hueristic_func, max_iters):
    i = 0
    cost = 0
    open_list = [(0, start_state)] # used as queue
    n_added_to_open = 1
    closed_list = {} # used as hash table
    n_added_to_closed = 0
    expanded_node = start_state
    while expanded_node.get_hash() != end_state.get_hash():
        i+=1
        if i >= max_iters:
            print('Maximum number of iterations reached')
            break

        # Expand Node
        cost_so_far,expanded_node = open_list.pop()
        h_val = hueristic_func(expanded_node)

        # Check to ensure that we do not hit a duplicate state
        # Theoritically possible, but highly unlikely
        if expanded_node.get_hash() in closed_list.keys():
            continue
        # Check if we are done
        if h_val == 0:
            print('=' * 40)
            print('Goal Reached')
            print('=' * 40)
            cost = cost_so_far
        else:
            # Find Children to continue search
            next_moves = expanded_node.get_possible_moves()
            for tile_val, board, _ in next_moves:
                # Skip over states already visited
                if board.get_hash() in closed_list.keys():
                    continue
                open_list.insert(0, (cost_so_far + (2 if tile_val > 9 else 1), board))
                n_added_to_open += 1
            closed_list[start_state.get_hash()] = start_state
            n_added_to_closed += 1
        
        display_state(expanded_node.board_id, expanded_node.parent_id, cost_so_far, h_val, None, expanded_node)
    display_final_stats('Breadth-First', i, n_added_to_open, n_added_to_closed, cost)
