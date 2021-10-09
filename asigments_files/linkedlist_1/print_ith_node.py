# Print ith node
# Send Feedback
# For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.
#  Note :
# Assume that the Indexing for the singly linked list always starts from 0.

# If the given position 'i',  is greater than the length of the given singly linked list, then don't print anything.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line contains the value of 'i'. It denotes the position in the given singly linked list.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
# Output format :
# For each test case, print the node data at the 'i-th' position of the linked list(if exists).

# Output for every test case will be printed in a seperate line.
#  Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# i  >= 0
# Time Limit: 1sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3
# Sample Output 1 :
# 2
# Sample Input 2 :
# 2
# 3 4 5 2 6 1 9 -1
# 0
# 9 8 4 0 7 8 -1
# 3
# Sample Output 2 :
# 3
# 0

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printIthNode(head, i):
    count = 0
    value = ""
    if head == None:
        return ""
    else:
        while head is not None and head.data is not None:
            if count == i:
                value = head.data
                break
            count = count + 1
            head = head.next
        return value


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    i = int(stdin.readline().rstrip())
    print(printIthNode(head, i))

    t -= 1