class multiFunction:
    def __init__(self, subfields=None):
        # Initialize subfields for listing AI subfields
        self.subfields = subfields if subfields else []

    def list_subfields_in_ai(self):
        if not self.subfields:
            print("No subfields available!")
            return []
        for subfield in self.subfields:
            print(subfield)
        return self.subfields

    @staticmethod
    def OddEven():
        try:
            number = int(input("Enter a number to check if it's odd or even: "))
            if number % 2 == 0:
                print("The number is even")
                return "The number is even"
            else:
                print("The number is odd")
                return "The number is odd"
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            return "Invalid input"

    @staticmethod
    def Elegible():
        try:
            # Get user input for gender and age
            gender = input("Enter your gender (male/female): ").strip().lower()
            age = int(input("Enter your age: "))

            # Check eligibility based on gender and age
            if gender == "male" and age >= 21:
                print("Eligible for marriage")
                return "Eligible for marriage"
            elif gender == "female" and age >= 18:
                print("Eligible for marriage")
                return "Eligible for marriage"
            else:
                print("Not eligible for marriage")
                return "Not eligible for marriage"
        except ValueError:
            print("Invalid input! Please enter a valid age.")
            return "Invalid input"

    @staticmethod
    def Percentage():
        try:
            # Collect marks for 5 subjects from the user
            marks = []
            for i in range(1, 6):
                subject_name = f"Subject {i}"
                mark = int(input(f"Enter marks for {subject_name}: "))
                marks.append(mark)

            # Calculate total and percentage
            total = sum(marks)
            percentage = total / len(marks)

            # Display the percentage and grade
            print(f"Percentage: {percentage}%")
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
        except ValueError:
            print("Invalid input! Please enter valid integers for marks.")

    @staticmethod
    def Area():
        try:
            # Get height and base as inputs
            height = float(input("Enter height of the triangle: "))
            base = float(input("Enter base of the triangle: "))

            # Calculate and print the area
            area = 0.5 * height * base
            print(f"Area of Triangle: {area}")
            print("Area Formula: (Height * Base) / 2")
            return area
        except ValueError:
            print("Invalid input! Please enter valid numbers for height and base.")
            return "Invalid input"

    @staticmethod
    def Perimeter():
        try:
            # Get height, base, and side as inputs
            height = float(input("Enter height of the triangle: "))
            base = float(input("Enter base of the triangle: "))
            side = float(input("Enter side of the triangle: "))

            # Calculate and print the perimeter
            perimeter = height + base + side
            print(f"Perimeter of Triangle: {perimeter}")
            print("Perimeter Formula: (Height + Base + Side)")
            return perimeter
        except ValueError:
            print(
                "Invalid input! Please enter valid numbers for height, base, and side."
            )
            return "Invalid input"

    @staticmethod
    def BMI():
        try:
            # Get weight and height from the user
            weight = float(input("Enter your weight in kilograms (e.g., 70): "))
            height = float(input("Enter your height in meters (e.g., 1.75): "))

            # Calculate BMI
            bmi = weight / (height**2)
            print(f"Your BMI is: {bmi:.2f} and you are: ", end="")

            # Determine BMI category
            if bmi < 16:
                print("severely underweight")
            elif bmi >= 16 and bmi < 18.5:
                print("underweight")
            elif bmi >= 18.5 and bmi < 25:
                print("healthy")
            elif bmi >= 25 and bmi < 30:
                print("overweight")
            elif bmi >= 30:
                print("severely overweight")
            else:
                print("Enter valid details")
        except ValueError:
            print("Invalid input! Please enter valid numbers for weight and height.")
