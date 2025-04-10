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