"""Write a program that takes a number as input and prints out
whether it is even and whether it is divisible by 3. """

#Take a number as input
x = int(input())

#Even?
if x % 2 == 0:
    print("It is even.")
else:
    print("It is odd.")

#Divisible by 3?
if x % 3 == 0:
    print("It is divisible by 3.")
else:
    print("It is not divisible by 3.")
