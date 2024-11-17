###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = float(input('Enter Celsius temperature: '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32
print(f'temperature in velsius: [{kelvin}')
print(f'temperature in fahrenheit: {fahrenheit}')