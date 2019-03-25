# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0 or len(tin)==0:
            return None
        elif len(pre)==len(tin)==1:
            return TreeNode(pre[0])
        else:
            root_data=TreeNode(pre[0])
            //构建左子树
            root_data.left=self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[:tin.index(pre[0])])
            //构建右子树
            root_data.right=self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1: ], tin[tin.index(pre[0]) + 1: ])
        return root_data

if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    root=Solution().reConstructBinaryTree(pre,tin)
    print(root)
    
