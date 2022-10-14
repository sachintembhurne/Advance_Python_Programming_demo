# Link List : Leaner Data Structure

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = NewNode

    def AtStart(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print('The Mentioned node does not exist')
            return
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def DeleteNode(self, RemoveData):
        Headval = self.head
        if Headval is not None:
            if Headval.data == RemoveData:
                self.head = Headval.next
                Headval = None
                return

        while Headval is not None:
            if Headval.data == RemoveData:
                break
            prev = Headval
            Headval = Headval.next

        if Headval == None:
            return
        prev.next = Headval.next
        Headval = None

    def getCount(self):
        tem = self.head
        count = 0

        while tem:
            count += 1
            tem = tem.next
        return count

    def remove_duplicates(self):
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head

        while ptr1 is not None and ptr1.next is not None:
            ptr2 = ptr1
            while ptr2.next is not None:
                if ptr1.data == ptr2.next.data:
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    # def remove_from_sorted(self):
    #     temp = self.head
    #     if temp is None:
    #         return
    #     while temp.next is not None:
    #         if temp.data == temp.next.data:
    #             new = temp.next.next
    #             temp.next = None
    #             temp.next = new
    #         else:
    #             temp = temp.next
    #     return self.head

    def remove_from_sorted(self):
        if self.head is None and self.head.next is None:
            return
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return

    def swapNodes(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX is not None and currX.data is not x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = None
        while currY is not None and currY.data is not y:
            preY = currY
            currY = currY.next
        if currX is None or currY is None:
            return
        if prevX is not None:
            prevX.next = currY
        else:
            self.head = currY
        if prevY is not None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next


list1 = SLL()
list1.head = Node(10)
e2 = Node(20)
e3 = Node(30)
list1.head.next = e2
e2.next = e3


list1.AtEnd(40)
list1.AtEnd(50)
list1.AtEnd(60)
print('The SLL before swapping nodes')
list1.listprint()
print('The SLL after swapping the nodes')
list1.swapNodes(10, 20)
list1.listprint()
# list1.Inbetween(list1.head, 20)
# list1.Inbetween(list1.head.next, 20)
# list1.Inbetween(list1.head.next.next, 20)
# list1.DeleteNode('Fir')



# count = list1.getCount()
# print('Count before removing duplicate= ', count)
# # list1.remove_duplicates()
# list1.remove_from_sorted()
# count = list1.getCount()
# print('Count after removing duplicate= ', count)
# list1.listprint()
