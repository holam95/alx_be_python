FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR
    
    

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR
    
    
Temp = int(input("Enter temperature 1 for Fahrenheit,2 for celcius: "))


if Temp == 1:
    Fah = int(input("Enter temperature in Fahrenheit: "))
    print("temp to celcius:", convert_to_celsius(Fah), "cel")

elif Temp == 2:
    cel = int(input("Enter temperature in celcius: "))
    print("temp to Fahrenheit: ", convert_to_fahrenheit(cel), "fah")

else:
    print("Invalid temperature. Please enter a numeric value.")
