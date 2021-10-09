# Check AB
# Send Feedback
# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Input format :
# String S
# Output format :
# 'true' or 'false'
# Constraints :
# 1 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false

## Read input as specified in the question.
## Print output as specified in the question.

def stringFunc(value , s):
    length = len(value) - 1
    if s == length:
        return "true"
    
    if s == 0 and value[s] != "a":
        return "false"
    
    if value[s] == "a":
        if value[s + 1] != "a":
            if s + 2 <= length:
                if value[s + 1] != 'b' or value[s + 2] != 'b':
                    return "false"

    if value[s] == 'b' and value[s + 1] == 'b':
        if s + 1 < length and value[s + 2] != 'a':
            return "false"

    return stringFunc(value, s + 1)


val = str(input())
print(stringFunc(val, 0))