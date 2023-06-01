from typing import Optional

from common import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        switchCount = 0

        while curA and curB:
            if curA == curB:
                return curA

            curA = curA.next
            if not curA:
                if switchCount == 2:
                    break
                switchCount += 1
                curA = headB

            curB = curB.next
            if not curB:
                if switchCount == 2:
                    break
                switchCount += 1
                curB = headA

        return None