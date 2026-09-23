import tkinter
import logging


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

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)
