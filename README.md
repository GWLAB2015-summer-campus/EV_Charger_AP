# ISO 15118-8 GUI Tool For EV

## Overview

The objective of this project is to develop a graphical user interface (GUI) that can be utilized in an electric vehicle (EV) charging scenario in accordance with the standards outlined in ISO 15118-8. The process entails scanning the EV, establishing a connection with the SECC, and subsequently receiving and parsing the data. The GUI enables users to perform scanning operations on the SECC through tactile interaction. Subsequent to establishing a connection, users can access comprehensive information regarding the AP and the SECC, in addition to the program debug log.

## Environment

- OS: Raspberry Pi OS 32-bit
- Python: 3.11.2
- Package
  - tkinter (GUI)
  - asyncio (async programing)

## Usage

This program depend on `wpa_cli` and `iw`. So, You need to use Linux based OS.

### Update And Upgrade
```bash
sudo apt update & sudo apt upgrade -y
```

### Install Dependency
```bash
sudo apt install net-tools gawk git
```

### Clone the repository

```bash
git clone https://github.com/GWLAB2015-summer-campus/EV_Charger_AP.git
cd EV_Charger_AP
```

### Run

```bash
sudo python main.py
```

note: sudo is required to access the wifi interface

## Preview
![20250324_14h27m52s_grimb](https://github.com/user-attachments/assets/cdbc76b5-a105-4eb2-b1dd-737006ddaba0)
![20250324_14h29m21s_grimbb](https://github.com/user-attachments/assets/0b99f874-0240-4034-a4d7-ab3f018cb644)

## Structure
- main.py : program main file
- logger.py : log on log view
- models.py : SECC and AP data model and formatter
- wifi_scanner.py : run `evcc.sh` for scan ap
- evcc.sh : shell script file for use `wpa_cli`, `iw` and `gawk`
- selectap.awk : awk file to select ap
- view : tkinter gui views
- const : constant values
- component : unit gui
- actions : action on gui include scanning

## Element Fields in ISO 15118-8

All elements are encoded in hex code bytes.

### Common Elements

The elements must be set to be the same in the SECC and EVCC, except for the length. In this program, EV will only select the SECC with the same elements from among several SECCs.

| Field           | Size (bytes)   | Value         | Description        |
|---              |---             |---            |---                 |
|EID              |1               |0xDD           |Fixed               |
|Length           |1               |0x11 ~ 0xFF    |payload length      |
|Organization ID  |5               |0x70B3D53190   |Fixed in ISO 15118  |

### SECC Elements

| Field                | Size (bytes)   | Value         | Description                                                                                        |
|---                   |---             |---            |---                                                                                                 |
|Element type          |1               |0x01           |Fixed if SECC                                                                                       |
|Energy Transfer type  |8               |0x01 ~ 0x0F    |bit 0 - AC support <br /> bit 1 - DC support <br /> bit 2 - WPT support <br /> bit 3 - ACD support  |
|Country Code          |2               |               |Two character country code ( ISO 3166-1 )                                                           |
|Operator ID           |3               |               |If no operator ID, the value set to 0x2D2D2D ("---")                                       |
|Charging site ID      |5               |               |Unique identifier of the CS. It is numerical not UTF-8 string                                       |
|Additional Information|0 ~ 255         |UTF-8 String   |see Additional Information section                                                                  |

### EVCC Elements

| Field                | Size (bytes)   | Value         | Description                                                                                        |
|---                   |---             |---            |---                                                                                                 |
|Element type          |1               |0x02           |Fixed if EVCC                                                                                       |
|Energy Transfer type  |8               |0x01 ~ 0x0F    |bit 0 - AC support <br /> bit 1 - DC support <br /> bit 2 - WPT support <br /> bit 3 - ACD support  |
|Additional Information|0 ~ 255         |UTF-8 String   |see Additional Information section                                                                  |

Because EVs need to find compatible CS, they compare the Elergy Transfer Type (ETT) of the EVCC to the ETT of the SECC and select only the appropriate SECC.

### Additional Information

#### Form
```
<ETT>:<parameter>=<value>:<parameter>=<value>,<value>|<ETT>:etc.
```
- `<ETT>`                 Energy Transfer type ( AC, DC, WPT, ACD )
- `<parameter>, <value>`  defined in Parameters
- `:` (0x3A)               separate ETT and parameters
- `=` (0x3D)               separate parameters from its values
- `,` (0x2C)              separate multiple values
- `|` (0x7C)               one per ETT

#### Parameters

- AC

| Parameter  | Value               | Description                                                                                              |
|---         |---                  |---                                                                                                       |
| C          | 1, 2, 3             | AC charging connector type                                                                               |
| M          | 1, 3                | AC charging phase                                                                                        |
| S          | C, B, I (multiple)  | C - charging service <br /> B - bidrectional power transfer service <br /> I - island operation service  |

- DC

| Parameter  | Value                  | Description                                                                                                                                                                                                 |
|---         |---                     |---                                                                                                                                                                                                          |
| C          | 1, 2, 3                | DC charging connector type                                                                                                                                                                                  |
| M          | 1, 2, 3, 4             | DC charging mode <br /> 1 - on the core pins <br /> 2 - using the extended pins of a configuration EE or FF connector <br /> 3 - using the core pins of a configuration EE or FF connector <br /> 4 - using a dedicated DC coupler  |
| S          | C, H, B, I (multiple)  | C - charging service <br /> H - high power charging service <br /> B - bidrectional power transfer service <br /> I - island operation service                                                              |

- WPT

| Parameter  | Value                 | Description |
|---         |---                    |---          |
| Z          | 1, 2, 3               | Gap class   |
| F          | M, A1, A2, V1, V2, E  | Fine positioning <br /> M - Manula/proprietary positioning <br /> A1 - using low frequency antenna ( EV -> EVSE ) <br /> A2 - using low frequency antenna ( EVSE -> EV ) <br /> V1 - using magnetic vectoring ( EV -> EVSE ) <br /> V2 - using magnetic vectoring ( EVSE -> EV ) <br /> E - using low power excitation ( EVSE -> EV ) |
| A          | E, P                  | Alignment check using <br /> E - low power excitation <br /> P - point-to-point signal ( EV -> EVSE ) |
| P          | E, P, V, A            | Pairing using <br /> E - low power excitation ( EVSE -> EV ) <br /> P - point-to-point signal ( EV -> EVSE ) <br /> V - magnetic vectoring <br /> A - low frequency antenna |
| G          | C, D, P               | Geometry of primary device <br /> C - circular <br /> D - double D <br /> P - polarized |

- ACD

| Parameter  | Value               | Description                                    |
|---         |---                  |---                                             |
| ID         |                     | EVID which may be used to support association  |
