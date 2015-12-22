#If you know what vectors are, then you should recognize this as the dot product of two vectors
#If not, don't worry; it's a more advanced math thing that you don't need to know at all for Python
#(It is a convenient problem subject, though)

def dot_product(nums1, nums2):
	#Keep track of the sum so far
	cumulative_sum = 0;
	#Again, loop through the lists by index
	for i in range(len(nums1)):
		#Increase the cumulative sum by the product of the corresponding elements of the two lists
		#Careful: cumulative_sum = nums1[i] * nums2[i] won't work, since you're completely resetting cumulative_sum
		#		  to the product each time, instead of keeping track of the sum so far.
		cumulative_sum += nums1[i] * nums2[i] #Same as: cumulative_sum = cumulative_sum + (nums1[i] * nums2[i])
	return cumulative_sum

#Testing
print(dot_product([1, 2, 3], [4, 5, 6])) #Prints 32