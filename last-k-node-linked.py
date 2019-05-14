# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 链表为空时，k为0时
        if head==None or k==0:
            return 0
        first=head
        second=None
        for i in range(0,k-1):
            if first.next!=None:
                first=first.next
            else:
                return 0
        second=head
        while first.next!=None:
            first=first.next
            second=second.next
        return second

x=ListNode(1)
x.next=ListNode(2)
x.next.next=ListNode(3)
x.next.next.next=ListNode(4)
res=Solution().FindKthToTail(x,3)
print(res.val)