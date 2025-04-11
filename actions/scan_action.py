import log_helper
from models import SECC_parser, AP
from wifi_scanner import scanning_and_connect

async def async_scan(app):
    app.root.ids.scan_button.disabled = True
    app.root.ids.tabs.disabled = True
    
    bss, ssid, signal, freq, vse = await scanning_and_connect()

    if vse is None:
        app.root.ids.scan_button.disabled = False
        app.root.ids.tabs.disabled = False
        await log_helper.snack_error("Failed to Connect AP")
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

        app.root.ids.tabs.disabled = False
        app.root.ids.auth_button.disabled = False

async def scan(app):
    await async_scan(app)