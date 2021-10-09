# Staircase
# Send Feedback
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
# Input format :
# Integer N
# Output Format :
# Integer W
# Constraints :
# 1 <= N <= 30
# Sample Input 1 :
# 4
# Sample Output 1 :
# 7
# Sample Input 2 :
# 5
# Sample Output 2 :
# 13

def calculate(n):
    if n < 3: 
        return n
    if n == 3:
        return 4

	return calculate(n - 1) + calculate(n - 2) + calculate(n - 3)

value = int(input())
print(calculate(value))