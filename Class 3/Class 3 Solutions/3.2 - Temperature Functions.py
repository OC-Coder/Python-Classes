#(a) Fahrenheit to Celcius
#Defines a function that takes one variable as input
def f_to_c(temp):
	#Formula: C = (5/9) (F - 32)
	return (5/9) * (temp - 32)

#(b) Celcius to Fahrenheit
#Defines a function that takes one variable as input
def c_to_f(temp):
	#Formula: F = (9/5) C + 32
	return (9/5) * temp + 32

#(c) Fahrenheit to Kelvin
#Defines a function that takes one variable as input
def f_to_k(temp):
	#Formula: C = (5/9) (F - 32)
	#Formula: K = C + 273
	#Therefore, K = (5/9) (F - 32) + 273
	return (5/9) * (temp - 32) + 273

#(d) Kelvin to Fahrenheit
#Defines a function that takes one variable as input
def k_to_f(temp):
	#Formula: F = (9/5) C + 32
	#Formula: C = K - 273
	#Therefore, F = (9/5) (K - 273) + 32
	return (9/5) * (temp - 273) + 32

#(c) by calling (a)
#Defines a function that takes one variable as input
def f_to_k_with_a(temp):
	#Convert from F to C, and then to K
	return f_to_c(temp) + 273

#(d) by calling (b)
#Defines a function that takes one variable as input
def k_to_f_with_b(temp):
	#Convert from K to C, and then to F
	return c_to_f(temp - 273)

temp_f = 32
temp_c = 0
temp_k = 273
print(f_to_c(temp_f)) #Prints 0.0
print(c_to_f(temp_c)) #Prints 32.0
print(f_to_k(temp_f)) #Prints 273.0
print(k_to_f(temp_k)) #Prints 32.0
print(f_to_k_with_a(temp_f)) #Prints 273.0
print(k_to_f_with_b(temp_k)) #Prints 32.0