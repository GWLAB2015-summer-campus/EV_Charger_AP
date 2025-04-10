import log_helper
import asyncio
from iso15118.evcc.main import main

async def async_authenticate(root, related_content, auth_view):
    root.ids.auth_button.disabled = True
    auth_view.ids.auth_status.change_status("Authenticating")

    # Need to Add Auth Logic
    result = await main()
    
    if result:
        auth_view.ids.auth_status.change_status("Authenticated")
    else:
        auth_view.ids.auth_status.change_status("Authenticated Error")

def authenticate(root, related_content, auth_view):
    asyncio.run(async_authenticate(root, related_content, auth_view))