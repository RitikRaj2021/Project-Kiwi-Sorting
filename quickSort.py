
### ------- Project Kiwi Sorting ------- ###

#importing numpy into 
import numpy as np
#importing time into code
import time
#import pyplot into the code 
import matplotlib.pyplot as plt

#open the kiwi data txt file
with open('kiwidata.txt') as file:  
    #read the text file 
    data = file.read()
#split the data by , and store in splitdata    
splitData = data.split(',')
splitData.remove('')

splitData = np.array(splitData).astype(np.float64)

# Quick sort in Python

 # function to find the partition position
def partition(array, low, high):

   # choose the rightmost element as pivot
   pivot = array[high]

   # pointer for greater element
   i = low - 1

   # traverse through all elements
   # compare each element with pivot
   for j in range(low, high):
     if array[j] <= pivot:
       # if element smaller than pivot is found
       # swap it with the greater element pointed by i
       i = i + 1

       # swapping element at i with element at j
       (array[i], array[j]) = (array[j], array[i])

   # swap the pivot element with the greater element specified by i
   (array[i + 1], array[high]) = (array[high], array[i + 1])

   # return the position from where partition is done
   return i + 1

 # function to perform quicksort
def quickSort(array, low, high):
   if low < high:

     # find pivot element such that
     # element smaller than pivot are on the left
     # element greater than pivot are on the right
     pi = partition(array, low, high)

     # recursive call on the left of pivot
     quickSort(array, low, pi - 1)

     # recursive call on the right of pivot
     quickSort(array, pi + 1, high)







'''
def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums
'''






#data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(splitData)

size = len(splitData)

quickSort(0, size - 1,splitData)

print('Sorted Array in Ascending Order:')
print(splitData)