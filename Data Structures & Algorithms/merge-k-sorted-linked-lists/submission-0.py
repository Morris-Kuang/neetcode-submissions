# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """兩兩排列，再兩兩排列"""
        
        if not lists or len(lists) == 0: # edge cases
            return None
        
        def recursive(lists): # divide and conquer
            if len(lists) == 1:
                return lists[0]

            mid = len(lists) // 2
            left = recursive(lists[:mid])
            right = recursive(lists[mid:])

            return self.merge2Lists(left, right)
        
        return recursive(lists)

        
        
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next

