# Area of a trapezoid 
# This program will ask the user for the deminsions of a trapezoid .
# It will then calculate the area for the user and display it .
print ("today we will calculate the area of a trapezoid")

# get base 1 from the user and convert it to an integer.
base1 =  float(input("Enter base 1 (cm): "))

# get base 2 from the user and convert it to an integer.
base2 =  float(input("Enter base 2 (cm): "))

# get height from the user and convert it to an integer.
height =  float(input("Enter height (cm): "))
# calculate the area of the trapezoid
area = ((base1 + base2) / 2) * height

# display the area
print("the area of a trapezoid with base 1 " + str(base1) + " cm and base 2 " + str(base2) + " cm and height " + str(height) + " cm is " + str(area) + " cm^2.")