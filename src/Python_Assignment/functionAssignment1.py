# create a class and function and list out the items in the list


class ListItSubfiledsInAI:
    def __init__(self, subfields):
        self.subfields = subfields

    def Subfields(self):
        for subfield in self.subfields:
            print(subfield)


subfields = [
    "Sub-Files in AI Are:",
    "Machine Learning",
    "Neural Networks",
    "Vision",
    "Robotics",
    "Search Processing",
    "NLP",
    "LLM",
    "AI Gents",
]
subfieldsList = ListItSubfiledsInAI(subfields)
subfieldsList.Subfields()


# create the class and function to check the input is odd or even
class OddEven:
    def __init__(self, number):
        self.number = number

    def OddEven(self):
        if self.number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")


number = int(input("Enter a number: "))
OddEven = OddEven(number)
OddEven.OddEven()

# create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female get the input gender and age


class EligibilityForMarriage:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def Elegible(self):
        if self.gender.lower() == "male" and self.age >= 21:
            print("Eligible for marriage")
        elif self.gender.lower() == "female" and self.age >= 18:
            print("Eligible for marriage")
        else:
            print("Not eligible for marriage")


gender = input("Enter your gender (male/female): ")
age = int(input("Enter your age: "))
eligibility = EligibilityForMarriage(gender, age)
eligibility.Elegible()


# create a class and function to check the percentage of marks by getting 5 marks as input and return the grade according to the percentage like if percentage >= 90 grade is A+ if percentage >= 80 grade is A and so on
class FindPercentage:
    def __init__(self, marks):
        self.marks = marks

    def Percentage(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        print("Percentage: ", percentage)
        if percentage >= 90:
            print("Grade: A+")
        elif percentage >= 80:
            print("Grade: A")
        elif percentage >= 70:
            print("Grade: B+")
        elif percentage >= 60:
            print("Grade: B")
        elif percentage >= 50:
            print("Grade: C+")
        elif percentage >= 40:
            print("Grade: C")
        else:
            print("Grade: F")


# Collect marks for 5 subjects from the user and store them in a list
marks = []
for i in range(1, 6):
    subject_name = f"Subject {i}"
    marks.append(int(input(f"Enter marks for {subject_name}: ")))

# Create an instance of FindPercentage and calculate the grade
Findpercentage = FindPercentage(marks)
Findpercentage.Percentage()


# print area and perimeter of a triange using class as triangle and function as triangle get the input from user height and base for area and hegiht, base and side for perimeter
class Triangle:
    def __init__(self, height, base, side):
        self.height = height
        self.base = base
        self.side = side

    def Area(self):
        area = 0.5 * self.height * self.base
        print("Area of Triangle: ", area)

    def Perimeter(self):
        perimeter = self.height + self.base + self.side
        print("Perimeter of a Triangle: ", perimeter)


height = int(input("Enter height of the triangle: "))
base = int(input("Enter base of the triangle: "))
triangle = Triangle(height, base, 0)
triangle.Area()
print("Area Formula: (Height * Base) / 2")
triangle.Area()
height = int(input("Enter height of the triangle: "))
base = int(input("Enter base of the triangle: "))
side = int(input("Enter side of the triangle: "))
print("Perimeter Formula: (Height + Base + Side)")
triangle = Triangle(height, base, side)
triangle.Perimeter()


# create a function to print list of Subfiles in AI
def SubfieldsInAI():
    subfields = [
        "Machine Learning",
        "Neural Networks",
        "Vision",
        "Robotics",
        "Search Processing",
        "NLP",
        "LLM",
        "AI Gents",
    ]
    for subfield in subfields:
        print(subfield)
