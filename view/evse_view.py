from kivymd.uix.floatlayout import MDFloatLayout

class EVSEView(MDFloatLayout):
    _evse = None
    def set_evse(self, evse):
        self._evse = evse
        self.ids.country_code.text = evse.country_code
        self.ids.operator_id.text = evse.operator_id
        self.ids.charging_site_id.text = evse.charging_site_id