height = input("Enter your height: ")
weight = input("Enter your weight: ")
bmi = float(weight) / float(height) ** 2
print("The body mass index (BMI) is " + str(round(bmi,2)))