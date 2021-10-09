# Minimum Number Of Squares
# Send Feedback
# A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the minimum number of squares that sum to n.
# Input format:
#  The first and only line of input contains an integer N (1 <= N <= 10000)
# Constraints:
#  Time Limit: 1 seconds
# Output format:
# The first and only line of output contains the minimum number if squares that sum to n.
# Sample Test Cases:
# Sample Input 1:
# 100
# Sample Output 1:
# 1
# Explanation:
# We can write 100 as 10^2 also, 100 can be written as (5^2) + (5^2) + (5^2) + (5^2), but this representation requires 4 squares. So, in this case, the expected answer would be 1, that is, 10^2.



import sys
import math
from sys import setrecursionlimit
setrecursionlimit(10**6)

def minStepsTo1(n, dp):
    if n == 0:
        return 0
    
    ans = sys.maxsize
    root = int(math.sqrt(n))
    
    for i in range(1, root + 1):
        if dp[n - (i ** 2)] == -1:
            smallans = minStepsTo1(n - (i ** 2), dp)
            currans = 1 + smallans
            dp[n - (i ** 2)] = smallans
        else:
            currans = 1 + dp[n - (i ** 2)]
        ans = min(currans, ans)
        
    return ans
    

        

    
n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minStepsTo1(n, dp)
print(ans)
