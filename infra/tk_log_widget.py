import tkinter as tk
import tkinter.scrolledtext
from tkinter import ttk


def TKLogWidget(root: tk.Tk):
    log_window_frame = ttk.LabelFrame(
        root, borderwidth=1, relief="solid", text="Log Messages"
    )
    log_window_frame.grid(row=4, column=6)

    log_window = tk.scrolledtext.ScrolledText(log_window_frame, state="disabled")
    log_window.configure(font="TkFixedFont")

    return log_window
