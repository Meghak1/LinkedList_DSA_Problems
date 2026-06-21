"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        if not head or x<=0:
            return head
        if x==1:
            head=head.next
            
            if head:
                head.prev = None
            return head
    
        current = head
        count = 1
        while count<x:
            current = current.next
            count+=1
            if current is None:
                return head
        if current.next:
            current.next.prev=current.prev
        if current.prev:
            current.prev.next = current.next
        current = None
        return head
            
