import log_helper
import asyncio
from iso15118.evcc.main import main

_auth_view = None

async def async_authenticate(app):
    global _auth_view
    app.root.ids.auth_button.disabled = True
    _auth_view = app.root.ids.auth_view
    _auth_view.ids.auth_status.change_status("Authenticating")

    # Need to Add Auth Logic
    result = await main()
    
    if result:
        _auth_view.ids.auth_status.change_status("Authenticated")
    else:
        _auth_view.ids.auth_status.change_status("Authenticated Error")
        app.root.ids.auth_button.disabled = False

async def authenticate(app):
    await async_authenticate(app)