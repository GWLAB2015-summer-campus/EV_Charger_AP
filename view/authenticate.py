import tkinter as tk
from const import SIZE, COLOR, FONT
from component import Label

STATE_DICT = {
    "No Authenticated" : {
        "text" : "No Authenticated",
        "color" : COLOR["GRAY2"]
    },
    "Authenticating" : {
        "text" : "Authenticating",
        "color" : COLOR["YELLOW1"]
    },

    "SessionSetup" : {
        "text" : "SessionSetup",
        "color" : COLOR["YELLOW1"]
    },
    "ServiceDiscovery" : {
        "text" : "ServiceDiscovery",
        "color" : COLOR["YELLOW1"]
    },
    "ServiceDetail" : {
        "text" : "ServiceDetail",
        "color" : COLOR["YELLOW1"]
    },
    "PaymentServiceSelection" : {
        "text" : "PaymentServiceSelection",
        "color" : COLOR["YELLOW1"]
    },
    "CertificateInstallation" : {
        "text" : "CertificateInstallation",
        "color" : COLOR["YELLOW1"]
    },
    "PaymentDetails" : {
        "text" : "PaymentDetails",
        "color" : COLOR["YELLOW1"]
    },
    "Authorization" : {
        "text" : "Authorization",
        "color" : COLOR["YELLOW1"]
    },
    "ChargeParameterDiscovery" : {
        "text" : "ChargeParameterDiscovery",
        "color" : COLOR["YELLOW1"]
    },
    "PowerDelivery" : {
        "text" : "PowerDelivery",
        "color" : COLOR["YELLOW1"]
    },
    "CableCheck" : {
        "text" : "CableCheck",
        "color" : COLOR["YELLOW1"]
    },
    "SessionStop" : {
        "text" : "SessionStop",
        "color" : COLOR["YELLOW1"]
    },
    "WeldingDetection" : {
        "text" : "WeldingDetection",
        "color" : COLOR["YELLOW1"]
    },
    "ChargingStatus" : {
        "text" : "ChargingStatus",
        "color" : COLOR["YELLOW1"]
    },
    "CurrentDemand" : {
        "text" : "CurrentDemand",
        "color" : COLOR["YELLOW1"]
    },
    "MeteringReceipt" : {
        "text" : "MeteringReceipt",
        "color" : COLOR["YELLOW1"]
    },
    "PreCharge" : {
        "text" : "PreCharge",
        "color" : COLOR["YELLOW1"]
    },

    "Authenticated" : {
        "text" : "Authenticated",
        "color" : COLOR["GREEN1"]
    },
    "Authenticated Error" : {
        "text" : "Authenticated Error",
        "color" : COLOR["RED1"]
    },
}

class Authenticate(tk.Frame):
    def __init__(self, parent, w=250 + SIZE["DOT.DIA"], h=SIZE["HEADER.H"]):
        tk.Frame.__init__(self, parent, bg=COLOR["BLACK1"])
        label_w = w - SIZE["DOT.DIA"]
        state = STATE_DICT["No Authenticated"]
        self.StateLabel = Label(self, text=state["text"], font=FONT["H5"], anchor="center")
        self.StateLabel.place(x=SIZE["DOT.DIA"], y=0, w=label_w, h=h)
        self.StateDot = tk.Canvas(self, bg=COLOR["BLACK1"], borderwidth=0, highlightthickness=0)
        self.StateDot.place(x=0, y=0, w=SIZE["DOT.DIA"], h=h)
        hgap = (SIZE["HEADER.H"] - SIZE["DOT.DIA"]) // 2
        self.StateDot.create_oval(0, hgap, SIZE["DOT.DIA"], hgap + SIZE["DOT.DIA"], fill=state["color"] )

    def set_state(self, state):
        if state not in STATE_DICT.keys():
            state = STATE_DICT["Authenticated Error"]
        else:
            state = STATE_DICT[state]
        
        self.StateLabel.config(text=state["text"])
        self.StateDot.delete("all")
        hgap = (SIZE["HEADER.H"] - SIZE["DOT.DIA"]) // 2
        self.StateDot.create_oval(0, hgap, SIZE["DOT.DIA"], hgap + SIZE["DOT.DIA"], fill=state["color"])
        self.update()