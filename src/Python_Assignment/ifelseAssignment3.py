# print 'CORRECT' if i==10 else 'INCORRECT'
i = int(input("Enter a Value: "))
print("CORRECT" if i == 10 else "INCORRECT")

# check the password, using if else statement
password = input("Enter the password: ")
if password == "Hope@123":
    print("Your Password is correct")
else:
    print("Your Password is incorrect")

# catagory the people by their age like child, adult, citizen, senior citizen
age = int(input("Enter your age: "))
if age < 18:
    print("You are a Child")
elif age < 35:
    print("You are an Adult")
elif age > 70:
    print("You are a Senior Citizen")
else:
    print("You are a Citizen")

# Finf whether the given number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("The given number is Positive")
else:
    print("The given number is Negative")

# check Whether the give number is divisible by 5 or not
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("The given number is Divisible by 5")
else:
    print("The given number is not Divisible by 5")
