import tkinter as tk
from component import Container, Label
from const import SIZE, FONT, COLOR
from models import SECC, AP

class ConnectedContainer(Container):
    def __init__(self, parent, secc = SECC(), ap = AP()):
        Container.__init__(self, parent)

        self.Inner = tk.Frame(self, bg=COLOR["BLACK2"])
        self.Inner.place(
            x=10, y=10,
            width=SIZE["CONTAINER.W"] - 20,
            height=SIZE["CONTAINER.H"] - 20
        )

        self.SSID = Label(self.Inner, 
        text=f"{ap.ssid} ({ap.bss})",
        anchor="w", 
        bg=COLOR["BLACK2"],
        font=FONT["H1"])

        self.SSID.place(x=0, y=0, w=SIZE["CONTAINER.W"] - 20, h=50)

        self.Info1 = Label(self.Inner, 
            text=f"Frequency : {ap.formatter('frequency')(ap.frequency)}    Signal : {ap.formatter('signal')(ap.signal)}    Country Code : {secc.country_code}",
            anchor="w", 
            bg=COLOR["BLACK2"],
            font=FONT["H5"])

        self.Info1.place(x=0, y=50, w=SIZE["CONTAINER.W"] - 20, h=30)

        self.Info2 = Label(self.Inner, 
            text=f"Operator : {secc.operator_id}    Charging Site : {secc.charging_site_id}",
            anchor="w", 
            bg=COLOR["BLACK2"],
            font=FONT["H5"])

        self.Info2.place(x=0, y=80, w=SIZE["CONTAINER.W"] - 20, h=30)

        self.Support_Frame = tk.LabelFrame(self.Inner, text="Support", bg=COLOR["BLACK2"], fg=COLOR["WHITE1"])
        self.Support_Frame.place(x=0, y=115, w=SIZE["CONTAINER.W"] - 20, h=50)
        pos = 115 + 50

        support_w = (SIZE["CONTAINER.W"] - 30) // 4
        
        self.AC_Support_Label = Label(self.Support_Frame,
            text="AC Support", anchor="center", bg=COLOR["BLACK2"], font=FONT["H6"], 
            fg=COLOR["WHITE1"] if secc.energy_transfer_type.AC_support else COLOR["GRAY1"])
        self.AC_Support_Label.place(x=5, y=0, w=support_w)

        self.DC_Support_Label = Label(self.Support_Frame,
            text="DC Support", anchor="center", bg=COLOR["BLACK2"], font=FONT["H6"], 
            fg=COLOR["WHITE1"] if secc.energy_transfer_type.DC_support else COLOR["GRAY1"])
        self.DC_Support_Label.place(x=5+support_w, y=0, w=support_w)

        self.WPT_Support_Label = Label(self.Support_Frame,
            text="WPT Support", anchor="center", bg=COLOR["BLACK2"], font=FONT["H6"], 
            fg=COLOR["WHITE1"] if secc.energy_transfer_type.WPT_support else COLOR["GRAY1"])
        self.WPT_Support_Label.place(x=5+support_w*2, y=0, w=support_w)

        self.ACD_Support_Label = Label(self.Support_Frame,
            text="ACD Support", anchor="center", bg=COLOR["BLACK2"], font=FONT["H6"], 
            fg=COLOR["WHITE1"] if secc.energy_transfer_type.ACD_support else COLOR["GRAY1"])
        self.ACD_Support_Label.place(x=5+support_w*3, y=0, w=support_w)

        formatted_add_info = secc.formatter('additional_infomation')(secc.additional_infomation)

        if 'AC' in formatted_add_info.keys():
            self.AC_Frame = tk.LabelFrame(self.Inner, text="AC", bg=COLOR["BLACK2"], fg=COLOR["WHITE1"])

            self.AC_Frame.place(x=0, y=pos, w=SIZE["CONTAINER.W"] - 20, h=80)
            pos += 80

            for i, info in enumerate(formatted_add_info['AC']):
                Label(self.AC_Frame, text=info, font=FONT["H7"], bg=COLOR["BLACK2"], anchor="w").place(x=5, y=18*i)

        if 'DC' in formatted_add_info.keys():
            self.DC_Frame = tk.LabelFrame(self.Inner, text="DC", bg=COLOR["BLACK2"], fg=COLOR["WHITE1"])

            self.DC_Frame.place(x=0, y=pos, w=SIZE["CONTAINER.W"] - 20, h=80)
            pos += 80

            for i, info in enumerate(formatted_add_info['DC']):
                Label(self.DC_Frame, text=info, font=FONT["H7"], bg=COLOR["BLACK2"], anchor="w").place(x=5, y=18*i)

        if 'WPT' in formatted_add_info.keys():
            self.WPT_Frame = tk.LabelFrame(self.Inner, text="WPT", bg=COLOR["BLACK2"], fg=COLOR["WHITE1"])
            self.WPT_Frame.place(x=0, y=pos, w=SIZE["CONTAINER.W"] - 20, h=110)
            pos += 110

            for i, info in enumerate(formatted_add_info['WPT']):
                Label(self.WPT_Frame, text=info, font=FONT["H7"], bg=COLOR["BLACK2"], anchor="w").place(x=5, y=18*i)

        if 'ACD' in formatted_add_info.keys():
            self.ACD_Frame = tk.LabelFrame(self.Inner, text="ACD", bg=COLOR["BLACK2"], fg=COLOR["WHITE1"])
            self.ACD_Frame.place(x=0, y=pos, w=SIZE["CONTAINER.W"] - 20, h=40)

            for i, info in enumerate(formatted_add_info['ACD']):
                Label(self.ACD_Frame, text=info, font=FONT["H7"], bg=COLOR["BLACK2"], anchor="w").place(x=5, y=18*i)