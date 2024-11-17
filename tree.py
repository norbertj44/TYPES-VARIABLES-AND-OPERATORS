import math
circumference = float(input('Enter tree circumference in cm: ')) #circumference - obwod
diameter = circumference / 3.14 #diameter - srednica
put_down = diameter >= 50

#sprawdza czy srednica jest co najmniej 50 cm i wypisuje True lub False - z tresci zadania
print(f'Tree can be cut down: {put_down}')