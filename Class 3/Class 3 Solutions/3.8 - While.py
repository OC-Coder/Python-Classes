#Only while forms of 3.3, 3.4, and 3.7 are provided. Do the rest yorself.

"""
3.3
"""
def num_even(nums):
    even = 0
    #Keep track of where we are in the list
    i = 0
    #Loop i is still in the bounds of the list (from 0 to len(nums) - 1)
    while i < len(nums):
        if nums[i] % 2 == 0:
            even += 1
        #Increase i to move on to the next number in the list
        i += 1
    return even

#This stays the same, as it uses num_even
def num_odd(nums):
    return len(nums) - num_even(nums)

#Testing
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
print(num_even(list)) #Prints 4
print(num_odd(list))  #Prints 6

"""
3.4
"""
def max_num(nums):
    #Do the same thing as above
    #No more comments from now on
    i = 0
    maxN = nums[0]
    while i < len(nums):
        if nums[i] > maxN:
            maxN = nums[i]
        i += 1
    return maxN

def min_num(nums):
    i = 0
    minN = nums[0]
    while i < len(nums):
        if nums[i] < minN:
            minN = nums[i]
        i += 1
    return minN

def avg(nums):
    i = 0
    cumulative_sum = 0
    while i < len(nums):
        cumulative_sum += nums[i]
        i += 1
    return cumulative_sum / len(nums)

#Testing
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
print(max_num(list)) #Prints 9
print(min_num(list)) #Prints 0
print(avg(list))     #Prints 3.6

"""
3.7
"""
def sentence(words):
	i = 0
	sentence = ""
	while i < len(words):
		sentence += words[i] + " "
		i += 1
	return sentence.strip()

#Testing
print(sentence(["Hello", "World", "!"]) + "!") #Prints "Hello World !!" (Note that the extra space is gone)