# Project1-Cmpsc-463
Implement hybrid sorting algorithm and analyze performance and use cases

## Objective
After researching different sorting algorithms and hybrid combinations, I settled on implementing Introsort or Introspective sort. The goal is to cement my understanding of sorting algorithms and understand good situations to use the different classic sorting algorithms.

## Introsort Description
Introsort uses three of the classic sorting algorithms: quicksort, heapsort, and mergesort. The average use of this algorithm isn't too different from quicksort except for the fact that the average and worst case time complexity is O(nlogn)

Even though quicksort and heapsort have O(nlogn) runtimes, with smaller sized lists they have too much overhead and asymptotic runtime is not needed, so insertion sort is used when size is less than 16 in the case of my implementation. Also after several recursions, once the input list becomes small enough, insertion sort is done rather than continuing to recurse. 

Generally quicksort is preferable to use over heapsort because of the constant factors hidden in the Big O runtime. Quicksort has on average O(nlogn) runtime but on rare occasions can have a worst case of O(n^2). On the otherhand, heapsort's worstcase runtime is O(nlogn). Introsort uses the advantages of both by using quicksort by default, but on the rare occasions that too many recursions are done, the algorithm switches to simply performing heapsort because of the guaranteed worst case time complexity of O(nlogn).

## Time Complexity Benchmark Testing
For testing time complexity I used the time library and plotted the array size vs time elapsed. I took the average time for 10 runs for each array size because there can be a lot of variability between runs because of resource usage within the computer and different kinds of luck based on the random list generated and the pivots chosen. The runtimes were similar for quicksort and introsort as I expected because the majority of introsort is using quicksort. Heapsort had the longest runtimes as expected due to constant factors that are ignored in asymptotic runtime.

## Space Complexity Benchmark Testing
For testing memory usage I used the tracemalloc library and plotted the array size vs memory usage. The experimental results did not match my expectations. I think this is because my implementation of heapsort and introsort are not optimal in terms of using the least amount of memory possible. Heapsort should have had the smallest memory usage but my implementation had the largest of the three algorithms compared.


## Sources
https://aquarchitect.github.io/swift-algorithm-club/Introsort/
https://www.geeksforgeeks.org/introsort-or-introspective-sort/
