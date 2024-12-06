import time
import customtkinter as ctk
import keyboard
import pyperclip


class ClipboardManager:

    def __init__(self):
        self.app = None
        self.history_box = None
        self.clipboard_history = []

    def ui_setup(self):
        self.app = ctk.CTk()
        self.app.geometry("600x500")
        self.app.title("Clipboard Manager")

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

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

    def update_history_display(self):

        for text in self.clipboard_history:
            # add textbox
            self.history_box = ctk.CTkTextbox(self.app, width=180, height=100)
            self.history_box.pack(pady=20)

            # insert text into box
            self.history_box.insert("end", text + "\n")

            # add button

            copy_button = ctk.CTkButton(self.app, text="Copy", command=lambda t=text: self.copy_to_clipboard(t))
            copy_button.pack(pady=10)


if __name__ == '__main__':
    clipboard = ClipboardManager()
    keyboard.add_hotkey('ctrl+c', clipboard.monitor_clipboard)
    clipboard.ui_setup()
    keyboard.wait('esc')
