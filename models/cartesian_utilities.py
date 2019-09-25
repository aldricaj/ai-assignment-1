ROWS = 5
COLS = 4
SIZE = ROWS * COLS

def to_cartesian_coords(index):
    return index % COLS, index // COLS

def from_cartesian_coords(coords):
    x,y = coords
    return y * COLS + x