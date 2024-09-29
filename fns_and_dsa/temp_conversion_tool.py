# Create a script that defines functions to convert temperatures between Celsius and Fahrenheit
# Use global variables to store conversion factors that are accessible within functions.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    temperature = input("Enter the temperature to convert: ")
    if not temperature.replace('.', '', 1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temperature)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if unit == "c":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif unit == "f":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        print("Invalid unit. Please enter the value C or F.")


if __name__ == "__main__":
    main()