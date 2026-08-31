# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        empty = []
        while head:
            empty.append(head.val)
            head = head.next
        empty1 = []
        for i in range(1, len(empty)-1):
            if empty[i-1] > empty[i] < empty[i+1] or empty[i-1] < empty[i] > empty[i+1]:
                empty1.append(i)
        if len(empty1) < 2:
            return [-1, -1]
        
        max1 = empty1[-1] - empty1[0]
        min1 = inf
        for i in range(1, len(empty1)):
            min1 = min(min1, empty1[i] - empty1[i-1])
        
        return [min1, max1]