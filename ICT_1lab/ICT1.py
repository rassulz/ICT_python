temp = float(input("Enter the temperature: "))
conversion = input("Convert to (C for Celsius, F for Fahrenheit): ").strip().upper()

if conversion == 'C':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp} Fahrenheit is {converted_temp:.2f} Celsius.")
elif conversion == 'F':
    converted_temp = temp * 9/5 + 32
    print(f"{temp} Celsius is {converted_temp:.2f} Fahrenheit.")
else:
    print("Invalid conversion option. Please enter 'C' or 'F'.")
