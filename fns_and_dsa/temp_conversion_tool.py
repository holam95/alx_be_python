FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
temperature = float(input("Enter the temperature to convert:"))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): " )
    
if scale == 'F':
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is equal to {celsius:.2f}°C.")
elif scale == 'C':
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F.")
else:
    print("Error Invalid temperature. Please enter a numeric value.")

