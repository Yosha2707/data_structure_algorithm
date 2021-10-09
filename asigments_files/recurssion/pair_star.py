# Pair Star
# Send Feedback
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a

## Read input as specified in the question.
## Print output as specified in the question.

def newString(string, index):
    if index >= len(string)- 1: 
        return string[index]
    
    result = newString(string, index + 1)
    return string[index] + "*" + result if result[0] == string[index] else string[index] + result

n = input()
print(newString(n , 0))
