import sys

import models.board as models

def parse_input():
    start_state = None
    end_state = None
    if len(sys.argv) > 3:
        # parse input
        start_state = []
        end_state = []
        for s in sys.argv[1:]:
            print(s)
            if s == ' ':
                continue
            if len(start_state) == 0:
                print(str(start_state))
                start_state.append(s)
            else:
                end_state.append(s)
        # Strip square brackets
        start_state[0] = start_state[0][1:]
        start_state[-1] = start_state[-1][:-1]
        end_state[0] = end_state[0][1]
        end_state[-1] = end_state[-1][:-1]

    elif len(sys.argv) == 3:
        start_state = sys.argv[1]
        end_state = sys.argv[2]
    else:
        start_state = input('Start state: ')
        end_state = input('End state: ')
    start_board = models.Board(start_state)
    end_board = models.Board(end_state)
    return start_board, end_board


def main():
    start_state, goal_state = parse_input()
    print('x')
    print(str(start_state))

main()