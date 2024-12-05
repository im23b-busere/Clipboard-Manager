import pyperclip
import time
from threading import Thread

clipboard_history = []


def monitor_clipboard():
    current_text = pyperclip.paste()
    clipboard_history.append(current_text)
    print(f'Kopierter Text: {current_text}')





if __name__ == '__main__':
    monitor_clipboard()