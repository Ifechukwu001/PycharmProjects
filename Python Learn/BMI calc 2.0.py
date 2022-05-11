# I am creating a BMI calculator 2.0.

user_weight = int(input("Enter your weight in Kg: "))
user_height = float(input("Enter your height in m: "))

BMI = user_weight / (user_height ** 2)
BMI_words = ""

if BMI < 18.5:
    BMI_words = "Underweight"
elif BMI < 25:
    BMI_words = "Normal weight"
elif BMI < 30:
    BMI_words = "Overweight"
elif BMI < 35:
    BMI_words = "Obese"
else:
    BMI_words = "Clinically Obese"

print(f"Your BMI is {round(BMI)},you are diagnosed {BMI_words}")