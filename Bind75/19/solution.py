# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Naive thought: 
        # step 1: find the length of the linklist first
        #  step 2: iterate the linklist and remove the Nth Node
        
        #  step 1:
        l =0
        current = head
        while current:
            l +=1
            current =current.next
        if l==n:
            return head.next
        #  step 2 
        reserved_num =0
        curr = head
        while reserved_num < l-n-1:
            reserved_num +=1
            curr =curr.next
        if n == 1:
            curr.next =None
        else:
            curr.next = curr.next.next
        return head