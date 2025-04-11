from models import AP, SECC, _ETT, _ADD_INFO

dummy_ap = AP(
    bss="2c:cf:67:e5:aa:73",
    ssid="yunhoAP",
    frequency=2.442,
    signal=-44.0
)

dummy_secc = SECC(
    energy_transfer_type=_ETT(
        AC_support=False,
        DC_support=True,
        WPT_support=False,
        ACD_support=False
    ),
    country_code="KR",
    operator_id="4675418",
    charging_site_id="211295614005",
    additional_infomation=[
        _ADD_INFO(
            ett="AC",
            parameter={
                "C" : [1],
                "M" : [1],
                "S" : ["C", "B", "I"]
            }
        ),
        _ADD_INFO(
            ett="DC",
            parameter={
                "C" : [1],
                "M" : [2],
                "S" : ["C", "H", "B", "I"]
            }
        ),
        _ADD_INFO(
            ett="WPT",
            parameter={
                "Z" : [1],
                "F" : ["A1"],
                "A" : ["P"],
                "P" : ["P"],
                "G" : ["P"]
            }
        ),
        _ADD_INFO(
            ett="ACD",
            parameter={
                "ID" : ["EVIDsdfgdsfsdfsdf"]
            }
        )
    ]
)