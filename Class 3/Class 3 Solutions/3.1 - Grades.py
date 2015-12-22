#Defines a function called letter_grade that takes one variable as input
def letter_grade(grade):
	if grade >= 90:
		return "A"
	elif grade >= 80:
		#No need to check whether grade < 90, since if it wasn't the first if statement would have been called
		return "B"
	elif grade >= 70:
		#Same as above. Elif is only called if everything before wasn't
		return "C"
	elif grade >= 60:
		return "D"
	else:
		#All other choices values of grade give an F
		return "F"

#Examples of how to call letter_grade
print(letter_grade(90)) #Prints A
print(letter_grade(89)) #Prints B
print(letter_grade(42)) #Prints F