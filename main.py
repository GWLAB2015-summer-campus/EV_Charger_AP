import asyncio

from kivy.lang import Builder
from async_app import AsyncApp
from kivy.core.window import Window
from kivymd.uix.divider import MDDivider
from kivymd.uix.tab import MDTabsItemSecondary
from kivymd.uix.tab.tab import MDTabsItemText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
)
from kivymd.uix.list import (
    MDListItem,
    MDListItemSupportingText,
)

from const import SIZE
import view
import log_helper
from actions import scan, authenticate

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

    def set_fullscreen(self, fullscreen):
        log_helper.log(f"Set fullscreen to {fullscreen}")
        Window.fullscreen = fullscreen
        self.debug_dialog.dismiss()
        self.debug_dialog = None

    def quit(self):
        log_helper.log("Quitting application")
        self.stop()

    debug_dialog = None
    def init_debug_Menu(self):
        debug_menu = [
            {
                "title" : "Fullscreen Mode",
                "option" : not Window.fullscreen,
                "func" : lambda x: self.set_fullscreen(True)
            },
            {
                "title" : "Window Mode",
                "option" : Window.fullscreen,
                "func" : lambda x: self.set_fullscreen(False)
            },
            {
                "title" : "Exit",
                "option" : True,
                "func" : lambda x: self.stop()
            }
        ]
        content_list = []
        for menu in debug_menu:
            if menu["option"]:
                content_list.append(
                    MDListItem(
                        MDListItemSupportingText(
                            text=menu["title"],
                        ),
                        on_release=menu["func"],
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    )
                )
                content_list.append(MDDivider())
        content_list.remove(content_list[-1])
                
        self.debug_dialog = MDDialog(
            MDDialogHeadlineText(
                text="Debug Menu",
                halign="left",
            ),
            MDDialogContentContainer(
                *content_list,
                orientation="vertical",
            ),
        )


    def on_tab_switch(self, *args):
        current_tab = args[0].get_current_tab()
        target_tab = args[1]

        if current_tab and current_tab == target_tab:
            if target_tab.id == "Debug":
                if self.enter_debug >= 5:
                    if not self.debug_dialog:
                        self.init_debug_Menu()
                    self.debug_dialog.open()
                    self.enter_debug = 0
                else:
                    self.enter_debug += 1
            else:
                self.enter_debug = 0

    def _on_scan_btn_click(self, *args):
        if not self.root.ids.scan_button.disabled:
            self.add_async_task(
                scan(self)
            )

    def _on_auth_btn_click(self, *args):
        if not self.root.ids.auth_button.disabled:
            self.add_async_task(
                authenticate(self), False
            )

    def _on_config_change(self, *largs):
        return super()._on_config_change(*largs)
        
    def on_start(self):
        self.root.ids.tabs.bind(on_tab_switch=self.on_tab_switch)
        for tab in TabItems:
            self.root.ids.tabs.add_widget(
                MDTabsItemSecondary(
                    MDTabsItemText(
                        text=tab["title"],
                    ),
                    id=tab["title"],
                    width = 120,
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
        self.root.ids.auth_button.bind(on_release=self._on_auth_btn_click)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file("view/kivy.kv")

def init_app():
    app = MainApp()
    Window.size = SIZE.SCREEN.SIZE
    Window.fullscreen = True
    return app

if __name__ == "__main__":
    app = init_app()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.app_func())
    loop.close()