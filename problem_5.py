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
PROBLEM 5
 Add Two Linked list
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
SAMPLE Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
SAMPLE Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
class Node(object):
    def __init__(self,data):
        self.data=data;
        self.next=None
class LinkedList(object):
    def __init__(self):
        self.head=None
#Push nodes at the back
    def pushBack(self,newData):
        newNode=Node(newData)
        if self.head is None:
            self.head=newNode
        else:
            last=self.head
            while(last.next):
                last = last.next
            last.next=newNode
#print the reultant linked list
    def printList(self):
        temp = self.head
        while (temp):
            if temp.next != None:
                print (temp.data,end="-->")
            else:
                print(temp.data)
            temp = temp.next
#reverse linked list
    def revllist(self,first):
        prev = None
        frev = first
        while (frev is not None):
            next = frev.next
            frev.next = prev
            prev = frev
            frev = next
            first = prev
        return first
#Add the two linked list
    def addlist(self, first, second):
        first = self.revllist(first)
        second = self.revllist(second)

        carry =0
        third = LinkedList()
        while first is not None or second is not None:
            val1 = first.data
            # print(val1)
            first = first.next
            val2 = second.data
            # print(val2)
            second = second.next
            sum = carry + val1 + val2
            if sum >= 10:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
            # print (sum)
            third.pushBack(sum)
        third.printList()



if __name__=="__main__":
    first = LinkedList()
    first.pushBack(2)
    first.pushBack(4)
    first.pushBack(3)
    first.printList()
    second=LinkedList()
    second.pushBack(5)
    second.pushBack(6)
    second.pushBack(4)
    second.printList()
    res= LinkedList()
    res.addlist(first.head,second.head)
