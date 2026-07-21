# Basics — defining and calling

# Write a function greet() that takes no parameters and just prints "Starting scan...". Call it.
# Write a function scan_port(port) that takes a port number as a parameter and prints "Scanning port: <port>". Call it with a few different port numbers.
# Write a function add_numbers(a, b) that takes two numbers and returns their sum (don't print inside the function — print the result when you call it).

def greet():
    print("Starting scan....")
greet()

def scan_port(port):
    print(f"Scanning port: {port}")
scan_port(443)
scan_port(24)

def add_number(a,b):
    z = a + b
    return z
print(add_number(1,2))

# Return values (this trips people up)
# 4. Write a function is_common_port(port) that takes a port number and returns True if it's 22, 80, or 443, otherwise returns False. Call it with a few ports and print the result.
# 5. Write a function password_strength(length) that takes a password length and returns the string "Weak", "Moderate", or "Strong" based on the same rules as your earlier if/elif exercise. Call it and print the return value.

def is_common_port(port):
    if port == 22 or port == 80 or port == 443:
        return True
    else:
        return False

print(is_common_port(22))
print(is_common_port(80))
print(is_common_port(24))

# user = int(input("Enter any port: "))
# userinput = is_common_port(user)
# print(userinput)

def password_strenght(length):
    if length <= 8:
        return("weak password your ")
    elif length <= 12:
        return("Good password")
    else:
        return("Bro you cooked the hacker mind ")

print(password_strenght(8))
print(password_strenght(11))
print(password_strenght(12))
print(password_strenght(22))
# Default parameters
# 6. Write a function scan_port(port, timeout=5) — if the caller doesn't provide a timeout, it should default to 5. Print "Scanning port <port> with timeout <timeout>". Call it once with just a port, and once with both a port and a custom timeout.
def function_scan_port(port,timeout=5):
    print(f"Scanning port {port} with the timeout {timeout}")

function_scan_port(443)
function_scan_port(443,1) 
# Functions calling other functions
# 7. Write a function check_port_range(start, end) that loops from start to end, and for each port, calls your is_common_port() function from Q4 to decide whether to print "<port> - common" or "<port> - uncommon".

def check_port_range(start,end):
    for port in range(start,end+1):
        if is_common_port(port):
            print(f"{port} is common")
        else:
            print(f"{port} is uncommon")
check_port_range(78,84)

# Functions + lists (major real-world pattern)
# 8. Write a function scan_ports(port_list) that takes a list of ports and loops through it, printing "Checking port: <port>" for each one. Call it with [21, 22, 80, 443].
def function_scan_ports(port_list):
    for port in port_list:
        print(f"Checking port: {port}")

port_list = [21, 22, 80, 443]
function_scan_ports(port_list)

# Practical mini-tool
# 9. Write a function login_attempt(username, password) that returns True if username == "admin" and password == "admin123", otherwise returns False. 
# Then write a loop that tries 3 different username/password pairs (you make them up) against this function, printing "Success" or "Failed" for each attempt.
def login_attempt(username, password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

attempts = [
    ("admin", "1234"),
    ("root", "toor"),
    ("admin", "admin123")
]

for username, password in attempts:
    result = login_attempt(username, password)
    if result:
        print(f"{username}:{password} -> Success")
    else:
        print(f"{username}:{password} -> Failed")  

# Bonus — multiple return values
# 10. Write a function port_stats(port_list) that takes a list of ports and returns two values: the count of ports, and the highest port number (hint: Python lets you return count, max_port and unpack both when calling).
# Take your time with these — functions are the biggest mental shift so far (thinking in terms of "input → process → output" as a reusable unit), so don't rush it.
def function_port_stats(port_list):
    print(len(port_list))
    print(max(port_list))
# port_list = [21, 22, 80, 443]
function_port_stats(port_list)

# anyother way

def function_port_stats(port_list):
    count = len(port_list)
    highest = max(port_list)
    return count, highest

total, highest_port = function_port_stats(port_list)
print(total)
print(highest_port)