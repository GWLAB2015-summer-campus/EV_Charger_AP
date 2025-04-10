from logger import logging
import asyncio
from iso15118.evcc.main import main

async def async_authenticate(root, header, authView):
    logging("start auth")
    header.AuthButton.disable()
    authView.set_state("Authenticating")

    # Need to Add Auth Logic
    result = await main()
    
    if result:
        authView.set_state("Authenticated")
    else:
        authView.set_state("Authenticated Error")

def authenticate(root, header, authView):
    asyncio.run(async_authenticate(root, header, authView))