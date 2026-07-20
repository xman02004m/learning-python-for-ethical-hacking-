# Basics — getting the mental model

# Print a simple multiplication table from 1 to 5 (outer loop = number 1-5, inner loop = multiplier 1-5), formatted like "1 x 1 = 1".
# Print a pattern of stars like this using nested loops:

# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for x in range(1,11):
        print(f"{i} * {x} = {i*x}")

for nest in range (1,6):
    for nesting in range (nest):
        print("*", end="")
    print()
# Print numbers 1-3 in the outer loop, and for each, print 1-3 in the inner loop, like:

# Outer: 1
#   Inner: 1
#   Inner: 2
#   Inner: 3
# Outer: 2
#   Inner: 1
#   Inner: 2
#   Inner: 3
# Outer: 3
#   Inner: 1
#   Inner: 2
#   Inner: 3

for index, f in enumerate(range(1,4)):
    print(f"Outer:{index+1}")
    for vivek , w in enumerate(range(1,4)):
        print(f"Inner: {vivek + 1}")

# Security-flavored — this is the real payoff of nested loops
# 4. You have a list of IP addresses ["192.168.1.1", "192.168.1.2"] and a list of ports [22, 80, 443]. Use nested loops to print "Scanning <ip>:<port>" for every IP-port combination.
# 5. You have a list of usernames ["admin", "root"] and a list of passwords ["1234", "password", "admin123"]. Use nested loops to print "Trying <username>:<password>" for every combination (this is literally the core loop structure behind brute-force tools).
# 6. Same as Q5, but stop immediately using break once you find username == "admin" and password == "admin123" — print "Match found: admin:admin123" and don't try any more combinations. (Hint: break only exits the inner loop — you'll need a flag variable or extra logic to stop the outer loop too. Try it and see what happens first, then we'll talk about the fix if you get stuck.)

IP_addresses = ["192.168.1.1", "192.168.1.2"]
ports = [22, 80, 443]
for Ip_address in IP_addresses:
    for Port in ports:
        print(f"scanning: {Ip_address}:{Port}")

usernames = ["admin", "root"]
passwords = ["1234", "password", "admin123"]
for username in usernames:
    for password in passwords:
        print(f"Trying: {username}:{password}")

usernames = ["admin", "root"]
passwords = ["1234", "password", "admin123"]

found = False

for usernam in usernames:
    for passwor in passwords:
        print(f"Trying: {usernam}:{passwor}")
        if usernam == "admin" and passwor == "admin123":
            print(f"Match found: {usernam}:{passwor}")
            found = True
            break
    if found:
        break



# Bonus — counting with nested loops
# 7. Using nested loops, count and print how many total combinations exist between a list of 3 IPs and a list of 4 ports (without just multiplying 3×4 directly — actually count using a counter variable incremented inside the inner loop).

# IP  = ["192.168.1.1", "192.168.1.2", "192.0.1.1"]
# portes = [22, 80, 443, 24]
counter = 0
for Ips in range(3):
    for port in range(4):
        counter = counter + 1
    
print(f"final output is {counter}")