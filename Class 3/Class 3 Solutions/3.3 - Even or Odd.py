def num_even(nums):
	#At first, we have seen no even numbers
    even = 0
    for n in nums:
    	#If the current number is divisible by 2, increase the number of even numbers we have so far by 1,
    	#as we have now seen one more even number
        if n % 2 == 0:
            even += 1 #Same as even = even + 1
    return even

def num_odd(nums):
	#All integers that aren't even are odd,  so we can just call num_even and substract that from the total length
    return len(nums) - num_even(nums)

#Testing
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
print(num_even(list)) #Prints 4
print(num_odd(list))  #Prints 6