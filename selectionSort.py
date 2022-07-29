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
