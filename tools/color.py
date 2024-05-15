from colorama import Fore, Style, init

# Inisialisasi Colorama dengan autoreset
init(autoreset=True)

def cetak_teks_berwarna(teks):
    teks_berwarna = Fore.RED + teks + Style.RESET_ALL
    print(teks_berwarna)
