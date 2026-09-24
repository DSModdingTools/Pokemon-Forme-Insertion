import logging  # ruff: ignore[N999]
import tkinter


class TKinterTextHandler(logging.Handler):
    def __init__(self, text):
        logging.Handler.__init__(self)
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state="normal")
            self.text.insert(tkinter.END, msg + "\n")
            self.text.configure(state="disabled")
            self.text.yview(tkinter.END)

        self.text.after(0, append)
