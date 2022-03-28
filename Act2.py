number1 = 7
number2 = 4
number3 = 9

if number1 < number2:
    if number1 < number3:
        min_value = number1
    else:
        min_value = number3
elif number2 < number3:
    min_value = number2
else:
    min_value = number3

print(min_value)