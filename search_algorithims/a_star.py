from search_algorithims.utilities import display_final_stats, display_state

def a_star_search(start_state, end_state, hueristic_func, max_iters, h_func_name="h"):
    i = 0
    cost = 0
    open_list = PriorityQueue(starting_values=[(0, start_state)])
    n_added_to_open = 1
    closed_list = {} # used as hash table
    n_added_to_closed = 0
    expanded_node = start_state

    while hueristic_func(expanded_node) > 0:
        i+=1
        if i >= max_iters:
            print('Maximum number of iterations reached')
            break
        # Expand Node
        _, expanded_node = open_list.pop()
        cost_so_far = expanded_node.board_cost
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
                new_h_val = hueristic_func(board)
                board.board_cost = cost_so_far + (2 if tile_val > 9 else 1)
                open_list.insert(board.board_cost + new_h_val, board)
                n_added_to_open += 1
            
            closed_list[start_state.get_hash()] = start_state
            n_added_to_closed += 1
        display_state(expanded_node.board_id, expanded_node.parent_id, cost_so_far, h_val, cost_so_far, expanded_node)
    display_final_stats(f'A* using {h_func_name}', i, n_added_to_open, n_added_to_closed, cost)

class PriorityQueue():
    def __init__(self, starting_values=None):
        '''
            Instantiates the priority queue

            Starting_values should be a list of tuples of (priority, item)
        '''
        self.queue = {} # use dictionary. Key is priority, value is queue

        if starting_values:
            for priority,val in starting_values:
                self.insert(priority, val)

    def insert(self, priority, value):
        if priority in self.queue.keys():
            self.queue[priority].insert(0, value)
        else:
            self.queue[priority] = [value] # instantiate the value it as a list
    
    def pop(self):
        next_key = min(self.queue.keys())
        value = self.queue[next_key].pop()

        # del key if no more values are in it
        if len(self.queue[next_key]) == 0:
            del self.queue[next_key]
        
        return next_key, value