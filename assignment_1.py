import sys

import models

import search_algorithims

MAX_COST = 1000
INPUT_FROM_FILE = True

def parse_input():
    start_state = None
    end_state = None
    if INPUT_FROM_FILE:
        with open('input.txt') as f:
            start_state = f.readline().strip()
            end_state = f.readline().strip()
        print(start_state)
    else:
        start_state = input('Start state: ')
        end_state = input('End state: ')
    start_board = models.Board(start_state)
    end_board = models.Board(end_state, board_id=-1)
    return start_board, end_board

def main():
    start_state, goal_state = parse_input()
    h1 = models.create_hueristic_1_func(goal_state)
    h2 = models.create_hueristic_2_func(goal_state)
    search_algorithims.breadth_first_search(start_state,goal_state, h1, MAX_COST)


main()