from typing import Optional

from common import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        next = head.next
        head.next = None
        newHead = self.reverseList(next)
        next.next = head

        return newHead
