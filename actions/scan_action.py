import log_helper
import asyncio
from const import SIZE
from actions.auth_action import authenticate
from models import SECC_parser, AP
from wifi_scanner import scanning_and_connect

async def async_scan(app):
    app.root.ids.scan_button.disabled = True
    app.root.ids.tabs.disabled = True
    
    bss, ssid, signal, freq, vse = scanning_and_connect()

    if vse is None:
        # scanningView.is_error("Connect Error", "AP Not Found")
        app.root.ids.scan_button.disabled = False
        app.root.ids.tabs.disabled = False
    else:
        secc = SECC_parser(vse)
        ap = AP(
            bss=bss,
            ssid=ssid,
            frequency=freq,
            signal=signal
        )

        log_helper.log(ap)
        log_helper.log(secc)

        app.tab_items["AP"].set_ap(ap)
        app.tab_items["EVSE"].set_evse(secc)

        app.root.ids.auth_button.bind(on_press=lambda x: authenticate(
            app.root,
            app.root.ids.related_content,
            app.root.ids.auth_view,
        ))
        app.root.ids.auth_button.disabled = False
        app.root.ids.tabs.disabled = False

def scan(app):
    asyncio.run(async_scan(app))
    app.stop_loading()