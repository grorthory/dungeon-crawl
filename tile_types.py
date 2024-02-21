from typing import Tuple
import numpy as np #type: ignore

#Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"), #unicode codepoint
        ("bg", "3B"), #3B means 3 unsigned bytes, for RGB colors
    ]
)

#Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", bool), #True if can be walked over
        ("transparent", bool), #True if tile doesn't block FOV
        ("dark", graphic_dt), #Graphics for when tile isn't in FOV
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function to define tile types. Takes tile_dt parameters, creates and returns Numpy array of just element"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)