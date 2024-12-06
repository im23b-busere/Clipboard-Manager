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
        # Choose latest text
        latest_text = self.clipboard_history[-1]

        # Frame
        frame = ctk.CTkFrame(self.app)
        frame.pack(pady=20, padx=20, fill="x")

        # Add textbox
        history_box = ctk.CTkTextbox(frame, width=180, height=100)
        history_box.pack(side="left", fill="both", expand=True)

        # Insert text into box
        history_box.insert("end", latest_text + "\n")
        history_box.configure(state="disabled")  # Make the text box read-only

        # Add button
        copy_button = ctk.CTkButton(frame, text="Copy", command=lambda t=latest_text: self.copy_to_clipboard(t))
        copy_button.pack(side="left", padx=10)


if __name__ == '__main__':
    clipboard = ClipboardManager()
    keyboard.add_hotkey('ctrl+c', clipboard.monitor_clipboard)
    clipboard.ui_setup()
    keyboard.wait('esc')
