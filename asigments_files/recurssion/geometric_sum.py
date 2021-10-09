# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# using recursion.
# Input format :
# Integer k
# Output format :
# Geometric sum (upto 5 decimal places)
# Constraints :
# 0 <= k <= 1000
# Sample Input 1 :
# 3
# Sample Output 1 :
# 1.87500
# Sample Input 2 :
# 4
# Sample Output 2 :
# 1.93750

def sumR(value, k):
    if value == 1 / (2 ** k):
        return value
    return sumR(value * (1/2), k) + value

k = int(input())
print(format(sumR(1, k), ".5f"))