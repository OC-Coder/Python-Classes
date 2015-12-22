#This function takes two inputs: nums1 and nums2
def sum_lists(nums1, nums2):
	#Create a list to store the sum in
	sum_nums = []
	#Loops through len(nums1) times, having first i = 0, then i = 1, then i = 2, ... , and finally i = len(nums1) - 1.
	#This is useful for using i to access the lists by index, as shown below.
	for i in range(len(nums1)):
		#Sums the elements at matching positions inthe two lists, and appends the result to sum_nums
		sum_nums.append(nums1[i] + nums2[i])
	return sum_nums

def mult_lists(nums1, nums2):
	mult_nums = []
	for i in range(len(nums1)):
		#Only needed difference is the operator: * for multiplication
		mult_nums.append(nums1[i] * nums2[i])
	return mult_nums

def diff_lists(nums1, nums2):
	diff_nums = []
	for i in range(len(nums1)):
		#Only needed difference is the operator: - for subtraction
		diff_nums.append(nums1[i] - nums2[i])
	return diff_nums

def div_lists(nums1, nums2):
	div_nums = []
	for i in range(len(nums1)):
		#Only needed difference is the operator: / for division
		div_nums.append(nums1[i] / nums2[i])
	return div_nums

#Testing
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(sum_lists(list1, list2))  #Prints [5, 7, 9]
print(mult_lists(list1, list2)) #Prints [4, 10, 18]
print(diff_lists(list1, list2)) #Prints [-3, -3, -3]
print(div_lists(list1, list2))  #Prints [0.25, 0.4, 0.5]