# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast, slow = head.next, head
        while fast != slow and fast != None:
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next.next
        if fast == slow:
            return True
        else:
            return False

