# attackwifi

Tools serbaguna mirip Wifite & Wireshark berbasis CLI (Python).

**Fitur:**
- Scan WiFi (deteksi interface otomatis, mode monitor, airodump-ng)
- Menu attack (handshake, deauth — siap dikembangkan)
- Capture/sniff paket & simpan ke `.pcap`
- Analisa paket (buka file pcap)

---

## Instalasi
```sh
pip install scapy
sudo apt install wireless-tools aircrack-ng
```

## Cara Pakai
1. Jalankan sebagai root/sudo.
2. Pastikan WiFi interface sudah mode monitor (gunakan `utils.py` atau manual).
3. Jalankan:
   ```
   sudo python3 main.py
   ```
4. Ikuti menu.

## Catatan
- Fitur attack (handshake, deauth) masih skeleton, siap dikembangkan.
- Gunakan hanya untuk edukasi & pentest legal.
