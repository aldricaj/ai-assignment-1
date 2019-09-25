from config import ROWS,COLS, SIZE

def to_cartesian_coords(index):
    return index % COLS, index // COLS

def from_cartesian_coords(coords):
    x,y = coords
    return y * COLS + x