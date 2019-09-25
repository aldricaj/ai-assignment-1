from config import SHOW_BOARD

def display_final_stats(search_type, iters, nodes_added_to_open, nodes_added_to_close, cost):
    print(f'{search_type} Stats:')
    print(f'Iterations:\t{iters}\n# of Nodes Added to Open List:\t{nodes_added_to_open}')
    print(f'# of Nodes Added to Closed List:\t{nodes_added_to_close}\nTotal Cost:\t{cost}')

def display_state(board_id, parent_id, cost, h_val, priority=None, board=None):
    f_n = h_val + cost
    print(f'<id={board_id}\t\tparent={parent_id}\t\tg(n)=\t{cost}\th(n)={h_val}\tf(n)={f_n}\tPriority={priority}>')
    if SHOW_BOARD:
        print(str(board))
