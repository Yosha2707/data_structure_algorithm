# Pair Sum To 0
# Send Feedback
# Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
# Note: Array A can contain duplicate elements as well.
# Input format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output format :
# The first and only line of output contains the count of pair of elements in the array which sum up to 0. 
# Constraints :
# 0 <= N <= 10^4
# Time Limit: 1 sec


from sys import stdin

def pairSum0(arr,n):
    d = {}
    
    pairs = 0
    for i in arr:
        opp = i * -1
        if opp in d:
            pairs += d[opp]
            
        d[i] = d.get(i, 0) + 1
        
    return pairs 
            
            
        
    
    return pairs



    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))