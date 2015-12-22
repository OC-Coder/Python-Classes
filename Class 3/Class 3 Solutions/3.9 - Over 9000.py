"""
The following is copied from the solution to exercise 3.4
"""

def min_num(nums):
    minN = nums[0]
    for n in nums:
        if n < minN:
            minN = n
    return minN

"""
End of copied code
"""

def over_9000(nums):
	#We can use min_num to find the minumum number in the list
	#If that number is over 9000, then every other number must be
	#So, we only need to loop until min_num returns something over 9000
	while min_num(nums) <= 9000:
		#Adds 1 to every number in the list
		for i in range(len(nums)):
			nums[i] += 1
	return nums

#Testing
print(over_9000([1, 2, 3])) #Prints [9001, 9002, 9003]