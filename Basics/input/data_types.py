# asking for the Name
print("What is your name?")
name = input()
print()
# asking for the age
print("How old are you(in years)?")
age = int(input())
print()
# asking for the height
print("How tall are you(in metres)")
height = float(input())
print()
# asking for the weight
print("What is your weight(in kilograms)?")
weight = float(input())
print()
# Calculate the BMI
bmi = weight / (height**2)
print(name, "you are", age, "and your BMI is", bmi)