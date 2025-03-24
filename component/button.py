import tkinter as tk
from const import SIZE, COLOR, FONT

class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        defaultKwargs = {
            "bg" : COLOR["BLACK2"],
            "fg" : COLOR["WHITE1"],
            "font" : FONT["H3"],
            "borderwidth" : 0,
            "highlightthickness" : 0
        }
        kwargs = defaultKwargs | kwargs
        tk.Button.__init__(self, *args, **kwargs)

    def enable(self):
        self.config(state=tk.NORMAL)
        self.config(fg=COLOR["WHITE1"])
    
    def disable(self):
        self.config(state=tk.DISABLED)
        self.config(fg=COLOR["GRAY1"])