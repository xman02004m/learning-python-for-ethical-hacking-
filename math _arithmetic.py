# Here's a set covering Python arithmetic and math essentials — again themed toward security use cases so it sticks.

# **Basic Arithmetic**
# 1. Write a script that takes two numbers as input, then prints their sum, difference, product, and quotient.
# 2. A scan takes 45 seconds per port. Given a number of ports (as input), calculate and print total scan time.
# 3. Print the result of `17 // 5` and `17 % 5` separately — then explain in a comment what each operator actually does (this matters a lot for security scripting — subnetting, chunking data, etc.)

a = int(input("Enter a no. "))
b = int(input("Enter a no. again "))
add = a + b
diff = a - b
mil = a*b
divi = a/b
print(add)
print(diff)
print(mil)
print(divi)


port = int(input("Give the number of port that you need to get the time of :- "))
a1 = port * 45
print(a1)

print(17 // 5)
# this operater is use for the round in output into the nearest whole interger for ex = if the output is 3.45
# this will convert it into 3
print(17 % 5)
# this operater give us the reminder for ex = we div the 17 with 5 then reminder is 2 that is the 
# output of the script


# **Operator Precedence**
# 4. Without running it first, predict the output of `10 + 5 * 2 - 3 / 3`, then run it and check if you were right.
# 5. Use parentheses to force `10 + 5` to be calculated before multiplying by `2`, and print the result.

# output is 19 
print(10+5*2-3/3)

print((10*5)+2)

# **Exponents & Roots**
# 6. Print `2 ** 10` (this is how you'd calculate max values for byte ranges — e.g. why a byte can hold 0–255).
# 7. Calculate the square root of `144` using `**` (hint: `0.5` power) — don't import `math` yet.
print(2 ** 10)

print (144 ** 0.5)
# **Practical Security-Flavored Problems**
# 8. A subnet mask allows `254` usable hosts. If you have `3` subnets, calculate and print total usable hosts.
# 9. Given a file size in bytes (as input), convert and print it in KB (divide by 1024) and MB (divide by 1024²).
# 10. Write a script that takes a number of failed login attempts as input, and calculates how many minutes until the account unlocks if lockout time is `attempts * 2` minutes.
# 11. Given a starting port (e.g. `1000`) and an ending port (e.g. `1010`), calculate and print how many total ports are in that range (without listing them — just arithmetic, `end - start + 1`).
print(254*3)

b1= int(input("Enter your file size "))
print(b1 / 1024)
print(b1/ (1024 ** 2))

attempts = int(input("enter your fail number of attempts "))
print(f"this time remain {attempts *2}")

print(10000-9000+1)


# **Bonus — Order of Operations Trap**
# 12. Predict then verify: `2 + 3 ** 2 * 2` — what does Python actually compute first? Write your prediction as a comment before running it.
# output is 20
print(2+3**2*2)
# Try these and send me your code — same as before, I'll review and flag anything off.