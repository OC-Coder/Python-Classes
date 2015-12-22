"""2.	Write a program that takes the temperature in Fahrenheit as input,
and prints the temperature in Celsius and the temperature in Kelvin.
If you don’t know the equations, look them up online. """

#Input the temperature in Fahrenheit
f = int(input("Enter the temperature in Fahrenheit: "))

#Convert to Celsius and print
c = (f-32)*5/9
print("The temperature in Celsius is: " + str(c))

#Convert to Kelvin and print
k = c + 273
#Alternatively: k = ((f-32)*5/9)+273
print("The temperature in Kelvin is: " + str(k))
