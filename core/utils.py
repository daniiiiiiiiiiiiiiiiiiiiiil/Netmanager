import subprocess
import psutil
import socket
from scapy.all import sniff, IP, TCP, UDP, ICMP, conf


def get_interfaces():
    interfaces = []
    stats = psutil.net_if_addrs()
    for name, addrs in stats.items():
        ip_info = next((addr for addr in addrs if addr.family == socket.AF_INET), None)
        interfaces.append({
            'name': name,
            'ip': ip_info.address if ip_info else 'Нет IP',
            'mask': ip_info.netmask if ip_info else '-',
        })
    return interfaces


def run_command(command):
    # Используем shell=True для Windows команд
    res = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='cp866')
    return res.stdout if res.returncode == 0 else res.stderr


def capture_packets(count=15):
    captured_data = []

    def process_packet(packet):
        if IP in packet:
            # Определяем протокол
            proto = "OTHER"
            if TCP in packet:
                proto = "TCP"
            elif UDP in packet:
                proto = "UDP"
            elif ICMP in packet:
                proto = "ICMP"

            captured_data.append({
                'src': packet[IP].src,
                'dst': packet[IP].dst,
                'proto': proto,
                'len': len(packet),
                'summary': packet.summary()
            })

    # Захват с таймаутом, чтобы не вешать сервер
    try:
        sniff(count=count, prn=process_packet, timeout=5, store=False)
    except Exception as e:
        captured_data.append(
            {'proto': 'SYSTEM', 'src': '-', 'dst': '-', 'len': 0, 'summary': f'Ошибка захвата: {str(e)}'})

    return captured_data


def set_ip_address(iface, ip, mask, gateway):
    # Команда netsh требует прав администратора
    cmd = f'netsh interface ip set address "{iface}" static {ip} {mask} {gateway}'
    return run_command(cmd)


def ping_host(host):
    return run_command(f'ping -n 4 {host}')


def get_routing_table():
    return run_command('route print -4')