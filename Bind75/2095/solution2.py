solution2.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#  we could use slow and fast pointer to find the middle node 
# instead of finding the length first

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# 3
# fast, slow, 


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	if head.next ==None:
    		return None
    	if head.next.next == None:
    		head.next =None
    		return head

    	slow =head
    	fast = head.next.next
    	while fast and fast.next:
    		fast = fast.next.next
    		slow = slow.next

    	slow.next = slow.next.next
    	return head




