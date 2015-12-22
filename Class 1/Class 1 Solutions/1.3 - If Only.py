"""Write a program that takes two numbers as input, and prints “True”
if the first is larger than the second and their sum is divisible by either 2 or 3,
and “False” otherwise."""

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
print(a > b and ((a + b) % 2 == 0 or (a + b) % 3 == 0))
