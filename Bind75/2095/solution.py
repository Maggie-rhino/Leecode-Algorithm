solution.py

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

#  if n %2 =1:
		# N =n-1



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first we need to get the lenght of the listNode
        l =0
        cur =head
        while cur !=None:
        	l +=1
        	cur =cur.next
        # step 2 : get the index of the middle node
        if l %2 ==1:
        	mid = (l-1)/2
        else:
        	mid = l/2

        # step 3: iterate the linklist and delete the middle node
        #  edge case: l =1
        if l ==1:
        	return None

        current_node =head
        #  iterate to the node before the middle node
        step=0
        while step < mid-1:
        	current_node = current_node.next
        	step +=1

        if current_node.next.next ==None:
        	current_node.next =None
        else:
        	current_node.next =current_node.next.next

        return head





