from typing import Optional

from common import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur.next != None and cur.next.next != None:
            next = cur.next
            nextNext = next.next
            nextNextNext = nextNext.next

            cur.next = nextNext
            nextNext.next = next
            next.next = nextNextNext

            cur = cur.next.next

        return dummy.next