import tkinter as tk
from const import COLOR

class Container(tk.Frame):
    def __init__(self, *args, **kwargs):

        defaultKwargs = {
            "bg" : COLOR["BLACK2"]
        }

        kwargs = defaultKwargs | kwargs

        tk.Frame.__init__(self, *args, **kwargs)
