def sentence(words):
	#This is very similar to getting the sum of numbers in a list, except you use + to concatenate strings instead
	sentence = ""
	for w in words:
		sentence += w + " " #Same as: sentence = sentence + w + " "
		#In this case, this concatenates w + " " to the end of sentence
	return sentence.strip() #.strip() takes off any extra spaces from either end of a string.  In this case, the one at the end

#Testing
print(sentence(["Hello", "World", "!"]) + "!") #Prints "Hello World !!" (Note that the extra space is gone)