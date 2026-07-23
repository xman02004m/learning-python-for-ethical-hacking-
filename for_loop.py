# Basics — range()

# Print numbers 1 to 10 using a for loop and range().
# Print numbers 10 down to 1 (countdown) using for and range() (hint: range() can take a negative step).
# Print only even numbers from 1 to 20 using for and range() (hint: range(start, stop, step)).
for x in range(1,11):
    print(x)

for i in range(10, 0 ,-1):
    print(i)

for v in range(0 ,21 , 2):
    print(v)

# Looping over lists (this is huge for security scripting)
# 4. Create a list of common ports: [21, 22, 23, 25, 80, 443]. Loop through it and print "Checking port: <port>" for each one.
# 5. Create a list of usernames: ["admin", "root", "test", "guest"]. Loop through and print each one with the message "Trying username: <name>".
# 6. Given a list of IP addresses (make one up, like ["192.168.1.1", "192.168.1.2", "10.0.0.5"]), loop through and print each one.

ports = [21, 22, 23, 25, 80, 443]

for port in ports:
    print(f"checking port: {port}")

usernames = ["admin", "root", "test", "guest"]

for username in usernames:
    print(f"Typing username: {username}")

IP_addresses = ["192.168.1.1.", "198.168.1.2", "10.0.0.5"]
for IP_address in IP_addresses:
    print(IP_address)

# Combining for with if (this is where real scanning logic starts)
# 7. Loop through the port list from Q4. For each port, if it's 22, 80, or 443, print "<port> - common port". Otherwise print "<port> - uncommon port".
# 8. Loop through numbers 1 to 20. Print only the numbers divisible by 3 and 5 at the same time (hint: % and and).
for port in ports:
    if port == 22 or port == 80 or port == 443:
        print(f"{port} - Common port")
    else:
        print(f"{port} - Uncommon port")

for m in range(1,21):
    if m % 3 == 0 and m % 5 == 0:
        print(m)
# enumerate() — useful for numbering results
# 9. Loop through the ports list from Q4 using enumerate(), and print like: "1: Checking port 21", "2: Checking port 22", etc.

for  index, port in enumerate(ports ):
    print(f"{index +1}: Checking port {port} ")



# Practical mini-simulation
# 10. Simulate a very basic port scanner: loop through range(1, 11) (ports 1–10). For each port, print "Port <n>: OPEN" if the port number is even, otherwise print "Port <n>: CLOSED".
for porting in range(1,11):
    if porting % 2 == 0:
        print(f"Port {porting}: OPEN")
    else:
        print(f"Port {porting}: CLOSE")

# Bonus — nested loops (skip if it feels too much right now)
#  11. Print a simple multiplication table from 1 to 5 using two nested for loops (outer loop = number, inner loop = multiplier 1–5).


