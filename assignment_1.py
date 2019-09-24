import sys

def parse_input():
    start_state = None
    end_state = None
    if len(sys.argv > 3):
        # parse input
        start_state = ''
        end_state = ''
        for s in sys.argv[1:]:
            if start_state[-1] != ']':
                start_state.push


def main():
    start_state, goal_state = parse_input()