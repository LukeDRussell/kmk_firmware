# Getting Started

> KMK is a feature-rich and beginner-friendly firmware for computer keyboards written and configured in CircuitPython.

Essentially it's a layer that sits on top of [CircuitPython](https://circuitpython.org/), which adds features enabling advanced keyboard customization. KMK _should_ work with most [boards that support CircuitPython](https://circuitpython.org/downloads), but we recommended using boards from the list of [Officially Supported Boards](Officially_Supported_Boards.md) for beginners. 

Please don't be afraid that this is all too technical:
> CircuitPython is a programming language designed to simplify experimenting and learning to program on low-cost microcontroller boards. It makes getting started easier than ever with no upfront desktop downloads needed. Once you get your board set up, open any text editor, and get started editing code. It's that simple.

Like CircuitPython, KMK Firmware is intended to be easy to learn for beginners without compromising on powerful features and ease of use. In fact those are the biggest reason to use KMK over the alternatives ([QMK](https://qmk.fm/), [ZMK](https://zmk.dev/), [various Rust firmwares](https://github.com/dfrankland/awesome-rust-keyboard-firmware)).

<br>

## Summary of Steps

1. [Install a code editor](#1-install-a-code-editor)
2. [Install CircuitPython](#2-install-circuitpython).
3. [Install KMK](#3_install-kmk)
4. [Test basic functions](#4-test-basic-functions)
5. Configure and Customise!

## 1. Install a Code Editor

Install [Mu](https://codewith.mu/) _a simple Python editor for beginner programmers_, on your computer.

KMK-powerred keyboards are configured through plain-text `.py` files - we have no GUI at this time. You could use `notepad.exe` or `textedit.app` to write and edit these files, but it's much easier to use a purpose-built code editing application as they help you write better code, faster and with less frustration.

We echo CircuitPython's recommendation of using the [Mu](https://codewith.mu/) editor to work with KMK. Even if you have experience coding and a preferred editor, we recommend starting with Mu as it knows the CircuitPython libraries (so linters won't warn `Import "board" could not be resolved`), and it has an in-built Serial connection client so you access the CircuitPython REPL for troubleshooting and learning the KMK functionality.

## 2. Install CircuitPython
Install the latest CircuitPython firmware on your board. CircuitPython has excellent documentation - as you'd hope from a _beginner friendly_ version of Python. We recommend following the [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython) guide to get up and running. The guide will give you enough knowledge of CircuitPython to be able to effectively work with KMK.

## 3. Install KMK
1. [Download KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip) and unzip to any location on your computer.
2. Check that after installing CircuitPython, when connected via a USB cable your board should show up as a removable storage device (aka "thum drive"), probably labelles as `CIRUITPY`.
3. Copy the `kmk` folder and `boot.py` file from the unizipped KMK download to the root of `CIRCUITPY`.

## 4. Test basic functions

1. Open the Mu Editor
2. From the "Select Mode" popup window choose `CircuitPython`. _The first time Mu will need time to download a bunch of necessary content to work with CircuitPython._
3. Click `New` to create a new file. Copy the code below into the new file, adapt the pins to your specific board (as per table). 

board     | row_pins | col_pins
----------|----------|---------
Keeboar   | D6       | D5
----------|----------|---------
Nice!Nano | P0_08    | P0_06
----------|----------|---------
Pro-Micro | D0       | D1
----------|----------|---------
Elite-C   | D0       | D1

```py
# Import all the necessary libraries and modules
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

# Create an instance of KMKKeyboard to hold our configuration:
keyboard = KMKKeyboard()

# Define a simple matrix to test basic functionality
keyboard.row_pins = (board.XXX,)    # Replace XXX with the correct pin for your board from the table.
keyboard.col_pins = (board.YYY,)    # Replace YYY with the correct pin for your board from the table.
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    print("")
    print("Starting up...")
    print("")

    keyboard.go()
```

4. In Mu click `Serial` to bring up the output of your board. With CircuitPython, everytime you change the contents of the files on your board, it will reload the board. This makes it super easy to make and test changes. 
5. `Save` your new file to your board as `D:\CIRCUITPY\boot.py` (or MacOS, Linux, *BSD equivalent). Watch the Serial pane for the output from your board. It should look something like below...
```

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:

Starting up...

```
It might look like nothing is happening at this stage, but it just means that KMK is doing it's thing...

6. With a jumper wire / paperclip / screwdriver / etc, short (aka connect) the pins you selected for col_pin and row_pin together. If everything is working, you should see 

![feather and keeboar example pins](pins56.jpg)

6. If it prints the letter "a" (or a "Q" or ... depending on your keyboard layout), you're done!

<br>


## Now that you're up and running, you may want to go further...
> This is your last chance. After this, there is no turning back. You take the blue pill—the story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill—you stay in Wonderland, and I show you how deep the rabbit hole goes. Remember: all I'm offering is the truth. Nothing more.

### You're extremely lucky and you have a fully supported keyboard
If your keyboard and microcontroller are officially supported, simply visit the page for your files, and dropping them on the root of the "flash drive". Those pages can be found [here](https://github.com/KMKfw/kmk_firmware/tree/master/boards). You will need the `kb.py` and `main.py`. More advanced instructions can be found [here](config_and_keymap.md).

### You've got another, maybe DIY, board and want to customise KMK for it  
First, be sure to understand how your device work, and particularly its specific matrix configuration. You can have a look [here](http://pcbheaven.com/wikipages/How_Key_Matrices_Works/) or read the [guide](https://docs.qmk.fm/#/hand_wire) provided by the QMK team for handwired keyboards
<br>Once you've got the gist of it:
- You can have a look [here](config_and_keymap.md) and [here](keys.md) to start customizing your code.py / main.py file
- There's a [reference](keycodes.md) of the available keycodes
- [International](international.md) extension adds keys for non US layouts and [Media Keys](media_keys.md) adds keys for ... media

And to go even further:
- [Sequences](sequences.md) are used for sending multiple keystrokes in a single action
- [Layers](layers.md) can transform the whole way your keyboard is behaving with a single touch
- [ModTap](modtap.md) allow you to customize the way a key behaves wether it is tapped or hold, and [TapDance](tapdance.md) depending on the number of times it is pressed

Want to have fun features such as RGB, split keyboards and more? Check out what builtin [modules](modules.md) and [extensions](extensions.md) can do!
You can also get ideas from the various [user examples](https://github.com/KMKfw/kmk_firmware/tree/master/user_keymaps) that we provide and dig into our [documentation](README.md).

<br>

## Additional help and support
> Roads? Where we're going we don't need roads.

In case you need it, debugging help can be found [here](debugging.md)

If you need support with KMK or just want to say hi, find us in 
[#kmkfw:klar.sh on Matrix](https://matrix.to/#/#kmkfw:klar.sh).  This channel is 
bridged to Discord [here](https://discordapp.com/widget?id=493256121075761173&theme=dark) 
for convenience. If you ask for help on chat or open a bug report, if possible 
please give us your commit SHA, found by running 
`from kmk.consts import KMK_RELEASE;  print(KMK_RELEASE)` in the REPL on your 
controller.
 





