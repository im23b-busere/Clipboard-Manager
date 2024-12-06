import pyperclip
import time
import keyboard
import customtkinter as ctk


class ClipboardManager:

    def __init__(self):
        self.clipboard_history = []

    def ui_setup(self):
        self.app = ctk.CTk()
        self.app.geometry("600x500")
        self.app.title("Clipboard Manager")

        # add textbox
        self.history_box = ctk.CTkTextbox(self.app, width=580, height=400)
        self.history_box.pack(pady=20)

        self.app.mainloop()

    def monitor_clipboard(self):
        time.sleep(0.1)  # fix copied text delay
        current_text = pyperclip.paste()
        if current_text not in self.clipboard_history:
            self.clipboard_history.append(current_text)
            self.update_history_display()

        else:
            pass

    def get_clipboard_history(self):
        return self.clipboard_history

    def update_history_display(self):
        self.history_box.delete(1.0, ctk.END)
        for text in self.clipboard_history:
            self.history_box.insert("end", text + "\n")


if __name__ == '__main__':
    clipboard = ClipboardManager()
    keyboard.add_hotkey('ctrl+c', clipboard.monitor_clipboard)
    clipboard.ui_setup()
    keyboard.wait('esc')
