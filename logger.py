_logView = None

def init_logview(view):
    global _logView
    _logView = view

def logging(value):
    _logView.logging(value)