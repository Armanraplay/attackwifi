import os

def check_root():
    if os.geteuid() != 0:
        print("Program harus dijalankan sebagai root.")
        exit(1)

def set_monitor_mode(iface):
    print(f"Mengaktifkan mode monitor di interface {iface} (butuh root)...")
    os.system(f"ip link set {iface} down")
    os.system(f"iwconfig {iface} mode monitor")
    os.system(f"ip link set {iface} up")
    print("Mode monitor aktif.")