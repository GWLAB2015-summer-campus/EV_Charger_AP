import asyncio

from kivy.lang import Builder
from async_app import AsyncApp
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsItemSecondary
from kivymd.uix.tab.tab import MDTabsItemText

from const import SIZE
import view
import log_helper
from actions import scan

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

class MainApp(AsyncApp):
    tab_items = {}

    enter_debug = 0

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

    def _on_scan_btn_click(self, *args):
        self.add_async_task(
            scan(self)
        )
        
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
        self.root.ids.scan_button.bind(on_release=self._on_scan_btn_click)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file("view/kivy.kv")

def init_app():
    app = MainApp()
    Window.size = SIZE.SCREEN.SIZE
    return app

if __name__ == "__main__":
    app = init_app()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.app_func())
    loop.close()