# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # step 1: find the niddle node
        #  two pointer: slow and fast
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #  step 2: reverse the second half
        prev,current = None,slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current= next_node
        
        # step 3: combine them
        first,second = head,prev
        while second.next:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next =first_next

            second =second_next
            first = first_next