import math

h=(input("Enter your height in meters "))
h = h.replace(",", ".")
h_2=float(h)

d = 3.57 * math.sqrt(h_2)
print(d)