from kivymd.uix.floatlayout import MDFloatLayout

class APView(MDFloatLayout):
    _ap = None
    def set_ap(self, ap):
        self._ap = ap
        print(self.ids)
        self.ids.bss.text = ap.bss
        self.ids.ssid.text = ap.ssid
        self.ids.frequency.text = ap.formatter("frequency")(ap.frequency)
        self.ids.signal.text = ap.formatter("signal")(ap.signal)