def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


num = int(input("Enter a number: "))

result = check_number(num)

print("The number is:", result)
