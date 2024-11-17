import math

#determine radius and PI values
r = float(input("Enter radius: ")) #promien
pi = math.pi

#calculate area
area = pi * r ** 2 #pole

#calculate circumference
circumference = 2 * pi * r #obwod

# print results
print(f"Radius: {r}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")
