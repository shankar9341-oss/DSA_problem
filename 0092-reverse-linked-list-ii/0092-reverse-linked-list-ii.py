# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prevleft = dummy

        for _ in range(1, left):
            prevleft = prevleft.next
        prev = None
        curr = prevleft.next 

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        LeftNode = prevleft.next
        prevleft.next = prev
        LeftNode.next = curr

        return dummy.next