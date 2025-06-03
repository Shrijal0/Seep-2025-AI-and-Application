# Function for converting between different length units
def length_conversion(): 
    print("\nLength Conversion:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")

    # Get the user's choice of conversion
    choice = input("Enter your choice: ")
    
    # Get the numeric value to convert
    value = float(input("Enter the value to convert: "))

    # Perform the appropriate conversion based on user input
    if choice == '1':
        # Convert meters to kilometers
        print(f"{value} meters = {round(value / 1000, 4)} kilometers")
    elif choice == '2':
        # Convert kilometers to meters
        print(f"{value} kilometers = {round(value * 1000, 4)} meters")
    elif choice == '3':
        # Convert miles to kilometers (1 mile = 1.60934 km)
        print(f"{value} miles = {round(value * 1.60934, 4)} kilometers")
    elif choice == '4':
        # Convert kilometers to miles
        print(f"{value} kilometers = {round(value / 1.60934, 4)} miles")
    else:
        print("Invalid choice!")


# Function for converting between temperature units
def temperature_conversion():   
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Get the user's choice
    choice = input("Enter your choice: ")
    
    # Get the temperature value to convert
    value = float(input("Enter the temperature value to convert: "))

    # Perform the chosen temperature conversion
    if choice == '1':
        # Convert Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
        print(f"{value} Celsius = {round((value * 9/5) + 32, 2)} Fahrenheit")
    elif choice == '2':
        # Convert Fahrenheit to Celsius: (°F − 32) × 5/9 = °C
        print(f"{value} Fahrenheit = {round((value - 32) * 5/9, 2)} Celsius")
    else:
        print("Invalid choice!")


# Function for converting between weight units
def weight_conversion():
    print("\nWeight Conversion:")     
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")

    # Get the user's choice
    choice = input("Enter your choice: ")
    
    # Get the weight value to convert
    value = float(input("Enter the weight value to convert: "))

    if choice == '1':
        # Convert kilograms to pounds (1 kg = 2.20462 lbs)
        print(f"{value} kilograms = {round(value * 2.20462, 4)} pounds")
    elif choice == '2':
        # Convert pounds to kilograms
        print(f"{value} pounds = {round(value / 2.20462, 4)} kilograms")
    else:
        print("Invalid choice!")


