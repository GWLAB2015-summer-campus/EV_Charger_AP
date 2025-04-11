import subprocess
import log_helper
import environs, os
import asyncio

async def scanning_and_connect():
    MAX_RETRY = 5
    retry = 0
    while retry < MAX_RETRY:
        try:
            env = environs.Env(eager=False)
            env_path = os.getcwd() + "/.env"
            env.read_env(path=env_path)

            interface = env.str("NETWORK_INTERFACE", default="eth0")

            subp_shell = await asyncio.create_subprocess_shell(
                f'bash ./evcc.sh {interface}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            result = await subp_shell.communicate()
            result = result[0].decode("utf-8")
            log_helper.log(result)
            result = result.split("\n")
            add_network = result[-2].split(" ")[0]
            
            if add_network:
                bss = result[-2].split(" ")[1]
                ssid = result[-2].split(" ")[2]
                signal = float(result[-2].split(" ")[3])
                freq = float(result[-2].split(" ")[4]) / 1000
                vse = "".join(result[-2].split(" ")[5:])
                return bss, ssid, signal, freq, vse
            else:
                raise Exception("Need Retry")
        except Exception as e:
            log_helper.log(e)
            log_helper.log("retrying...")
            retry += 1
            await asyncio.sleep(0.5)
    log_helper.log("connect error")
    return None, None, None, None, None

if __name__ == '__main__':
    scanning_and_connect()