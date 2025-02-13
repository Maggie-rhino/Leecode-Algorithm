solution.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You must solve the problem in O(1) extra space complexity 
# and O(n) time complexity.


# odd_node and even_node
#  even_node.next = odd_node.next
#  odd_node.next = odd_node.next.next



class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	# edge case
    	if head==None or head.next ==None:
    		return head

    	# define even_node and odd_node
    	odd_node = head
    	even_node =head.next
    	even_header =even_node

    	while even_node and even_node.next:
    		odd_node.next =even_node.next
    		odd_node =odd_node.next

    		even_node.next = odd_node.next
    		even_node = even_node.next

    	odd_node.next =even_header

    	return head 





