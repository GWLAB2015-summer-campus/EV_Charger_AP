from logger import logging
import asyncio
from view import ConnectedContainer
from const import SIZE
from actions.auth_action import authenticate
from models import SECC_parser, AP
from wifi_scanner import scanning_and_connect

async def async_scan(root, header, scanningView):
    header.ScanButton.disable()
    scanningView.is_scanning()
    
    bss, ssid, signal, freq, vse = scanning_and_connect()

    if vse is None:
        scanningView.is_error("Connect Error", "AP Not Found")
        header.ScanButton.enable()
    else:
        secc = SECC_parser(vse)
        ap = AP(
            bss=bss,
            ssid=ssid,
            frequency=freq,
            signal=signal
        )

        logging(secc)

        connectedContainer = ConnectedContainer(root, secc, ap)
        connectedContainer.place(
            x=SIZE["DEFUALT_PADDING"],
            y=SIZE["DEFUALT_PADDING"]*2+SIZE["HEADER.H"],
            width=SIZE["CONTAINER.W"],
            height=SIZE["CONTAINER.H"]
        )
        scanningView.place_forget()

        header.AuthButton.bind("<Button-1>", lambda x : authenticate(root, header, header.Authenticate))
        header.AuthButton.enable()

def scan(root, header, scanningView):
    asyncio.run(async_scan(root, header, scanningView))