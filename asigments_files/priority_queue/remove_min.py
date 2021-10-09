# Code : Remove Min
# Send Feedback
# Implement the function RemoveMin for the min priority queue class.
# For a minimum priority queue, write the function for removing the minimum element present. Remove and return the minimum element.
# Note : main function is given for your reference which we are using internally to test the code.

class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def _percolateDown(self):
        parentI = 0
        firstC = 2 * parentI + 1
        secondC = 2 * parentI + 2
        
        while firstC < len(self.pq):
            if self.pq[parentI].priority > self.pq[firstC].priority:
                self.pq[parentI], self.pq[firstC] = self.pq[firstC], self.pq[parentI]
                parentI = firstC
            elif secondC < len(self.pq) and self.pq[parentI].priority > self.pq[secondC].priority:
                self.pq[parentI], self.pq[secondC] = self.pq[secondC], self.pq[parentI]
                parentI = secondC
            else:
                break
            firstC = 2 * parentI + 1
            secondC = 2 * parentI + 2

    def removeMin(self):
        if len(self.pq) == 0:
            return None
        removed = self.pq[0].ele
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self._percolateDown()
        return removed 
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1