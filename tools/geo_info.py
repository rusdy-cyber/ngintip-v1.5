import requests
import socket
import sys
import whois

def print_info_geo(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\nInformasi Geografis untuk IP {}:".format(ip))
        print("IP Address     :", data.get('ip', 'N/A'))
        print("Hostname       :", data.get('hostname', 'N/A'))
        print("Lokasi         :", data.get('city', 'N/A'), data.get('region', 'N/A'), data.get('country', 'N/A'), data.get('postal', 'N/A'))
        print("Koordinat      :", data.get('loc', 'N/A'))
        print("Penyedia Layanan Internet :", data.get('org', 'N/A'))
    else:
        print("Gagal mendapatkan informasi geografis.")

def print_whois_info(domain):
    try:
        w = whois.whois(domain)
        print("\nInformasi WHOIS untuk domain '{}':".format(domain))
        print("Tanggal Kedaluwarsa   :", w.expiration_date)
        print("Email Pendaftar       :", w.emails)
        print("Nomor Telepon Pendaftar:", w.phone)
    except Exception as e:
        print("Gagal mendapatkan informasi WHOIS. Kesalahan:", e)

def print_info_geo_with_input():
    target_host = input("\nMasukkan hostname/domain/sub-domain: ")

    try:
        ip = socket.gethostbyname(target_host)
        print_info_geo(ip)
        print_whois_info(target_host)
    except socket.gaierror:
        print("Maaf, IP tidak ditemukan. Mohon periksa kembali domain atau koneksi internet Anda.")

    pilihan_lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
    if pilihan_lanjut.lower() != 'y':
        print("Perintah selesai.")
        sys.exit()

# Contoh penggunaan
if __name__ == "__main__":
    print_info_geo_with_input()
