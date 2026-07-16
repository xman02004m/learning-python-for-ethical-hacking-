# Basic if/elif/else

# Ask the user for a port number. If it's 80 or 443, print "Common web port". Otherwise, print "Non-standard port".
# Ask for a password's length (as a number). If it's less than 8, print "Weak". If it's between 8 and 12, print "Moderate". If it's more than 12, print "Strong".
# Ask the user to enter an HTTP status code (as int). If it's 200, print "OK". If it's 404, print "Not Found". If it's 500, print "Server Error". Otherwise print "Unknown status code".

port_number = int(input("Enter the port no. "))
if port_number == 80:
    print("commom web port")
elif port_number == 443:
    print("common web port")
else:
    print("Non-standaed port")


length = int(input("Enter your password length (as a numbers) "))
if length <  8:
    print("weak")
elif length >= 8 and length  <= 12:
    print("Moderate")
else:
    print("bro you are goated how can you remind that much password. ")


http_code = int(input("enter your http status code "))
if http_code == 200:
    print("ok")
elif http_code == 404:
    print("Not found ")
elif http_code == 500:
    print("Server error")
else:
    print("Unknow status code ")

# Multiple Conditions (and / or)
# 4. Ask for a username and password. If username is "admin" and password is "admin123", print "Login successful". Otherwise print "Access denied".
# 5. Ask for a port number. If it's less than 1024 or greater than 65535, print "Invalid or reserved port". Otherwise print "Valid port".
username = input("Enter your username name ")
password = input("Enter your password ")
if username == 'admin' and password =='admin123':
    print("Login successful")
else:
    print("Login unsuccessful")

port = int(input("Enter a port number :- "))
if port < 1024 and port > 65535:
    print("Invalid or reserved port ")
else:
    print("Valid Port ")

# Nested/Chained Logic
# 6. Ask for the number of failed login attempts. If attempts is 3 or more and it's been less than 10 minutes since the last attempt (just ask for minutes as input too), print "Account locked". Otherwise print "Login allowed".
# 7. Ask for an IP address's first number (just the first octet, as int, e.g. from "192" type in 192). If it's 10, 172, or 192, print "Likely private IP". Otherwise print "Likely public IP".
# Practical Security Scenario
# 8. Write a simple "firewall rule checker": ask the user for a port number. If port is 22, print "SSH - allow only from trusted IP". If port is 80 or 443, print "Web traffic - allow". If port is 3389, print "RDP - block, high risk". Otherwise print "Unknown port - flag for review".
# 9. Ask the user to enter a file extension (like "exe", "pdf", "txt"). If it's "exe" or "bat", print "Potentially dangerous file type". Otherwise print "Likely safe file type".
# Bonus — Logic Puzzle
# 10. Ask for two numbers. Without using max(), write if/elif/else logic to print which one is larger, or print "Equal" if they're the same.
# Try these out and send your code when ready.