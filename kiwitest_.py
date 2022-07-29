from random import randint, random
import numpy as np
from quickSort import quickSort, splitData
from time import time
import pytest
 
#averagecase= [randint(1,10000) for _ in range(1000)]
#bestcase= sorted(averagecase)
#worstcase= sorted(averagecase, reverse=True)

bestcase = np.sort(np.copy(splitData))
averagecase = splitData
worstcase = bestcase[::-1]
 
def test_bubbleWorst():
    start= time()
    assert np.array_equal(quickSort(0,len(worstcase)-1,np.copy(worstcase)) == bestcase)
    print(time()-start)
 
def test_bubbleBest():
    start= time()
    assert np.array_equal(quickSort(0,len(bestcase)-1,np.copy(bestcase)) == bestcase)
    print(time()-start)
    
def test_bubbleAvg():
    start= time()
    assert np.array_equal(quickSort(0,len(averagecase)-1,np.copy(averagecase)) == bestcase)
    print(time()-start)