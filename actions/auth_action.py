from logger import logging
import asyncio

async def async_authenticate(root, header, authView):
    logging("start auth")
    header.AuthButton.disable()
    authView.set_state("Authenticating")

    # Need to Add Auth Logic
    await asyncio.sleep(2)
    
    authView.set_state("Authenticated")

def authenticate(root, header, authView):
    asyncio.run(async_authenticate(root, header, authView))