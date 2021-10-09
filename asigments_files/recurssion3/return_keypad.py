# Return Keypad
# Send Feedback
# Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important.
# Input Format :
# Integer n
# Output Format :
# All possible strings in different lines
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf


his = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
def keypad(n):
    if len(n) == 1:
        val = his[n]
        return list(val)
    
    data = keypad(n[1:])
    localVars = list(his[n[0]])
    
    result = []
    
    for i in data:
        for j in localVars:
            result.append(j + i)
    
    return result 
    

n = input()
ans = keypad(n)
for s in ans:
    print(s)