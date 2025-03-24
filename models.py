from dataclasses import dataclass, field
import binascii
from typing import List, Dict

class _WithFormatter:
    _formatter = {}

    def defaultformatter(self, value):
        return value

    def formatter(self, field):
        if field in self._formatter.keys():
            return self._formatter[field]
        else:
            return self.defaultformatter

@dataclass
class _AP:
    bss: str = ""
    ssid: str = ""
    frequency: float = 0.0
    signal: float = 0.0

class AP(_AP, _WithFormatter):

    def _freq_format(value):
        return f"{value} GHz"

    def _signal_format(value):
        return f"{value} dBm"

    _formatter = {
        "frequency" : _freq_format,
        "signal" : _signal_format
    }

@dataclass
class _ETT:
    AC_support: bool = False
    DC_support: bool = False
    WPT_support: bool = False
    ACD_support: bool = False

@dataclass
class _ADD_INFO:
    ett: str = ""
    parameter: Dict[str, List[str]] = field(default_factory=dict)

@dataclass
class _SECC:
    energy_transfer_type: _ETT = field(default_factory=lambda : _ETT())
    country_code: str = ""
    operator_id: str = ""
    charging_site_id: str = ""
    additional_infomation: List[_ADD_INFO] = field(default_factory=list)

class SECC(_SECC, _WithFormatter):
    def _add_info_format(value):
        result = {}
        for v in value:
            ett = v.ett
            result[ett] = []
            for key, value in v.parameter.items():
                formatted = None
                if key == 'C':
                    formatted = f"charging connector type {value[0]}"
                elif key == 'M':
                    if ett == 'AC':
                        formatted.value.append(
                            f"{value[0]} phase charging"
                        )
                    elif ett == 'DC':
                        modes = [
                            "charging on the core pins",
                            "charging using the extended pins of a configuration EE, FF connector",
                            "charging using the core pins of a configuration EE, FF connector",
                            "charging using a dedicated DC coupler"
                        ]
                        formatted = modes[int(value[0])+1]
                elif key == 'S':
                    services = {
                        'C' : "charging",
                        'H' : "High power charging",
                        'B' : "Bidirectional power transfer",
                        'I' : "Island operation"
                    }
                    print(value)
                    formatted = ','.join([services[v] for v in value])
                elif key == 'Z':
                    formatted = f"Gap class Z{value[0]}"
                elif key == 'P':
                    pairing = {
                        'E' : "low power excitation ( EVSE -> EV )",
                        'P' : "point-to-point signal ( EV -> EVSE )",
                        'V' : "magnetic vectoring",
                        'A' : "low frequency antenna"
                    }
                    formatted = f"Pairing using {pairing[value[0]]}"
                elif key == 'F':
                    fine_pos = {
                        'M' : "Manula/proprietary positioning",
                        'A1' : "Fine positioning using low frequency antenna ( EV -> EVSE )",
                        'A2' : "Fine positioning using low frequency antenna ( EVSE -> EV )",
                        'V1' : "Fine positioning using magnetic vectoring ( EV -> EVSE )",
                        'V2' : "Fine positioning using magnetic vectoring ( EVSE -> EV )",
                        "E" : "Fine positioning using low power excitation ( EVSE -> EV )"
                    }
                    formatted = fine_pos[value[0]]
                elif key == 'A':
                    alignment = {
                        'E' : "Alignment check using low power excitation",
                        'P' : "Alignment check using point-to-point signal ( EV -> EVSE )"
                    }
                    formatted = alignment[value[0]]
                elif key == 'G':
                    geometry = {
                        'C' : "circular",
                        'D' : "double D",
                        'P' : "polarized"
                    }
                    formatted = f"Geometry of primary device is {geometry[value[0]]}"
                elif key == 'ID':
                    formatted = value[0]
                if formatted != None:
                    result[v.ett].append(formatted)
        return result

    _formatter = {
        "additional_infomation": _add_info_format
    }

def additional_info_parser(field):
    split_by_ett = field.split('|')
    additional_info_list = []
    for ett_field in split_by_ett:
        split_by_param = field.split(':')
        ett = split_by_param[0]
        params = split_by_param[1:]
        info = _ADD_INFO(ett=ett)
        for param in params:
            [key, value] = param.split('=')
            info.parameter[key] = value.split(',')
        additional_info_list.append(info)
    return additional_info_list

def SECC_parser(vse):

    ett_field = bin(int(vse[16:18], 16))[2:].zfill(8)

    secc = SECC(
        energy_transfer_type=_ETT(
            AC_support = (ett_field[-1] == '1'),
            DC_support = (ett_field[-2] == '1'),
            WPT_support = (ett_field[-3] == '1'),
            ACD_support = (ett_field[-4] == '1')
        ),
        country_code=str(binascii.unhexlify(vse[18:22]))[1:].replace("'",""),
        operator_id=int(vse[22:28], 16),
        charging_site_id=int(vse[28:38], 16),
        additional_infomation=additional_info_parser(str(binascii.unhexlify(vse[38:]))[1:].replace("'",""))
    )
    return secc