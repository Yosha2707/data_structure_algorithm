# Check Palindrome (recursive)
# Send Feedback
# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false


def palindrome(string, start, end):
    if start >= end:
        return string
    lip = list(string)
    lip[start], lip[end] = lip[end], lip[start]
    string = "".join(lip)
    return palindrome(string, start + 1, end - 1)

    
n = input()
result = palindrome(n , 0 , len(n) - 1)
print("true") if result == n else print("false")