###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
password_bad = len(password) < 8
print(f'Is password length valid?: {password_ok}') #zmienilem pytanie poniewaz nie wiedzialem czy mam uzywac tuta if i else - nie ma tak w zadaniu


