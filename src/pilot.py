#!/usr/bin/env python

from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
