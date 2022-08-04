# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        while l1 != None:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2 != None:
            s2 = str(l2.val) + s2
            l2 = l2.next
        s = str(int(s1) + int(s2))
        
        if len(s) != 1:
            temp1 = ListNode(val=int(s[0]), next=None)
            if len(s) > 2:
                for x in range(1, len(s)):
                    temp = ListNode(val=int(s[x]), next=temp1)
                    temp1 = temp
                return temp
            else:
                return ListNode(val=int(s[1]), next=temp1)
        else:
            return ListNode(val=int(s[0]),next=None)
