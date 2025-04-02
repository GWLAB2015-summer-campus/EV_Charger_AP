from tkinter import Tk
from view import LogView, ScanningContainer, Header
from logger import init_logview
from const import SIZE, COLOR
from actions import scan

def test():
    from iso15118.evcc.main import run
    run()

def _init_app():
    global is_fullscreen
    root = Tk()
    root.geometry(f"{SIZE['SCREEN.W']}x{SIZE['SCREEN.H']}")
    root.configure(background=COLOR["BLACK1"])
    root.attributes("-fullscreen", True)
    root.bind("<f>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
    root.bind("<q>", lambda x : root.quit())

    logview = LogView(root)
    init_logview(logview)
    logview.place(
        x=SIZE["DEFUALT_PADDING"] * 2 + SIZE["CONTAINER.W"], 
        y=0, 
        width=SIZE["LOGVIEW.W"], 
        height=SIZE["SCREEN.H"])

    header = Header(root)
    header.place(
        x=SIZE["DEFUALT_PADDING"],
        y=SIZE["DEFUALT_PADDING"],
        width=SIZE["CONTAINER.W"],
        height=SIZE["HEADER.H"]
    )

    scanningContainer = ScanningContainer(root)
    header.ScanButton.bind("<Button-1>", lambda x : scan(root, header, scanningContainer))
    header.ScanButton.disable()
    header.AuthButton.enable()
    header.AuthButton.bind("<Button-1>", lambda x : test())
    scanningContainer.place(
        x=SIZE["DEFUALT_PADDING"],
        y=SIZE["DEFUALT_PADDING"]*2+SIZE["HEADER.H"],
        width=SIZE["CONTAINER.W"],
        height=SIZE["CONTAINER.H"]
        )

    root.mainloop()

if __name__ == '__main__':
    _init_app()