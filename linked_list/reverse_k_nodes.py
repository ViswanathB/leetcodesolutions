"""_summary_

https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print(self, head: Optional[ListNode]):
        while head != None:
            print(head.val, end=",")
            head = head.next

        print()

    def reverse(self, start: Optional[ListNode], end: Optional[ListNode]):
        start_node_return = end
        end_node_return = start

        prev_node = None
        end.next = None

        while start != None:
            temp = start.next
            start.next = prev_node
            prev_node = start
            start = temp

        return start_node_return, end_node_return

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        head_prev_1 = ListNode()
        head_prev_1.next = head

        head_prev_2 = ListNode()
        head_prev_2.next = head

        first_time = True
        while head != None:
            end = head
            init_k = k
            while init_k > 1 and end.next != None:
                end = end.next
                init_k -= 1

            if init_k > 1:
                break
            end_next = end.next
            start_return, end_return = self.reverse(head, end)

            if first_time:
                first_time = False
                head_prev_1.next = start_return

            head_prev_2.next = start_return
            head_prev_2 = end_return
            end_return.next = end_next
            head = end_next

            self.print(head_prev_1.next)

        return head_prev_1.next
