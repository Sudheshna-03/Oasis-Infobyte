def calculate_BMI(w,h):
    bmi = w/(h**2)
    return bmi


def check_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:5
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator: ")
    print("Please enter your weight (in kilograms):")
    weight = float(input())
    print("Please enter your height (in meters):")
    height = float(input())

    bmi = calculate_BMI(weight, height)
    category = check_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == "__main__":
    main()
