# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        Second = slow.next
        slow.next = None
        prev = None
        while Second:
            nxt = Second.next
            Second.next = prev
            prev = Second
            Second = nxt
        
        first, Second = head, prev
        while Second:
            tmp1, tmp2 = first.next, Second.next
            first.next = Second
            Second.next = tmp1
            first, Second = tmp1, tmp2
        