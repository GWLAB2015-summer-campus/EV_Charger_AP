import tkinter as tk
from const import SIZE, COLOR, FONT
from component import Label

STATE_DICT = {
    "No Authenticated" : {
        "text" : "No Authenticated",
        "color" : COLOR["GRAY2"]
    },
    "Authenticating" : {
        "text" : "Authenticating",
        "color" : COLOR["YELLOW1"]
    },
    "Authenticated" : {
        "text" : "Authenticated",
        "color" : COLOR["GREEN1"]
    },
    "Authenticated Error" : {
        "text" : "Authenticated Error",
        "color" : COLOR["RED1"]
    },
}

class Authenticate(tk.Frame):
    def __init__(self, parent, w=250 + SIZE["DOT.DIA"], h=SIZE["HEADER.H"]):
        tk.Frame.__init__(self, parent, bg=COLOR["BLACK1"])
        state = STATE_DICT["No Authenticated"]
        self.StateLabel = Label(self, text=state["text"], font=FONT["H5"], anchor="center")
        self.StateLabel.place(x=SIZE["DOT.DIA"], y=0, w=250, h=h)
        self.StateDot = tk.Canvas(self, bg=COLOR["BLACK1"], borderwidth=0, highlightthickness=0)
        self.StateDot.place(x=0, y=0, w=SIZE["DOT.DIA"], h=h)
        hgap = (SIZE["HEADER.H"] - SIZE["DOT.DIA"]) // 2
        self.StateDot.create_oval(0, hgap, SIZE["DOT.DIA"], hgap + SIZE["DOT.DIA"], fill=state["color"] )

    def set_state(self, state):
        if state not in STATE_DICT.keys():
            state = STATE_DICT["Authenticated Error"]
        else:
            state = STATE_DICT[state]
        
        self.StateLabel.config(text=state["text"])
        self.StateDot.delete("all")
        hgap = (SIZE["HEADER.H"] - SIZE["DOT.DIA"]) // 2
        self.StateDot.create_oval(0, hgap, SIZE["DOT.DIA"], hgap + SIZE["DOT.DIA"], fill=state["color"])
        self.update()