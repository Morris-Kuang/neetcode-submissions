# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # An efficient one

        dummy = ListNode()
        curr = dummy
        dummy.next = head

        while True:
            groupPrev = curr  # Always start with the former group's last element
            groupLast = curr.next
            curr = curr.next  # first item in a group

            kth = curr
            kElements = True
            for i in range(k-1):
                kth = kth.next
                if kth == None:
                    kElements = False
                    break

            if kElements == True:
                groupNext = kth.next
                prev = groupPrev
                while True:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    if nxt == groupNext:
                        break
                    curr = nxt
                
                groupPrev.next = curr
                curr = groupLast
                curr.next = groupNext
                if groupNext == None:
                    break
            else:
                groupPrev.next = groupLast
                break
            

        return dummy.next




