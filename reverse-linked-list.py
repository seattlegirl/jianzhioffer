#-*- coding:utf-8 -*-
class LNode:
    def __init__(self,x):
        self.val=x
        self.next=None


#法一：利用三个指针遍历
# 返回ListNode
def ReverseList1(pHead):
    # write code here
    if pHead==None:
        return pHead
    p=pHead
    q=None
    r=None
    while(p):
        q=p.next
        p.next=r
        r=p
        p=q
    return r

#法二：尾插法实现
# 返回ListNode
def ReverseList2(pHead):
    # write code here
    if pHead==None:
        return pHead
    p=pHead
    q=None
    r=p
    while(p.next!=None):
        q=p.next
        p.next=q.next
        q.next=r
        r=q
    return r

#法三：递归实现
# 返回ListNode
def ReverseList3(pHead):
    # write code here
    if pHead.next==None: #递归跳出条件
        return pHead
    newHead=ReverseList3(pHead.next)
    pHead.next.next=pHead
    pHead.next=None
    return newHead

if __name__ == "__main__":
    l1=LNode(3)
    l1.next=LNode(2)
    l1.next.next=LNode(1)
    l1.next.next.next=LNode(99)
    l=ReverseList3(l1)
    print(l.val,l.next.val,l.next.next.val,l.next.next.next.val)
          
        

