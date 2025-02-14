from typing import Optional, List
import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to print the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# Convert a list to a linked list
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> int:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev=cur
            cur = next_node
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        orginal = copy.deepcopy(head)
        reversed_head = self.reverseList(head)
        print("reversed head .....",reversed_head)
        print("head inside the pairsum.....",orginal)
        # Step 2: Traverse both original and reversed lists to compute twin sums
        max_sum = float("-inf")
        while orginal:
            max_sum = max(max_sum, orginal.val + reversed_head.val)
            orginal = orginal.next
            reversed_head = reversed_head.next
        return max_sum



vals =[47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
head = create_linked_list(vals)
print("original head = ", head)
sol = Solution()
print(sol.pairSum(head))