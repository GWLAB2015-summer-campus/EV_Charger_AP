from kivymd.uix.screen import MDScreen

class LoadingView(MDScreen):
    def end_loading(self):
        self.parent.remove_widget(self)