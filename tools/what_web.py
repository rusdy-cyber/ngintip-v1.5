import subprocess

def scan_website(url):
    print(f"Memindai website '{url}' menggunakan whatweb...")

    try:
        result = subprocess.run(['whatweb', url], capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            print("Hasil pemindaian whatweb:")
            print(output)
        else:
            print("Tidak ada hasil yang ditemukan atau terjadi kesalahan.")
            print(f"Kode keluaran: {result.returncode}")
            print(f"Pesan kesalahan: {result.stderr}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    url = input("Masukkan URL untuk pemindaian website: ")
    scan_website(url)
