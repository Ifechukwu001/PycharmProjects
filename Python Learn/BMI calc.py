# I am creating a BMI calculator.

user_weight = int(input("Enter your weight: "))
user_height = float(input("Enter your height: "))

BMI = user_weight / (user_height ** 2)

result = int(BMI)

print(result)
