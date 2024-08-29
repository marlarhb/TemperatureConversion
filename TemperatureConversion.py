degree = float(input("What temperature is it today?: "))
print("'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin.")
unit = input("What temperature unit is it?: ").lower()
print("To convert your unit to Celsius, type 'C'. To convert to Fahrenheit, type 'F'. To convert to Kelvin, type 'K'.")
goal_unit = input("To what unit would you like to convert to?: ").lower()

if goal_unit == 'c' and unit == 'f':
    result = (degree - 32) * 5/9
    print(f"{degree} degrees Fahrenheit equals to {round(result, 2)} degrees Celsius.")
elif goal_unit == 'c' and unit == 'k':
    result = degree - 273.15
    print(f"{degree} degrees Kelvin equals to {round(result, 2)} degrees Celsius.")
elif goal_unit == 'k' and unit == 'c':
    result = degree + 273.15
    print(f"{degree} degrees Celsius equals to {round(result, 2)} degrees Kelvin.")
elif goal_unit == 'k' and unit == 'f':
    result = (degree - 32) * 5/9 + 273.15
    print(f"{degree} degrees Fahrenheit equals to {round(result, 2)} degrees Kelvin.")
elif goal_unit == 'f' and unit == 'c':
    result = (degree * 9/5) + 32
    print(f"{degree} degrees Celsius equals to {round(result, 2)} degrees Fahrenheit.")
elif goal_unit == 'f' and unit == 'k':
    result = (degree - 273.15) * 9/5 + 32
    print(f"{degree} degrees Kelvin equals to {round(result, 2)} degrees Fahrenheit.")
