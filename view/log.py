import tkinter as tk
from component import Label
from const import SIZE, COLOR, FONT
from view.authenticate import Authenticate

class LogView(tk.Frame):
    def __init__(self, parent, w=SIZE["LOGVIEW.W"], h=SIZE["CONTAINER.H"]):
        tk.Frame.__init__(self, parent, bg=COLOR["BLACK1"])

        auth_h = int(SIZE["HEADER.H"] * 0.6)
        self.Authenticate = Authenticate(self, w=w)
        self.Authenticate.place(x=0, y=0, width=w, height=auth_h)

        self.Title = Label(self, text="Debug Log", anchor="sw", font=FONT["H4"])
        title_h = SIZE["HEADER.H"] - auth_h - int(SIZE["DEFUALT_PADDING"] // 2)
        self.Title.place(x=0, y=auth_h + SIZE["DEFUALT_PADDING"], width=w, height=title_h)

        self.LogFrame = tk.Frame(self, bg=COLOR["BLACK2"])
        self.LogFrame.place(
            x=0, 
            y=SIZE["HEADER.H"] + SIZE["DEFUALT_PADDING"],
            width=w,
            height=SIZE["CONTAINER.H"])

        self.LogBox = tk.Text(self.LogFrame, 
            bg=COLOR["BLACK2"], 
            fg=COLOR["WHITE1"], 
            borderwidth=0, 
            highlightthickness=0,
            state=tk.DISABLED)

        self.LogBox.place(x=10, 
            y=10,
            width=w-20, 
            height=SIZE["SCREEN.H"] - title_h - SIZE["DEFUALT_PADDING"]*2 - 20)

        self.loglen = 0

    def logging(self, value):
        print(value)
        vstr = str(value)
        for line in vstr.split("\n"):
            self.loglen += 1
            self.LogBox.config(state=tk.NORMAL)
            self.LogBox.insert(self.loglen * 1.0, str(line) + "\n")
            self.LogBox.config(state=tk.DISABLED)
        self.update()
        
