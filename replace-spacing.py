# -*- coding:utf-8 -*-
"""
时间限制：1秒 空间限制：32768K 热度指数：884138

题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution:
    # s 源字符串
    # def replaceSpace(self, s):
    #     # write code here
    #     return s.replace(' ','%20')
    def replaceSpace(self,s):
        return '%20'.join(s.split(' '))
if __name__ == "__main__":
    print(Solution().replaceSpace("We Are Happy"))
    