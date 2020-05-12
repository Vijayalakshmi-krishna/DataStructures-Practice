"""
Copyright (C) 2020 vijayalakshmisuresh

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

'''
PROBLEM 6
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
SAMPLE INPUT:
A   0--->9--->1--->2--->4
B             3--->2--->4

SAMPLE OUPUT: 2
A and B to intersect at node 2.
'''

class Node(object):
    def __init__(self,data):
        self.data=data;
        self.next=None
class LinkedList(object):
    def __init__(self):
        self.head=None
    #push node at the back
    def pushBack(self,newData):
        newNode=Node(newData)
        if self.head is None:
            self.head=newNode
        else:
            last=self.head
            while(last.next):
                last = last.next
            last.next=newNode
    #print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            if temp.next != None:
                print (temp.data,end="-->")
            else:
                print(temp.data)
            temp = temp.next

    def findInterNode(self,first,second):

        c1=self.getCount(first)
        c2= self.getCount(second)

        if c1 > c2:
            d= c1 - c2
            return self.getInterNode(d,first,second)
        else:
            d= c2 - c1
            return self.getInterNode(d,second,first)
    def getCount(self,c):
        # print (c.data)
        curr = c
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    #return the intersect node
    def getInterNode(self,d,head1,head2):
        # print (head1.data)
        for i in range(0,d):
            if head1.next == None:
                return -1
            head1 = head1.next
        while head1 is not None and head2 is not None:
            if head1.data == head2.data:
                return head1.data
            head1= head1.next
            head2 = head2.next
        return -1

if __name__=="__main__":
    first = LinkedList()
    first.pushBack(3)
    first.pushBack(6)
    first.pushBack(9)
    first.pushBack(15)
    first.pushBack(30)
    first.printList()
    second=LinkedList()
    second.pushBack(10)
    second.pushBack(15)
    second.pushBack(30)

    second.printList()
    res= LinkedList()
    print(res.findInterNode(first.head,second.head))