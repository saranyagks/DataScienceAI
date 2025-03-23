# Taking weight and height input from the user
weight = float(input("Enter your weight in kilograms(e.g., 70):  "))
height = float(input("Enter your height in meters (e.g 1.75): "))
# calculate BMI
bmi = weight / (height**2)
print("Your BMI is: {0} and you are: ".format(bmi), end="")
# Conditions
if bmi < 16:
    print("severely underweight")

elif bmi >= 16 and bmi < 18.5:
    print("underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Healthy")

elif bmi >= 25 and bmi < 30:
    print("overweight")

elif bmi >= 30:
    print("severely overweight")
else:
    print("Enter valid details")
