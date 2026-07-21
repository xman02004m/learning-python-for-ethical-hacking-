# Devised varied, challenging function practice questionsDevised varied, challenging function practice questionsGood instinct — more reps is the right move for functions since it's the biggest mental shift so far. Here's a fresh set, no repeats from before.
# Basics — different scenarios

# Write a function is_even(number) that returns True if a number is even, False if odd.
# Write a function square(number) that returns the number squared.
# Write a function celsius_to_fahrenheit(celsius) that returns the converted value (formula: F = C * 9/5 + 32).
def is_even(number):
    if number % 2 == 0:
        print("Ture")
    else:
        print("False")
is_even(2)
is_even(3)

def square(number):
    squared = number * number
    print(squared)
square(20)
square(16)

def celsius_to_farhrenheit(celsius):
    F = celsius * 9/5 + 32
    return F
print(celsius_to_farhrenheit(20))


# String-focused (useful for parsing later)
# 4. Write a function contains_admin(username) that returns True if the word "admin" appears anywhere in the given string, otherwise False (hint: use the in keyword — "admin" in username).
# 5. Write a function reverse_string(text) that returns the input string reversed (hint: text[::-1] works, or loop through it manually — try the manual way first for practice).
def contains_admin(username):
    if "admin" in username:
        return True
    else:
        return False
print(contains_admin("admin"))
print(contains_admin("superadmin123"))
print(contains_admin("Iamvivek"))

def reverse_string(text):
    # a=text[::-1]
    # return a
    for i in range(len(text) -1, -1, -1 ):
        # i = text [::-1]
        print(text[i] , end="")
reverse_string("name")

print(end="\n")

# this is for try
text ="python"
for a in reversed(text):
    print(a , end="")

# Multiple parameters + logic
# 6. Write a function is_valid_port(port) that returns True only if the port is between 1 and 65535 (inclusive), otherwise False.
# 7. Write a function check_login(username, password, correct_user, correct_pass) — instead of hardcoding "admin"/"admin123" like before, take the correct credentials as parameters too. Return True/False.
def is_valid_port(port):
    if port >= 1 and port <= 65535:
        return True
    else:
        return False
print(end="\n")
print(is_valid_port(-1))
print(is_valid_port(443))
print(is_valid_port(420))
print(is_valid_port(65555))

def check_login(username, password, correct_user, correct_pass):
    if username == correct_user and password == correct_pass:
        return True
    else:
        return False
    
print(check_login("admin", "admin123", "admin", "admin123"))   
print(check_login("root", "vivek", "admin", "admin123"))        
print(check_login("xman", "vivek123", "xman", "vivek123"))       


# Functions + loops together
# 8. Write a function count_common_ports(port_list) that takes a list of ports and returns how many of them are 22, 80, or 443 (a count, not True/False this time).
# 9. Write a function filter_valid_ports(port_list) that takes a list of ports and returns a new list containing only the ports that pass your is_valid_port() check from Q6 (hint: build an empty list, loop through, append valid ones).
def count_common_ports(port_list):
    for ports in port_list:
        ports = len(port_list)
        return ports
port_list = [22,80,443,-4578,0,24]
print(count_common_ports(port_list))

def filter_valid_ports(port_list):
    empty_list = []
    for ports in port_list:
        if is_valid_port(ports):
            empty_list.append(ports)
    return empty_list
print(filter_valid_ports(port_list))
# Slightly trickier — default + optional logic
# 10. Write a function generate_report(scanned_ports, verbose=False) — it should always print "Scan complete: X ports checked" (X = length of the list). But if verbose=True, it should also print each individual port in the list. Call it once with verbose=False and once with verbose=True.
def generate_report(scanned_ports, verbose=False):
    print(f"Scan complete: {len(scanned_ports)} ports checked")
    if verbose == True:
        for port in scanned_ports:
            print(port)

generate_report([22, 443, 80], False)
generate_report([22, 443, 80], True)

# Bonus — function returning a function's result to another function
# 11. Write a function average(numbers) that returns the average of a list of numbers. Then write a function describe_average(numbers) that calls average() and returns "High" if the average is above 50, "Low" otherwise.

def average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for num in numbers:
        total += num
    b = total / len(numbers)
    return b


def describe_average(numbers):
    avg = average(numbers)
    if avg > 50:
        return(f"{numbers}-> High")
    else:
        return(f"{numbers}-> low")

print(describe_average([45, 55, 60, 65, 75]))
print(describe_average([10,20,30,40,50]))