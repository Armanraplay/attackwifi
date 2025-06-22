import subprocess
import re

def list_wireless_interfaces():
    # Deteksi interface wireless menggunakan 'iw dev'
    try:
        result = subprocess.run(['iw', 'dev'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        interfaces = []
        for line in result.stdout.splitlines():
            m = re.match(r'\s*Interface\s+(\w+)', line)
            if m:
                interfaces.append(m.group(1))
        return interfaces
    except Exception as e:
        print(f"[!] Gagal mendeteksi interface: {e}")
        return []

def scan_wifi():
    print("[*] Mendeteksi interface wireless ...")
    interfaces = list_wireless_interfaces()
    if not interfaces:
        print("[!] Tidak ada interface wireless terdeteksi.")
        return

    print("\nPilih interface WiFi (mode monitor, misal: wlan0mon):")
    for idx, iface in enumerate(interfaces):
        print(f"  {idx+1}. {iface}")
    try:
        pilih = int(input("Masukkan nomor interface: ").strip())
        iface = interfaces[pilih-1]
    except (ValueError, IndexError):
        print("[!] Pilihan tidak valid.")
        return

    print(f"[*] Menjalankan airodump-ng pada interface {iface} (tekan CTRL+C untuk berhenti)...")
    try:
        subprocess.run(["airodump-ng", iface])
    except KeyboardInterrupt:
        print("\n[*] Scan dihentikan oleh user. Kembali ke menu utama.")
    except FileNotFoundError:
        print("[!] airodump-ng tidak ditemukan. Install dengan: sudo apt install aircrack-ng")
    except Exception as e:
        print(f"[!] Terjadi error: {e}")
