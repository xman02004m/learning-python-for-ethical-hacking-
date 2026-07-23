import socket

target = "127.0.0.1"   # your own computer, safe to test on
port = 24

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)   # don't wait forever if there's no response
result = s.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

s.close()


# Wrap the single-port check into a function scan_port(target, port) that returns True/False instead of printing directly.


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        return True
    else:
        return False

print(scan_port("127.0.0.1", 8000))
print(scan_port("127.0.0.1", 80))
# s.close()

# Using the ports list [21, 22, 80, 443, 3306], loop through and scan each one against 127.0.0.1, printing open/closed for each (keep your test server running on 8000 if you want to see at least one open result — or add 8000 to your ports list).

# ports_list = [21, 22, 80, 443, 3306, 8000]
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(1)

# for port in ports_list:
#     result = s.connect_ex((target, port))
#     # s.close()
#     if result == 0:
#      print(f"Port {port} is OPEN")
#     else:
#      print(f"Port {port} is CLOSED")

# s.close
ports_list = [21, 22, 80, 443, 3306, 8000]

for port in ports_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    



# Combine into a function scan_range(target, start, end) that scans every port from start to end and prints only the open ones.

def scan_range(target, start, end):
    for i in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, i))
        s.close()
        if result == 0:
            print(f"Port {i} is OPEN")

scan_range("127.0.0.1", 7999, 8001)
