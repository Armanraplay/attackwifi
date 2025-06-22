import subprocess

def scan_wifi():
    print("[*] Melakukan scanning jaringan WiFi dengan airodump-ng (mode monitor, root diperlukan).")
    iface = input("Masukkan nama interface WiFi (mode monitor, contoh: wlan0mon): ").strip()
    print("[*] Tekan CTRL+C untuk menghentikan scan dan kembali ke menu utama.")
    try:
        # Jalankan airodump-ng, tampilkan output langsung
        subprocess.run(["airodump-ng", iface])
    except KeyboardInterrupt:
        print("\n[*] Scan dihentikan oleh user. Kembali ke menu utama.")
    except FileNotFoundError:
        print("[!] airodump-ng tidak ditemukan. Install dengan: sudo apt install aircrack-ng")
    except Exception as e:
        print(f"[!] Terjadi error: {e}")
