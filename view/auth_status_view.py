from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, Ellipse

COLOR = {
    "GRAY" : (0.85, 0.85, 0.85, 1),
    "YELLOW" : (1, 0.91, 0.27, 1),
    "GREEN" : (0.32, 1, 0.42, 1),
    "RED" : (1, 0.42, 0.42, 1),
}

STATE_DICT = {
    "No Authenticated" : {
        "text" : "No Authenticated",
        "color" : COLOR["GRAY"]
    },
    "Authenticating" : {
        "text" : "Authenticating",
        "color" : COLOR["YELLOW"]
    },

    "SessionSetup" : {
        "text" : "SessionSetup",
        "color" : COLOR["YELLOW"]
    },
    "ServiceDiscovery" : {
        "text" : "ServiceDiscovery",
        "color" : COLOR["YELLOW"]
    },
    "ServiceDetail" : {
        "text" : "ServiceDetail",
        "color" : COLOR["YELLOW"]
    },
    "PaymentServiceSelection" : {
        "text" : "PaymentServiceSelection",
        "color" : COLOR["YELLOW"]
    },
    "CertificateInstallation" : {
        "text" : "CertificateInstallation",
        "color" : COLOR["YELLOW"]
    },
    "PaymentDetails" : {
        "text" : "PaymentDetails",
        "color" : COLOR["YELLOW"]
    },
    "Authorization" : {
        "text" : "Authorization",
        "color" : COLOR["YELLOW"]
    },
    "ChargeParameterDiscovery" : {
        "text" : "ChargeParameterDiscovery",
        "color" : COLOR["YELLOW"]
    },
    "PowerDelivery" : {
        "text" : "PowerDelivery",
        "color" : COLOR["YELLOW"]
    },
    "CableCheck" : {
        "text" : "CableCheck",
        "color" : COLOR["YELLOW"]
    },
    "SessionStop" : {
        "text" : "SessionStop",
        "color" : COLOR["YELLOW"]
    },
    "WeldingDetection" : {
        "text" : "WeldingDetection",
        "color" : COLOR["YELLOW"]
    },
    "ChargingStatus" : {
        "text" : "ChargingStatus",
        "color" : COLOR["YELLOW"]
    },
    "CurrentDemand" : {
        "text" : "CurrentDemand",
        "color" : COLOR["YELLOW"]
    },
    "MeteringReceipt" : {
        "text" : "MeteringReceipt",
        "color" : COLOR["YELLOW"]
    },
    "PreCharge" : {
        "text" : "PreCharge",
        "color" : COLOR["YELLOW"]
    },

    "Authenticated" : {
        "text" : "Authenticated",
        "color" : COLOR["GREEN"]
    },
    "Authenticated Error" : {
        "text" : "Authenticated Error",
        "color" : COLOR["RED"]
    },
}

class AuthStatusView(MDFloatLayout):

    def change_status(self, status):
        status = STATE_DICT.get(status, STATE_DICT["Authenticated Error"])
        with self.canvas:
            self.canvas.clear()
            Color(rgba=status["color"])
            Ellipse(
                pos=(
                    self.x,
                    self.y + self.height / 2 - 13
                ), 
                size=(
                    26, 26
                )
            )
            MDLabel(
                text=status["text"],
                pos=(
                    self.x + self.height*0.4 + 10,
                    self.y
                ),
                size_hint=(None, None),
                height=self.height,
                width=self.width - self.height*0.4 - 10,
                halign="center"
            )