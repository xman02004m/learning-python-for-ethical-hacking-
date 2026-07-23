# Variables

# Store your name, age, and favorite hacking tool in three variables, then print a sentence using all three.
# Create variables for ip_address, port, and protocol, then print them as "Scanning 192.168.1.1 on port 80 using TCP".
# Swap the values of two variables var_a and var_b without using a third variable.

name = "Vivek kumar mishra"
age = 22
hacking_tool = "I do'nt know"

print(f"I am {name}. My age is {age}. {hacking_tool} what is like to use hacking.")

ip_address = "192.168.1.1"
port = 80
protocol = "TCP"

print(f"Scanning {ip_address} on port {port} using {protocol}.")

var_a = 2
var_b = 5
var_a, var_b = var_b, var_a
print (f"{var_a}\n{var_b}")

# 4. Take a port number as a string "443" and convert it to an integer, then check if it's greater than 1024.
# 5. A user enters their age as text via input — convert it to int and print whether they're eligible for something (age > 18).
# 6. Convert the float 3.99 to an int and explain out loud (or in a comment) what happens to the decimal part.
# 7. You have "192", "168", "1", "1" as four separate strings — convert and combine them into a single IP string 
# using string formatting (not casting to int, just realize why casting isn't needed here — trick question).

port = "443"
port2 =int(port)
if port2 > 1024:
    print("this is grater than 1024")
else :
    print("this is smaller than given port ")



user = input("Enter your age: ")
User1 = int(user)
if User1 < 18:
    print ("You can't drink ")
else:
    print("You can drink")

f1 = 3.99
# in this it is a float point number and I am using typecasting to convert it into float to int
f2 = int(f1)
print(f2)

s1 = "198"
s2 = "168"
s3 = "1"
s4 = "1"
print(f"{s1}.{s2}.{s3}.{s4}")

# 8. Write a script that asks the user to enter a target IP address and port, then prints 
# "Target set: <ip>:<port>".
# 9. Ask the user for a password, then print its length using len().
# 10. Ask the user for two numbers (they'll come in as strings), cast them to int,
#  and print their sum — this simulates parsing numeric input from a log file or user prompt.
# 11. Ask the user to enter "yes" or "no" for "Do you want to start the scan?" — 
# print a different message depending on their answer (no if/else needed yet, just print based on 
# comparison practice... actually try it with a simple if, even before we've formally covered 
# it, and see if you can figure out the syntax).

target_ip = input("Enter the traget ip address ")
port3 = input("Enter the port: ")
print(f"Traget set: {target_ip}:{port3}")

password = input("Enter your password: ")
length = len(password)
print(length)

a1 = input("Enter a no. ")
a2 = input("Enter a no. ")
a3= int(a1)
a4 = int(a2)
print(a3+a4)

a = input("enter yes or no for Do you want to start the scan?")

if a == "yes":
    print("start scanning")
else:
    print("write yes to start scanning motherfucker")


