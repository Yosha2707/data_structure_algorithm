# Merge Sort Code
# Send Feedback
# Sort an array A using Merge Sort.
# Change in the input array itself. So no need to return or print anything.
# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)
# Output format :
# Array elements in increasing order (separated by space)
# Constraints :
# 1 <= n <= 10^3
# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
# Sample Input 2 :
# 5
# 2 1 5 2 3
# Sample Output 2 :
# 1 2 2 3 5 

def mergeSort(arr):
    
    if len(arr) == 0 or len(arr) == 1:
        return
    
    mid = len(arr)//2
    a1 = arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)

def merge(a1,a2,arr):
    i = 0
    j = 0
    k = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = a2[j]
            j=j+1
            k=k+1
    while i < len(a1):
        arr[k] = a1[i]
        i=i+1
        k=k+1
    while j < len(a2):
        arr[k] = a2[j]
        j=j+1
        k=k+1
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
