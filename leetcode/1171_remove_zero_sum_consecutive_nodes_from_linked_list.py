from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        nodes = self._get_list(head)
        removed = self._get_removed_nodes(nodes)
        return self._get_linked_list(nodes, removed)

    def _get_list(self, head: ListNode) -> List[int]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes

    def _get_removed_nodes(self, nodes: List[int]) -> List[bool]:
        N = len(nodes)
        removed = [False] * N
        for i in range(N):
            if removed[i]:
                continue
            j = i
            curr_sum = 0
            while j < N:
                if not removed[j]:
                    curr_sum += nodes[j]
                j += 1
                if curr_sum == 0:
                    break
            if curr_sum == 0:
                for k in range(i, min(N, j)):
                    removed[k] = True
        return removed

    def _get_linked_list(self,
                         nodes: List[int],
                         removed: List[bool]) -> ListNode:
        dummy = curr = ListNode(-1)
        for val, remd in zip(nodes, removed):
            if not remd:
                node = ListNode(val)
                curr.next = node
                curr = curr.next
        return dummy.next
