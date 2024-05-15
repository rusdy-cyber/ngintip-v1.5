import sublist3r

def scan_subdomain(domain):
    print(f"Memindai subdomain untuk domain '{domain}'...")

    try:
        subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        
        if subdomains:
            print("Subdomain yang ditemukan:")
            for subdomain in subdomains:
                print(f"- {subdomain}")
        else:
            print("Tidak ada subdomain yang ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    domain = input("Masukkan domain untuk pemindaian subdomain: ")
    scan_subdomain(domain)