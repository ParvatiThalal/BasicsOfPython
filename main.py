
#  1 -  Write a program which will find all such numbers which are divisible by 7 but are not a
#       multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed


# Giving range between 2000 to 3200

Range = range(2000,3200)
Numbers = ""
#Looping in Range

for i in Range:
    if i%7==0 and i%5 !=0:
            Numbers = Numbers+str(i)+","
print(Numbers)


# 2 - Write a Python program to accept the user's first and last name and then getting them
#     printed in the the reverse order with a space between first name and last name.

fullname = input("What is your first name?") + " " + input("What is your last name?")
fullname = fullname[::-1]
print(fullname)

# 3 - Write a Python program to find the volume of a sphere with diameter 12 cm.

diameter = 12
radius = diameter/2

volume = round(4/3*3.14*(radius**3),2)
print(volume)