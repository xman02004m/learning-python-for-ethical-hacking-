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

s1 = "198"
s2 = "168"
s3 = "1"
s4 = "1"
print(f"{s1}.{s2}.{s3}.{s4}")