from pynput import mouse
import json


def on_move(x, y):
    print(f'{x} : {y}')
    return {
        'action': 'move',
        'X': x,
        'Y': y
    }

def on_click(x, y, button, pressed):
    ps = "p" if pressed else 'r'
    print()
    return {
        'action': 'cli',
        'X': x,
        'Y': y,
        'button': button,
        'ps': ps
    }

with mouse.Listener(on_move=on_move,
                    on_click=on_click, suppress=True) as listener:
    listener.join()

listener = mouse.Listener(on_move=on_move,
                    on_click=on_click, suppress=True)
listener.start()