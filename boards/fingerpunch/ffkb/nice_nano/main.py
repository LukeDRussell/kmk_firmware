import board

import kb

from kmk.keys import KC
from kmk.modules.combos import Combos, Sequence
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot

combos = Combos()
dyn_seq = DynamicSequences(
    slots=1, # The number of sequence slots to use
    timeout=60000,  # Maximum time to spend in record or config mode before stopping automatically, milliseconds
    key_interval=20,  # Milliseconds between key events while playing
    use_recorded_speed=False,  # Whether to play the sequence at the speed it was typed
)
layers = Layers()
oneshot = OneShot()

keyboard = kb.KMKKeyboard()
keyboard.modules = [combos, dyn_seq, layers, oneshot]
keyboard.debug_enabled = False

SEQ_REC = KC.RECORD_SEQUENCE()
SEQ_STP = KC.STOP_SEQUENCE()
SEQ_PLY = KC.PLAY_SEQUENCE()

combos.combos = [
    Sequence((KC.LEADER, KC.A), KC.LCTL(KC.A)),  # select All
    Sequence((KC.LEADER, KC.T), KC.LCTL(KC.X)),  # cuT
    Sequence((KC.LEADER, KC.C), KC.LCTL(KC.C)),  # Copy
    Sequence((KC.LEADER, KC.P), KC.LCTL(KC.V)),  # Paste
    Sequence((KC.LEADER, KC.U), KC.LCTL(KC.Z)),  # Undo
    Sequence((KC.LEADER, KC.Y), KC.LCTL(KC.Y)),  # redo
    ]

___ = KC.TRNS
xxx = KC.NO

OS_LSFT = KC.OS(KC.LSFT)
TAB_NAV = KC.LT(1, KC.TAB, prefer_hold=True)
ENT_FN = KC.LT(2, KC.ENT, prefer_hold=True)
gaming = KC.DF(4)
no_game = KC.DF(0)
ESC_G2 = KC.LT(5, KC.ESC, prefer_hold=True)

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [
        KC.ESC,     KC.Q,   KC.W,   KC.F,   KC.P,   KC.B,           KC.J,   KC.L,   KC.U,   KC.Y,   KC.SCLN,KC.GUI,
        KC.LCTL,    KC.A,   KC.R,   KC.S,   KC.T,   KC.G,   xxx,    KC.M,   KC.N,   KC.E,   KC.I,   KC.O,   KC.QUOT,
        KC.LALT,    KC.Z,   KC.X,   KC.C,   KC.D,   KC.V,           KC.K,   KC.H,   KC.COMM,KC.DOT, KC.SLSH,KC.BSLS,
                    xxx,       KC.LEADER,   OS_LSFT,KC.BSPC,        TAB_NAV,KC.SPACE,ENT_FN,        xxx,
    ],
    [
        KC.TAB,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,            KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
          ___  , KC.LPRN, KC.LEFT, KC.UP,   KC.RGHT,KC.RPRN,   ___  , KC.GRV,  KC.PLUS, KC.EQL,    xxx  ,   xxx  ,   xxx  ,
          ___  , KC.LBRC, KC.LCBR, KC.DOWN, KC.RCBR, KC.RBRC,          KC.TILD, KC.MINS, KC.UNDS,   xxx  ,   xxx  ,   xxx  ,
                      ___  ,            ___  ,   ___  , KC.DEL,             ___  ,   ___  ,   ___  ,   ___  ,
    ],
    [
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,            KC.F6,   KC.F7,   KC.F8,   KC.F9,    KC.F10,  KC.F11,
          ___  , SEQ_REC, SEQ_PLY,   ___  ,   ___  ,   ___  ,   ___  ,   ___  ,   ___  ,   ___  ,   ___  ,    ___  ,   ___  ,
          ___  , SEQ_STP,   ___  ,   ___  ,   ___  ,   ___  ,            ___  ,   ___  ,   ___  ,   ___  ,    ___  ,   ___  ,
                  ___  ,            ___   ,   ___  ,   ___  ,            gaming, ___  ,   ___  ,             ___  , 
    ],
    [
        KC.TAB, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,          xxx,    xxx,    xxx,    xxx,    xxx,    xxx,
        KC.LCTL,KC.F1,  KC.LEFT,KC.UP,  KC.RGHT,KC.F2,  xxx,    xxx,    xxx,    xxx,    xxx,    xxx,    xxx,
        KC.LALT,KC.F3,  KC.F4,  KC.DOWN,KC.F5,  KC.F6,          xxx,    xxx,    xxx,    xxx,    xxx,    xxx,
                xxx,            ESC_G2, KC.SPC, KC.LSFT,                no_game,xxx,    ENT_FN, xxx,
    ],
    [
        ___,    KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,          ___,    ___,    ___,    ___,    ___,    ___,
        ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,    ___,
        ___,    ___,    ___,    ___,    ___,    ___,            ___,    ___,    ___,    ___,    ___,    ___,
                ___,            ___,    ___,    ___,            ___,    ___,    ___,      ___
    ],
]
# fmt: on

if __name__ == '__main__':
    keyboard.go()
