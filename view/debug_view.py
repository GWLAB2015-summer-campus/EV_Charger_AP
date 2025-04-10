from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

class DebugView(MDFloatLayout):
    def logging(self, log):
        self.ids.log_list.add_widget(
            MDLabel(
                text=log,
                size_hint=(1, None),
                adaptive_height=True,
            )
        )