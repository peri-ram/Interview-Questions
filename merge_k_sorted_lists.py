# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = [ (x.val, id(x), x.next) for x in lists if x]
        heapq.heapify(heads)

        s = None
        e = None
        while(heads):
            (v, _, n) = heapq.heappop(heads)
            if(not s):
                s = e = ListNode(v)
            else:
                e.next = ListNode(v)
                e = e.next
            if(n):
                heapq.heappush(heads, (n.val, id(n), n.next))
        return s
