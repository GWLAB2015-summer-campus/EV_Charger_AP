import subprocess
from logger import logging

def scanning_and_connect():
    interface = "wlan0"

    result = subprocess.run(f'bash ./evcc.sh {interface}', capture_output=True, text=True, shell=True)
    logging(result.stdout)
    result = result.stdout.split("\n")
    add_network = result[-2].split(" ")[0]
    
    if not add_network:
        logging("connect error")
        return None, None, None, None, None
    else:
        bss = result[-2].split(" ")[1]
        ssid = result[-2].split(" ")[2]
        signal = float(result[-2].split(" ")[3])
        freq = float(result[-2].split(" ")[4]) / 1000
        vse = "".join(result[-2].split(" ")[5:])
        return bss, ssid, signal, freq, vse

if __name__ == '__main__':
    scanning_and_connect()