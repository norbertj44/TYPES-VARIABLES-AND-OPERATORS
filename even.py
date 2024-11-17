###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#

number = int(input('Enter number: '))
even = number%2==0 #procent to reszta (remainder) #==0sprawdza czy reszta z dzielenia liczby przez 2 wynosi 0 #sluzy do porownywania dwoch wartosci lub wyrazen aby sprawdzic czy są rowne

print(f'Number is even: {even}')