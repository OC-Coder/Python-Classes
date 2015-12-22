"""Write a four-function calculator program that takes in a number,
an operation (“+”, “-“, “x”, or “/”), and then a second number,
and prints out the result."""

#Float is used to allow for inputs like 1.23+4.56 (Using int would make that 1+4)
#Input first number
a = float(input("Enter the first number: "))

#Input operation
b = input("Enter the operation (+, -, x, or /): ")

#Input second number
c = float(input("Enter the second number: "))

#Calculate and print the result
"""Note: the way Python handles floats sometimes causes results like
1.23+4.56=5.789999999999999 instead of 5.79"""
if b == '+':
    print(str(a + c))
elif b == '-':
    print(str(a - c))
elif b == 'x':
    print(str(a * c))
elif b == '/':
    print(str(a / c))
