from tkinter import Tk

from my_constants import version


def create_root_window() -> Tk:
    root = Tk()
    root.title("Pokemon Forme Insertion V." + version)
    root.state("zoomed")
    return root
