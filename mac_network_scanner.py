import subprocess
import re
import ipaddress
import threading

def ping(ip):
    subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_arp_table():
    arp_output = subprocess.check_output(['arp', '-a'], encoding='utf-8')
    devices = re.findall(r'\((.*?)\) at ([\w:]+)', arp_output)
    return devices

def scan_network():
    local_ip = subprocess.check_output("ipconfig getifaddr en0", shell=True, encoding='utf-8').strip()
    network = ipaddress.ip_network(local_ip + '/24', strict=False)
    
    print(f"🔍 Scanning devices on {network} ...")
    threads = []
    for ip in network.hosts():
        t = threading.Thread(target=ping, args=(str(ip),))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    devices = get_arp_table()
    print(f"\n📡 Devices found:")
    print(f"{'IP Address':20} {'MAC Address'}")
    print("-" * 35)
    for ip, mac in devices:
        print(f"{ip:20} {mac}")

if __name__ == "__main__":
    scan_network()
