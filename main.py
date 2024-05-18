from tkinter import ttk
from tools.color import cetak_teks_berwarna
from tools.geo_info import print_info_geo_with_input
from tools.port_scan import scan_port_with_input
from tools.subdomain_scan import scan_subdomain
from tools.what_web import scan_website
from tools.scan_waf import scan_waf 
import sys
import random
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
art_folder = 'art'

art = read_file(os.path.join(art_folder, 'art1.txt'))
art2 = read_file(os.path.join(art_folder, 'art2.txt'))
art3 = read_file(os.path.join(art_folder, 'art3.txt'))
art4 = read_file(os.path.join(art_folder, 'art4.txt'))
art5 = read_file(os.path.join(art_folder, 'art5.txt'))
art6 = read_file(os.path.join(art_folder, 'art6.txt'))

def get_random_art():
    return random.choice([art,art2,art3,art4,art5,art6])

teks = """
Information Gathering tools ngintip V1.5
1. Informasi Geografis IP Address
2. Scan Port
3. Scan Subdomain
4. what web
5. waf detection
6. exit
"""

while True:
    cetak_teks_berwarna(get_random_art())
    cetak_teks_berwarna(teks)

    jawaban = input("(1/2/3/4/5/6/7): ")

    if jawaban == '1':
        print_info_geo_with_input()
    elif jawaban == '2':
        target_host = input("\nEnter hostname/domain/sub-domain: ")
        open_ports, closed_ports = scan_port_with_input(target_host)
        print("\nPort terbuka:")
        print('\n'.join(open_ports))
        print("\nPort tertutup:")
        print('\n'.join(closed_ports))
        pilihan_lanjut = input("\nApakah Anda ingin melanjutkan? (y/n): ")
        if pilihan_lanjut.lower() != 'y':
            print("Perintah selesai.")
            sys.exit()
    elif jawaban == '3':
        domain = input("\nEnter domain untuk pemindaian subdomain: ")
        scan_subdomain(domain)
        pilihan_lanjut = input("\nApakah Anda ingin melanjutkan? (y/n): ")
        if pilihan_lanjut.lower() != 'y':
            print("Perintah selesai.")
            sys.exit()
    elif jawaban == '4':
        url =  input("\nEnter domain untuk pemindaian website: ") 
        scan_website(url)
        pilihan_lanjut = input("\nApakah Anda ingin melanjutkan? (y/n): ")
        if pilihan_lanjut.lower() != 'y':
            print("Perintah selesai.")
            sys.exit()
    elif jawaban == '5':
        url = input("\nEnter domain untuk pemindaian WAF: ")
        scan_waf(url)
        pilihan_lanjut = input("\nApakah Anda ingin melanjutkan? (y/n): ")
        if pilihan_lanjut.lower() != 'y':
            print("Perintah selesai.")
            sys.exit()
    elif jawaban == '6':
        print("\nPerintah selesai.")
        break 
    else:
        print("Opsi tidak dikenali. Silakan coba lagi.")
