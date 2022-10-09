import kb

from kmk.keys import KC
from kmk.modules.combos import Combos, Sequence
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.oneshot import OneShot
from kmk.extensions.media_keys import MediaKeys

combos = Combos()
dyn_seq = DynamicSequences(
    slots=1,
    timeout=60000,
    key_interval=20,
    use_recorded_speed=False,
)
layers = Layers()
oneshot = OneShot()

keyboard = kb.Keyboard()
keyboard.modules = [combos, dyn_seq, layers, oneshot]

keyboard.debug_enabled = True

# Convenience variables for the Keymap
_______ = KC.TRNS
xxxxxxx = KC.NO

L1_TAB = KC.LT(1, KC.TAB, prefer_hold=True)
L2_ENT = KC.LT(2, KC.ENT, prefer_hold=True)

OS_LSFT = KC.OS(KC.LSFT)

SEQ_REC = KC.RECORD_SEQUENCE()
SEQ_STP = KC.STOP_SEQUENCE()
SEQ_PLY = KC.PLAY_SEQUENCE()

combos.combos = [
    Sequence((KC.LDR, KC.A), KC.LCTL(KC.A)),  # select All
    Sequence((KC.LDR, KC.T), KC.LCTL(KC.X)),  # cuT
    Sequence((KC.LDR, KC.C), KC.LCTL(KC.C)),  # Copy
    Sequence((KC.LDR, KC.P), KC.LCTL(KC.V)),  # Paste
    Sequence((KC.LDR, KC.U), KC.LCTL(KC.Z)),  # Undo
    Sequence((KC.LDR, KC.Y), KC.LCTL(KC.Y)),  # redo
    ]

# flake8: noqa
# fmt: off
keyboard.keymap = [
    [  # 0: Colemak-DH letters
        KC.ESC,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,             KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.LEADER,
        KC.LCTL, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,             KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,
        KC.LALT, KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,             KC.K,    KC.H,    KC.COMM, KC.DOT,  KC.SLSH, KC.BSLS,
                 KC.HOME,          KC.LGUI, OS_LSFT, KC.BSPC,          L1_TAB,  KC.SPACE,L2_ENT,           KC.END,
    ],
    [  # 1: Nav & Numbers
        KC.TAB,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,            KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        _______, KC.LPRN, KC.LEFT, KC.UP,   KC.RIGHT,KC.RPRN,          KC.GRV,  KC.PLUS, KC.EQL,  xxxxxxx, xxxxxxx, xxxxxxx,
        _______, KC.LBRC, KC.LCBR, KC.DOWN, KC.RCBR, KC.RBRC,          KC.TILD, KC.MINS, KC.UNDS, xxxxxxx, xxxxxxx, xxxxxxx,
                 _______,          _______, _______, KC.DEL,           _______, _______, _______,          _______,
    ],
    [  # 2: F-row & Board Functions
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,            KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        _______, SEQ_REC, SEQ_PLY, _______, _______, _______,          _______, _______, _______, _______, _______, _______,
        _______, SEQ_STP, _______, _______, _______, _______,          _______, _______, _______, _______, _______, _______,
                 _______,          _______, _______, _______,          _______, _______, _______,          _______,
    ],
]

encoder = EncoderHandler()
encoder.pins = kb.encoder_pins
encoder.map = [
    [[KC.UP, KC.DOWN]],  # L0
    [[xxxxxxx, xxxxxxx]],  # L1
    [[xxxxxxx, xxxxxxx]],  # L2
]
keyboard.modules.append(encoder)

if __name__ == '__main__':
    print()
    print("Starting KMK...")
    print()
    keyboard.go()
