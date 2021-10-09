# Longest Increasing Subsequence
# Send Feedback
# Given an array with N elements, you need to find the length of the longest subsequence in the given array such that all elements of the subsequence are sorted in strictly increasing order.
# Input Format
# The first line of input contains an integer N. The following line contains N space separated integers, that denote the value of elements of array.
# Output Format
# The first and only line of output contains the length of longest subsequence.
# Constraints
# 1 <= N <= 10^3
# Time Limit: 1 second
# Sample Input 1 :
# 6
# 5 4 11 1 16 8
# Sample Output 1 :
# 3
# Sample Output Explanation
# Length of longest subsequence is 3 i.e. (5,11,16) or (4,11,16).
# Sample Input 2 :
# 3
# 1 2 2
# Sample Output 2 :
# 2

from sys import stdin

def lis(arr): 
    storage = [None for i  range(n)]
    storage[0] = 1

    ans = 1

    for i in range(1, n):
        max = 1
        for j in range(i - 1, -1, -1):
            if(arr[j] < arr[i]):
                op = storage[j] + 1
                if(op > max):
                    max = op

        storage[i] = max
        if(max > ans):
            ans = max
    return ans
      

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))