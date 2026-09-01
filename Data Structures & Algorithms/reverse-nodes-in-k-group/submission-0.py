# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while True:
            groupPrev = curr #None
            curr = curr.next
            groupLast = curr
            kth = self.findKth(curr, k)
            if kth == None:
                break
            groupNext = kth.next
            
            prev = groupPrev
            while True:
                nxt = curr.next
                curr.next = prev
                prev = curr
                
                if curr == kth:
                    break
                curr = nxt

            groupPrev.next = curr
            curr = groupLast
            curr.next = groupNext

        return dummy.next
    
    
    def findKth(self, curr, k):
        cnt = 1
        signal = False
        while curr and k > 0:
            curr = curr.next
            cnt += 1
            if cnt == k:
                signal = True
                break
        
        return curr if signal == True else None
