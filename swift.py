# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Enter SWIFT code: ')

bank_code = swift[:4]  # pierwsze 4 znaki dla bank code
country_code = swift[4:6]  # dwa nastepne znaki dla country code
location_code = swift[6:8]  # dwa nastepne dla location code
branch_code = swift[8:11]  # ostatnie 3 dla branch code

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')
print(f'Location Code: {location_code}')
print(f'Branch Code: {branch_code}')
