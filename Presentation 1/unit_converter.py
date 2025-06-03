#Importing length_conversion, temperature_conversion, weight_conversion function from conversion.py
from conversion_module import length_conversion, temperature_conversion, weight_conversion

print("Welcome to the Unit Converter!")
print("Choose the type of conversion:")
print("1. Length")
print("2. Temperature")
print("3. Weight")

# Get the user's choice
choice = input("Enter your choice (1/2/3): ")

# Using functions according to the users choice
if choice == '1':
    # To convert length
    length_conversion()
elif choice == '2':
    # To convert temprature
    temperature_conversion()
elif choice == '3':
    # To convert weight
    weight_conversion()
else:
    print("Invalid choice! Please restart the program.")