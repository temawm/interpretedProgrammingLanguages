import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]['
                         r''
                         r'0-9]?)$')
    return bool(pattern.match(ip))


def check_ipv4_address(ip):
    if not isinstance(ip, str):
        raise ValueError("Аргумент должен быть строкой.")

    if not is_valid_ipv4(ip):
        raise ValueError(f"'{ip}' не является корректным адресом IPv4.")

    return ip


try:
    ip_address = "255.255.255.255"
    valid_ip = check_ipv4_address(ip_address)
    print(f"Корректный адрес IPv4: {valid_ip}")
except ValueError as e:
    print(e)

try:
    invalid_ip_address = "255.255.255.256"
    valid_ip = check_ipv4_address(invalid_ip_address)
    print(f"Корректный адрес IPv4: {valid_ip}")
except ValueError as e:
    print(e)
