import time
import customtkinter as ctk
import keyboard
import pyperclip


class ClipboardManager:

    def __init__(self):
        self.app = None
        self.frame = None
        self.clipboard_history = []

    def ui_setup(self):
        self.app = ctk.CTk()
        self.app.geometry("600x500")
        self.app.title("Clipboard Manager by Erik")

        self.label = ctk.CTkLabel(self.app, text="Waiting for copied text...")
        self.label.pack(pady=10)

        clear_button = ctk.CTkButton(self.app, text="Clear All", command=self.clear_history)
        clear_button.pack(pady=10)

        self.frame = ctk.CTkScrollableFrame(self.app)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.app.mainloop()

    def monitor_clipboard(self):
        time.sleep(0.1)  # fix copied text delay
        current_text = pyperclip.paste()
        if current_text not in self.clipboard_history:
            self.clipboard_history.append(current_text)
            self.update_history_display()

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

    def update_history_display(self):

        if self.label.winfo_manager():
            self.label.pack_forget()

        # Choose latest text
        latest_text = self.clipboard_history[-1]

        frame = ctk.CTkFrame(self.frame)
        frame.pack(pady=10, padx=10, fill="x")

        history_box = ctk.CTkTextbox(frame, width=180, height=100)
        history_box.pack(side="left", fill="both", expand=True)

        # Insert text into box
        history_box.insert("end", latest_text + "\n")
        history_box.configure(state="disabled")  # Make the text box read-only

        copy_button = ctk.CTkButton(frame, text="Copy")

        copy_button.configure(command=lambda t=latest_text, b=copy_button: self.button_onclick(t, b))
        copy_button.pack(side="left", padx=10)

        self.scroll_to_bottom()


    def button_onclick(self, text, button):
        self.copy_to_clipboard(text)
        button.configure(text="Copied ✔ ", text_color="lightgreen")
        self.app.after(1000, lambda: button.configure(text="Copy", text_color="white"))


    # scroll to bottom inspired by: https://stackoverflow.com/questions/77366191/customtkinters-ctkscrollableframe-autoscroll-to-bottom-python
    def scroll_to_bottom(self):
        self.app.after(1, self.frame._parent_canvas.yview_moveto, 1)

    def clear_history(self):
        self.clipboard_history = []
        for widget in self.frame.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    clipboard = ClipboardManager()
    keyboard.add_hotkey('ctrl+c', clipboard.monitor_clipboard)
    clipboard.ui_setup()
    keyboard.wait('esc')
