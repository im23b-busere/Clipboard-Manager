import pyperclip
import time
from threading import Thread
import keyboard

clipboard_history = []


def monitor_clipboard():
    time.sleep(0.1) # fix copied text delay
    current_text = pyperclip.paste()
    clipboard_history.append(current_text)
    print(f'Kopierte Texte: {clipboard_history}')


keyboard.add_hotkey('ctrl+c', monitor_clipboard)



if __name__ == '__main__':
    keyboard.wait('esc')