# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:28:07 2023

@author: krish
"""
import sys
import random
import tracemalloc
import time
import math

# 
# main function that implements introsort after choosing an appropriate depth limit based on the size of the given array
def introSort(arr):
    num = len(arr)
    depthLimit = 2 * math.floor(math.log2(num-1))
    return introSortHelper(arr, 0, num, depthLimit)


def introSortHelper(arr, begin, end, depthLimit):
    # function to help choose pivot based on median of three indicies
    # returns value from array based on median of three 
    def medianOf3(arr, low, mid, high):
        if (arr[low] - arr[mid]) * (arr[high] - arr[low]) >= 0:
            return arr[low]

        elif (arr[mid] - arr[low]) * (arr[high] - arr[mid]) >= 0:
            return arr[mid]

        else:
            return arr[high]

    # function from quicksort that partitions the array at the given pivot
    def partition(arr, low, high, pivot):
        i = low
        j = high
        while True:

            while (arr[i] < pivot):
                i += 1
            j -= 1
            while (pivot < arr[j]):
                j -= 1
            if i >= j:
                return i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Uses quicksort if array is smaller than 16 and depth limit of recursion has not been exceeded
    while(end - begin > 16):
        if depthLimit == 0:
            return heapSort(arr)
        depthLimit -= 1
        # calculates median to partition array at using median of threes
        median = medianOf3(arr, begin, begin +
                           ((end - begin) // 2) + 1, end - 1)
        # partitions the array at the chosen pivot
        p = partition(arr, begin, end, median)
        # recursive call to continue sorting array with helper function
        introSortHelper(arr, p, end, depthLimit)
        end = p

    # performs insertion sort on small arrays after enough recursions
    # or begins here if original array is small enough
    return insertionSort(arr, begin, end)

#classic insertion sort function for use with smaller arrays
def insertionSort(arr, begin=0, end=None):
    #sets end to length of array if no input parameter given
    if end == None:
        end = len(arr)
    # iterates through portion of array based on begin and end and sorts that portion
    for i in range(begin, end):
        j = i
        toChange = arr[i]
        while (j != begin and arr[j - 1] > toChange):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = toChange
    return arr

#classic heapsort function that contructs minheap and then removes smallest value one at a time to 
def heapSort(arr):
    num = len(arr)
    # calls MinHeap class
    minHeap = MinHeap(num)
    
    # constructs minheap object that maintains minheap invariant with minimum object at root
    for value in arr:
        minHeap.insert(value)
    arr = []
 
    # pops elements from heap one at a time and inserts into arr. 
    # result is sorted arr because minheap structure maintains invariant
 
    arr = arr + [minHeap.remove() for i in range(num)]
    return arr
 
 
 # class for minheap data structure to use heapsort function exactly copied from website
 # source: https://www.geeksforgeeks.org/min-heap-in-python/
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
   
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
 
#quicksort implementation from https://www.geeksforgeeks.org/quick-sort/ in order to compare running times
# Python3 implementation of QuickSort
# Function to find the partition position
def partition_qs(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
def quicksort(array):
    num = len(array)
    return quicksortHelper(array, 0, num-1)

# Function to perform quicksort
def quicksortHelper(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_qs(array, low, high)
 
        # Recursive call on the left of pivot
        quicksortHelper(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksortHelper(array, pi + 1, high)
 
 
def main():
    randomlist = []
    for i in range(0,1000):
        n = random.randint(1,1000)
        randomlist.append(n)

    #tracemalloc.start()
    #print(heapSort(randomlist))
    #print(tracemalloc.get_traced_memory())
    #tracemalloc.stop()
    
    #start_time = time.time()
    #arry = heapSort(randomlist)
    #end_time = time.time()
    #execution_time = end_time - start_time
    #print("Execution time:",execution_time)
    
    print(introSort(randomlist))

 
if __name__ == '__main__':
    main()