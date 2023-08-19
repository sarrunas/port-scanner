import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[ Scanning target ] ' + str(target))
    for port in range(port_num1, port_num2):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
    
def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


targets = input('[+] Enter Target/s To Scan (split multiple targets with , ): ')
port_num = input('[+] Enter port or ports range you want to scan (split with - ): ')

if '-' in port_num:
    port_num = port_num.split('-')
    port_num1, port_num2 = int(port_num[0]), int(port_num[1]) + 1
else:
    port_num1, port_num2 = (int(port_num), int(port_num) + 1)

if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '))
else:
    scan(targets)
