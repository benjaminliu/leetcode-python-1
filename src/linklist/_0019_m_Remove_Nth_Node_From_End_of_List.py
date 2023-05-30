from typing import Optional

from common import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        while n >= 0:
            n -= 1
            fast = fast.next

        slow = dummy
        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
