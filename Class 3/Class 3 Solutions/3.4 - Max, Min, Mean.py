def max_num(nums):
    #Keep track of what the largest number so far is
    maxN = nums[0]
    for n in nums:
        #If the number we're currently looking is greater than the largest number so far,
        #then the largest number so far must be changed to the current number
        if n > maxN:
            maxN = n
    return maxN

def min_num(nums):
    minN = nums[0]
    for n in nums:
        #Do the same as max_num, except use < to keep track of the lowest number so far
        if n < minN:
            minN = n
    return minN

def avg(nums):
    #Calculates the sum of all of the numbers in the list
    cumulative_sum = 0
    for n in nums:
        cumulative_sum += n
    #The average is just the sum divided by the number of numbers
    return cumulative_sum / len(nums)

#Testing
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 0]
print(max_num(list)) #Prints 9
print(min_num(list)) #Prints 0
print(avg(list))     #Prints 3.6