import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

def ic(row, col):
    return (8 * row) + col

class Keyboard(KMKKeyboard):

    col_pins = (
        board.P1_06,  # row[0]
        board.P1_04,  # row[1]
        board.P0_11,  # row[2]
        board.P1_00,  # row[3]
        board.P0_24,  # row[4]
        board.P0_22,  # row[5]
        board.P0_10,  # row[6]
        board.P1_11,  # row[7]
    )
    row_pins = (
        board.P0_08,  # col[0]
        board.P0_31,  # col[1]
        board.P0_29,  # col[2]
        board.P0_02,  # col[3]
        board.P1_15,  # col[4]
        board.P1_13,  # col[5]
    )
    diode_orientation = DiodeOrientation.COLUMNS
    bat_volt = board.P0_04
    rgb_num_pixels = 42
    i2c = board.I2C

# flake8: noqa
# fmt: off
    coord_mapping = [
        ic(0, 0), ic(0, 1), ic(0, 2), ic(0, 3), ic(0, 4), ic(0, 5),             ic(0, 6), ic(0, 7), ic(4, 3), ic(3, 4), ic(4, 5), ic(3, 7),
        ic(1, 0), ic(1, 1), ic(1, 2), ic(1, 3), ic(1, 4), ic(1, 5),             ic(1, 6), ic(1, 7), ic(3, 2), ic(4, 4), ic(3, 5), ic(4, 7),
        ic(2, 0), ic(2, 1), ic(2, 2), ic(2, 3), ic(2, 4), ic(2, 5),             ic(2, 6), ic(2, 7), ic(4, 2), ic(3, 3), ic(3, 6), ic(4, 6),
                  ic(5, 1),           ic(5, 3), ic(5, 4), ic(5, 5),             ic(5, 6), ic(5, 7), ic(5, 2),           ic(5, 0)
    ]
# fmt: on

encoder_pins = [
    [board.P0_20, board.P0_17],
]
