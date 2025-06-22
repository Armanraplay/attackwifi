import subprocess

def scan_wifi():
    print("[*] Melakukan scanning jaringan WiFi (butuh mode monitor, root)...")
    try:
        # Cek interface WiFi (misal wlan0mon)
        iface = input("Masukkan nama interface WiFi (mode monitor): ").strip()
        result = subprocess.run(
            ["iwlist", iface, "scan"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
        )
        if result.returncode != 0:
            print("Gagal scan. Pastikan interface sudah mode monitor & benar.")
            print(result.stderr)
            return

        networks = []
        for line in result.stdout.split("\n"):
            if 'ESSID' in line:
                essid = line.split(':')[1].replace('"', '')
                networks.append(essid)
        print(f"Jaringan ditemukan: {', '.join(networks) if networks else 'tidak ada'}")
    except Exception as e:
        print(f"Error: {e}")
