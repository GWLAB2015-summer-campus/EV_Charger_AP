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
