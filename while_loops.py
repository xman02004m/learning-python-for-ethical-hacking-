# Basic while loops

# Print numbers from 1 to 10 using a while loop.
# Print numbers from 10 down to 1 (countdown) using a while loop.
# Ask the user to enter a number. Keep printing "Scanning..." that many times using a while loop.
n = 1
while n <= 10:
    print(n)
    n = n + 1

num = 10 
while num >= 1:
    print(num)
    num = num - 1

count = int(input("Enter a number: "))
i = 0
while i < count:
    print("Scanning...")
    i = i + 1

# Loop with condition checking (this is the real use case)
# 4. Simulate a login system: ask the user for a password in a while loop. Keep asking until they type the correct password ("admin123"). Once correct, print "Access granted".
# 5. Simulate a brute-force limiter: start attempts = 0. Keep asking for a password in a loop. Each wrong attempt increases attempts by 1. If attempts reaches 3, print "Account locked" and stop asking (even if they never got it right).

password = ""
while  password != "admin123":
   password = input("Enter your password ")
print("Access granted")

attempts = 0
password1 = ""
while attempts <= 3:
    attempts = attempts + 1
    password = (input(f"enter your password "))

print("Account locked")
    


# Port scanning style (this is where it gets fun)
# 6. Start at port = 1. Using a while loop, print "Checking port 1", "Checking port 2" ... up to "Checking port 10".
# 7. Same as above, but only print the port number if it's even (hint: you'll need an if check inside the loop).
port = 1
while port <= 10 :
    print(f"checking port {port}.....")
    port = port +1

port1 = 1
while port1 <= 10:
    if port1 % 2 == 0:
        print(f"Checking port {port1}.....")
    
    port1 = port1 + 1
    



# Infinite loop control (important safety concept)
# 8. Write a while True: loop that keeps asking the user to enter a command. If they type "exit", break out of the loop using break. Otherwise just print whatever they typed.

food = ""
while food != "exit":
    food = input(f"Your enter food {food}. type exit to end the program    ")
print("bye")
# Bonus — combining what you know

# 9. Simulate a simple retry system: ask the user to enter a number between 1 and 10. If it's outside that range, keep asking again (loop) until they give a valid number, then print "Valid number: X".
num1 = 11
while num1 >= 11:
    num1 = int(input("Give a valid number b/w 1 to 10 "))
print(f"Valid number{num1}")







 # A tip since you said you tend to quit around here: the #1 thing that breaks people on while loops is forgetting to update the variable that controls the loop — causing an infinite loop that hangs. If your terminal freezes, that's almost always why. Don't panic — just Ctrl+C to stop it, check your loop variable, and fix it. It happens to everyone.