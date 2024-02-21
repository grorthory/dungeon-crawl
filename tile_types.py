from typing import Tuple
import numpy as np #type: ignore

#Tile graphics structured type compatible with Console.rgb
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
        ("light", graphic_dt), #Graphics for when tile is in FOV
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function to define tile types. Takes tile_dt parameters, creates and returns Numpy array of just element"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

#SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (78, 28, 24)), dtype=graphic_dt) #currently draws black tile

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (178, 89, 54)),
    light=(ord(" "), (255, 255, 255), (204, 130, 89)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (155, 56, 47)),
    light=(ord(" "), (255, 255, 255), (192, 97, 86)),
)