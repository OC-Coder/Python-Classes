"""Write a program that takes a number as input
and prints out whether that year is a leap year.
Leap years occur on every year that is a multiple of 400,
as well as years that are multiples of 4 but not multiples of 100."""

#Input the year
year = int(input("Enter the year: "))

#Divisible by 400
if year % 400 == 0:
    print(str(year) + " is a leap year.")
#Divisible by 4 but not 100
elif year % 4 == 0 and not year % 100 == 0:
    print(str(year) + " is a leap year.")
#Not a leap year
else:
    print(str(year) + " is not a leap year.")

"""Alternatively:
if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")"""
