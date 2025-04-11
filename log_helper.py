from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

_log_view = None

def set_log_view(log_view):
    global _log_view
    _log_view = log_view

def get_log_view():
    return _log_view

def log(obj):
    print(obj)
    log_view = get_log_view()
    if log_view:
        log_view.logging(str(obj))

async def snack_error(message):
    MDSnackbar(
        MDSnackbarText(
            text=message,
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),
        ),
        pos=(5, 5),
        size_hint=(.3, .15),
        duration=1,
        background_color=(1, 0.72, 0.72, 1),
    ).open()