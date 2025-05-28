from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.chip import MDChip, MDChipText

class ChipBox(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        self.title = kwargs.pop("title", "")
        super().__init__(*args, **kwargs)

class EVSEView(MDFloatLayout):
    _evse = None
    def set_evse(self, evse):
        self._evse = evse
        self.ids.country_code.text = evse.country_code
        self.ids.operator_id.text = evse.operator_id
        self.ids.charging_site_id.text = evse.charging_site_id

        ett_chips = [
            "AC_support",
            "DC_support",
            "WPT_support",
            "ACD_support"
        ]

        self.ids.contents.add_widget(MDDivider())
        chip_box = ChipBox(
            id="support_box",
            title="Support",
        )
        self.ids.contents.add_widget(chip_box)

        for ett in ett_chips:
            chip_box.ids.chip_list.add_widget(
                MDChip(
                    MDChipText(
                        text = ett,
                    ),
                    size_hint = (None, None),
                    adaptive_width = True,
                    adaptive_height = True,
                    disabled = not getattr(evse.energy_transfer_type, ett),
                )
            )

        formatted = evse.formatter("additional_infomation")(evse.additional_infomation)
        for ett, values in formatted.items():
            self.ids.contents.add_widget(
                MDDivider()
            )
            chip_box = ChipBox(
                id=f"{ett}_box",
                title=f"{ett} Information",
            )
            self.ids.contents.add_widget(
                chip_box
            )
            for v in values:
                chip_box.ids.chip_list.add_widget(
                    MDChip(
                        MDChipText(
                            text = v,
                        ),
                        size_hint = (None, None),
                        adaptive_width = True,
                        adaptive_height = True,
                    )
                )
        self.remove_widget(self.ids.empty)