import tkinter as tk
from component import Container, Label
from const import SIZE, FONT, COLOR

class ScanningContainer(Container):
    def __init__(self, parent):
        Container.__init__(self, parent)
        self.Text = Label(self, 
        text="", 
        anchor="center", 
        bg=COLOR["BLACK2"],
        font=FONT["H1"])
        
        self.SubText = Label(self, 
        text="", 
        anchor="center", 
        bg=COLOR["BLACK2"],
        fg=COLOR["RED1"],
        font=FONT["H4"])

    def is_scanning(self):
        self.Text.config(text="Scanning....", fg=COLOR["WHITE1"], anchor="center")
        self.SubText.place_forget()
        self.Text.place(x=0, y=0, w=SIZE["CONTAINER.W"], h=SIZE["CONTAINER.H"])
        self.update()

    def end_scanning(self):
        self.Text.place_forget()
        self.update()

    def is_error(self, error_title, error_msg):
        self.Text.config(text=error_title, fg=COLOR["RED1"], anchor="s")
        self.SubText.config(text=error_msg, anchor="n")
        self.Text.place(x=0, y=0, w=SIZE["CONTAINER.W"], h=SIZE["CONTAINER.H"]/2)
        self.SubText.place(x=0, y=SIZE["CONTAINER.H"]/2, w=SIZE["CONTAINER.W"], h=SIZE["CONTAINER.H"]/2)
        self.update()
