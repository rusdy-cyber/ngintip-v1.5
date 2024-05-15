import socket
import sys

def scan_port_with_input(target_host):
    target_ports = {
        21: "FTP (File Transfer Protocol)",
        22: "SSH (Secure Shell)",
        23: "Telnet",
        25: "SMTP (Simple Mail Transfer Protocol)",
        53: "DNS (Domain Name System)",
        80: "HTTP (Hypertext Transfer Protocol)",
        110: "POP3 (Post Office Protocol version 3)",
        135: "Microsoft RPC",
        139: "NetBIOS Session Service",
        143: "IMAP (Internet Message Access Protocol)",
        443: "HTTPS (Hypertext Transfer Protocol Secure)",
        445: "Microsoft-DS",
        993: "IMAPS (IMAP over SSL)",
        995: "POP3S (POP3 over SSL)",
        3389: "Remote Desktop Protocol (RDP)",
        8080: "HTTP alternate (HTTP Proxy)"
    }

    open_ports = []
    closed_ports = []

    for port, service in target_ports.items():
        try:
            # Membuat socket untuk koneksi TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # Mengatur timeout menjadi 2 detik
            
            # Mencoba koneksi ke port pada target_host
            result = sock.connect_ex((target_host, port))
            
            # Memeriksa hasil koneksi
            if result == 0:
                open_ports.append(f"Port {port} ({service}): Open")
            else:
                closed_ports.append(f"Port {port} ({service}): Closed")
            
            sock.close()  # Menutup socket setelah selesai
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            sys.exit()
        except socket.error as e:
            print(f"Gagal terhubung ke port {port}: {e}")
            continue  # Melanjutkan pemindaian ke port berikutnya
        except Exception as e:
            print(f"Terjadi kesalahan pada port {port}: {e}")
            continue  # Melanjutkan pemindaian ke port berikutnya

    return open_ports, closed_ports
