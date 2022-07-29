
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



#copy data loaded from the imported data and store  in sorted buble
sortedBubble = np.copy(splitData)
#starts the time for the function 
startTime = time.time()
#calls function - assign sorted bubble to nums
sortedBubble = bubbleSort(sortedBubble)
#ends the time recording
endTime = time.time()
#stores recored time into bubbleSortTime
bubbleSortTime = endTime - startTime
#prints out the text and rounds up to 2 decimal points
print('Time Taken to sort the data: '+ str(np.round(bubbleSortTime,2))+' seconds')
#prints out the sorted list 
print(sortedBubble)