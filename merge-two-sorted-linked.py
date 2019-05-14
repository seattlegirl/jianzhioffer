# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1==None:
            return pHead2
        elif pHead2==None:
            return pHead1
        mergeHead=None
        if pHead1.val<pHead2.val:
            mergeHead=pHead1
            mergeHead.next=self.Merge(pHead1.next,pHead2)
        else:
            mergeHead=pHead2
            mergeHead.next=self.Merge(pHead1,pHead2.next)
        return mergeHead

x=ListNode(1)
x.next=ListNode(3)
x.next.next=ListNode(5)
x.next.next.next=ListNode(7)

y=ListNode(2)
y.next=ListNode(4)
y.next.next=ListNode(6)
y.next.next.next=ListNode(10)

res=Solution().Merge(x,y)
while res:
    print(res.val)
    res=res.next