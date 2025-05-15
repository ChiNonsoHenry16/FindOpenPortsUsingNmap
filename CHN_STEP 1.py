# ............STEP 1 - Scan IPs in your network.................
import subprocess

for num in range(00, 200):
    ip = "10.0.0." + str(num)

    try:
        subprocess.check_output("ping " + ip + " -n 1 -w 500", shell=True)
        print("PING", ip, "OK")
    except subprocess.CalledProcessError:
        pass
