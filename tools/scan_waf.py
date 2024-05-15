from wafw00f.main import WAFW00F

def scan_waf(url):
    print(f"Memindai WAF untuk website '{url}' menggunakan wafw00f...")

    try:
        # Inisialisasi WAFW00F dengan URL yang diberikan
        waf = WAFW00F(url)
        
        # Lakukan pemindaian
        waf.identwaf()
        
        # Dapatkan hasil pemindaian
        result = waf.result_dict
        
        if result:
            print("Hasil pemindaian wafw00f:")
            for waf_name, waf_info in result.items():
                print(f"- {waf_name}: {waf_info}")
        else:
            print("Tidak ada WAF yang terdeteksi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    url = input("Masukkan URL untuk pemindaian WAF: ")
    scan_waf(url)
