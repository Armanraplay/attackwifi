import os
import re

def detect_wifi_interfaces():
    interfaces = []
    iwconfig_out = os.popen('iwconfig 2>/dev/null').read()
    for line in iwconfig_out.splitlines():
        if re.match(r'^\w', line):
            name = line.split()[0]
            if "IEEE 802.11" in line or "Mode:Monitor" in line:
                interfaces.append(name)
    return interfaces

def select_interface():
    interfaces = detect_wifi_interfaces()
    if not interfaces:
        print("Tidak ada interface WiFi terdeteksi.")
        return None
    print("Pilih interface WiFi:")
    for idx, iface in enumerate(interfaces, 1):
        print(f"{idx}. {iface}")
    pilihan = input(f"Pilihan [1-{len(interfaces)}]: ").strip()
    try:
        idx = int(pilihan) - 1
        return interfaces[idx]
    except:
        print("Pilihan tidak valid.")
        return None
