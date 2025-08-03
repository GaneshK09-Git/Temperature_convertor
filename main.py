#Temperature conversion program

temp = float(input("Enter the temp: "))
unit= input("Enter the units of temp (f or c): ")
unit = unit.lower()

if unit == 'c':
    temp = round((9 * temp)/ 5 + 32, 1)
    print(f"The temp in Fahrenheit is: {temp} °F")  #alt + 0176 = °
elif unit == 'f':
    temp = round((temp - 32) * 5/ 9, 1)
    print(f"The temp in Celsius is: {temp} °C")
else:
    print("Invalid unit")


