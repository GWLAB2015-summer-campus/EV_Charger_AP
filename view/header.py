import tkinter as tk
from const import SIZE, COLOR
from component import Button, Label
from view.authenticate import Authenticate

class Header(tk.Frame):
    def __init__(self, parent, w=SIZE["CONTAINER.W"], h=SIZE["HEADER.H"]):
        tk.Frame.__init__(self, parent, bg=COLOR["BLACK1"])
        self.ScanButton = Button(self, text="Scan", anchor="center")
        self.ScanButton.place(x=0, y=0, width=200, h=h)
        self.AuthButton = Button(self, text="Authenticate", anchor="center")
        self.AuthButton.disable()
        self.AuthButton.place(x=200 + SIZE["DEFUALT_PADDING"], y=0, width=200, h=h)
        self.Authenticate = Authenticate(self)
        self.Authenticate.place(x=SIZE["CONTAINER.W"] - 250 - SIZE["DOT.DIA"], y=0, width=250 + SIZE["DOT.DIA"], height=SIZE["HEADER.H"])