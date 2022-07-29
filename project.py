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
#This creates the data for the array to plot on the x axis 
xValues = [0]*len(splitData)
for i in range(len(splitData)):
    xValues[i] = i 


### ------- BUBBLE SORT METHOD ------- ###

#bubble sort function 
def bubbleSort(nums):
    #internal loop that does swapping, each pass goes throgh this loop
    for i in range(len(nums)-1,0,-1):
        #external loop that checks the number of elements you have
        for j in range(i):
            #check in numbers are neede to be swapped
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums 

#nums= [5, 3, 8, 6, 7, 2]
#bubbleSort(splitData)

#print (splitData)






### ------- SELECTION SORT METHOD ------- ###

#seclection sort function 
def sort(nums):
    #find min value from the low index to high index - low will be 0 high will 5 
    for i in range (len(nums)):  
        #variable that will hold the min position
        minpos = i
        #make the array range smaller
        for j in range(i +1 ,len(nums)):
            if nums[j] <nums[minpos]:
                minpos = j
                
                
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        
    return nums
        #print (splitData)
 
 
 
 
#nums= [5, 3, 8, 6, 7, 2]
#sort(nums)

#print (nums)





# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
'''
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
 '''




# sortedBubble = np.copy(splitData)
# sortedBubble = bubbleSort(sortedBubble)
# print(sortedBubble)

# selectionsort = np.copy(splitData)
# selectionsort = sort(selectionsort)
# print(selectionsort)



#copy data loaded from the imported data and store  in sorted buble
sortedBubble = np.copy(splitData)
#starts the time for the function 
startTime = time.time()
sortedBubble = bubbleSort(sortedBubble)
#ends the time recording
endTime = time.time()
#stores recored time into bubbleSortTime
bubbleSortTime = endTime - startTime
#prints out the text and rounds up to 2 decimal points
print('Time Taken to sort the data: '+ str(np.round(bubbleSortTime,2))+' seconds')
#prints out the sorted list 
print(sortedBubble)


#copy data loaded from the imported data and store in selectionSort
selectionSort = np.copy(splitData)
#starts the time for the function
startTime = time.time()
selectionSort = sort(selectionSort)
#ends the time recording
endTime = time.time()
#stores recored time into bubbleSortTime
selectionSortTime = endTime - startTime
#prints out the text and rounds up to 2 decimal points
print('Time Taken to sort the data: '+ str(np.round(selectionSortTime,2))+' seconds')
#prints out the sorted list 
print(selectionSort)


#copy data loaded from the imported data and store  in sorted buble
sortedMerge = np.copy(splitData)
#starts the time for the function 
startTime = time.time()
sortedMerge = mergeSort(sortedMerge)
#ends the time recording
endTime = time.time()
#stores recored time into bubbleSortTime
sortedMergeTime = endTime - startTime
#prints out the text and rounds up to 2 decimal points
print('Time Taken to sort the data: '+ str(np.round(sortedMergeTime,2))+' seconds')
#prints out the sorted list 
print(sortedMerge)


'''
#Used to plot the sorted data into a scatter graph 
#Puts a title on the grapgh
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(selectionSort),max(selectionSort),0.5))
#sets graph type and sets the xValues
plt.scatter(xValues, selectionSort)
#shows created grapgh in a new window
plt.show()
'''

#Used to plot unsorted data into the scatter graph
#Puts a title on the grapgh
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(splitData),max(splitData),0.5))
#sets graph type and sets the xValues 
plt.scatter(xValues, splitData)
#shows created grapgh in a new window 
plt.show()