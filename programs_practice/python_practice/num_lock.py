#!/usr/bin/env python3

from pynput import keyboard
import subprocess

def show_notification(message):
    subprocess.run(['notify-send', message])

def on_press(key):
    if key == keyboard.Key.num_lock:
        state = subprocess.check_output('xset q | grep "Num Lock"', shell=True)
        if b'on' in state:
            show_notification("Num Lock: ON")
        else:
            show_notification("Num Lock: OFF")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
