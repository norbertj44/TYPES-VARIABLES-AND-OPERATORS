###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ').lower()
last = input('Enter last letter: ').lower()
first_letter_code = ord(first)
last_letter_code = ord(last)


number_of_letters = abs(last_letter_code - first_letter_code) -1
if first == last: #tu byl blad ze wyskakiwalo -1 zamiast 0 jak sie wpisywalo k i k
    number_of_letters = 0


print(f'Between {first.lower()} and {last.lower()} is {number_of_letters} letters')