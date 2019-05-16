# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def similar(self,p,q):
        #递归跳出条件
        #如果tree2已经遍历完成，返回true
        if q==None:
            return True
        #如果tree2还没有遍历完，tree1遍历完成，返回false
        if p==None:
            return False
        #如果其中有一个点对不上了，返回false
        if p.val!=q.val:
            return False
        #根节点对上就去子节点找
        return self.similar(p.left,q.left) and self.similar(p.right,q.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result=False
        #两个根节点都不为空，开始判断
        if pRoot1!=None and pRoot2!=None:
            #两个根节点相等
            if pRoot1.val == pRoot2.val:
                #判断两个根节点的子节点
                result=self.similar(pRoot1,pRoot2)
            #如果根节点那没找到，就去找左儿子节点为根节点
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            #如果左儿子还没找到，就去找右儿子为根节点
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result

tree1=TreeNode(8)
tree1.left=TreeNode(9)
tree1.right=TreeNode(2)


tree2=TreeNode(8)
tree2.left=TreeNode(9)


print(Solution().HasSubtree(tree1,tree2))
