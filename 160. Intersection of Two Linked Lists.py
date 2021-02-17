# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return
        l1 = headA
        l2 = headB
        
        lastElement = None
        while True:
            
            if l1 == l2:
                return l2
            
            if l1.next != None:
                l1 = l1.next
            else:
                if lastElement is None: lastElement = l1
                elif lastElement != l1: break
                l1 = headB
                
            if l2.next != None:
                l2 = l2.next
            else:
                if lastElement is None: lastElement = l2
                elif lastElement != l2: break
                l2 = headA
