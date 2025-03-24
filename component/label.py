import tkinter as tk
from const import SIZE, COLOR, FONT

class Label(tk.Label):
    def __init__(self, *args, **kwargs):
        defaultKwargs = {
            "bg" : COLOR["BLACK1"],
            "fg" : COLOR["WHITE1"],
        }
        kwargs = defaultKwargs | kwargs
        tk.Label.__init__(self, *args, **kwargs)