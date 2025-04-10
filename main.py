from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsItemSecondary
from kivymd.uix.tab.tab import MDTabsItemText
from kivy.metrics import dp

from const import SIZE
import view
import log_helper
from actions import scan
from dummy_info import dummy_ap, dummy_secc

TabItems = [
        {
            "title" : "AP",
            "lander": view.APView
        },
        {
            "title" : "EVSE",
            "lander": view.EVSEView
        },
        {
            "title" : "Authentication",
            "lander": view.AuthView
        },
        {
            "title" : "Debug",
            "lander": view.DebugView
        },
    ]

class MainApp(MDApp):
    tab_items = {}

    enter_debug = 0

    def start_loading(self):
        self.root.ids.loading.size_hint = (None, None)
        self.root.ids.tabs.disabled = True
        self.root.ids.loading_text.text = "Loading..."
        self.root.refresh()

    def stop_loading(self):
        self.root.ids.loading.size_hint = (
            0, 0
        )
        self.root.ids.tabs.disabled = False
        self.root.ids.loading_text.text = ""

    def on_tab_switch(self, *args):
        current_tab = args[0].get_current_tab()
        target_tab = args[1]

        if current_tab and current_tab == target_tab:
            if target_tab.id == "Debug":
                if self.enter_debug >= 5:
                    log_helper.log("Debug mode activated")
                    Window.fullscreen = not Window.fullscreen
                    self.enter_debug = 0
                else:
                    log_helper.log(f"Tab {5 - self.enter_debug} attempts to enter Debug mode")
                    self.enter_debug += 1
            else:
                self.enter_debug = 0
        
    def on_start(self):
        self.root.ids.tabs.bind(on_tab_switch=self.on_tab_switch)
        for tab in TabItems:
            self.root.ids.tabs.add_widget(
                MDTabsItemSecondary(
                    MDTabsItemText(
                        text=tab["title"],
                    ),
                    id=tab["title"],
                )
            )
            item_view = tab["lander"](
                id=f'tab_item_{tab["title"]}',
            )
            self.tab_items[tab["title"]] = item_view

            if tab["title"] == "Debug":
                log_helper.set_log_view(item_view)

            self.root.ids.related_content.add_widget(
                item_view
            )
        self.root.ids.tabs.switch_tab(text=TabItems[0]["title"])
        self.root.ids.scan_button.bind(on_press=lambda x : self.on_scan_click())

    def on_scan_click(self):
        if not self.root.ids.scan_button.disabled:
            self.start_loading()
            scan(self)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file("view/kivy.kv")

def init_app():
    app = MainApp()
    Window.size = SIZE.SCREEN.SIZE
    app.run()

if __name__ == "__main__":
    init_app()