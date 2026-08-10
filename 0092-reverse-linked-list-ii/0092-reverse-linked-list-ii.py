# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Step 1: Move `pre` to the node before `left`
        for _ in range(left - 1):
            pre = pre.next

        # Step 2: Reverse the sublist [left, right]
        reverse = None
        cur = pre.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = reverse
            reverse = cur
            cur = nxt

        # Step 3: Connect the reversed sublist back
        pre.next.next = cur
        pre.next = reverse

        return dummy.next
