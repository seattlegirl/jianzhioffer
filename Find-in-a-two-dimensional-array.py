# -*- coding:utf-8 -*-
"""
时间限制：1秒 空间限制：32768K 热度指数：1021682

题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution(object):
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row=len(array)#行数
        col=len(array[0])#列数
        for i in range(row):
            for j in range(col)[::-1]:
                if (array[i][j]==target):
                    return True
                elif (array[i][j]>target):
                    col-=1
                else:
                    row+=1
        return False
                
        
if __name__ == "__main__":
    print(Solution().Find(7,[[1,2,3],[4,5,6],[7,8,9]]))
    