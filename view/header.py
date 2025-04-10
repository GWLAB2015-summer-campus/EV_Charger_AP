import tkinter as tk
from const import SIZE, COLOR
from component import Button

class Header(tk.Frame):
    def __init__(self, parent, w=SIZE["CONTAINER.W"], h=SIZE["HEADER.H"]):
        tk.Frame.__init__(self, parent, bg=COLOR["BLACK1"])
        self.ScanButton = Button(self, text="Scan", anchor="center")
        btn_w = (SIZE["CONTAINER.W"] // 2) - (SIZE["DEFUALT_PADDING"] // 2)
        auth_w = btn_w * 1.5
        self.ScanButton.place(x=0, y=0, width=int(btn_w*0.8), h=h)
        self.AuthButton = Button(self, text="Authenticate", anchor="center")
        self.AuthButton.disable()
        self.AuthButton.place(x=int(btn_w*0.8) + SIZE["DEFUALT_PADDING"], y=0, width=int(btn_w*1.2), h=h)