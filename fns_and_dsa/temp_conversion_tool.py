
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Ask the user for temperature value
        temp = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
        
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
    except ValueError as e:
        print(f"Invalid temperature. {e}")

if __name__ == "__main__":
    main()
