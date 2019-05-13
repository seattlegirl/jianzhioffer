# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        result=1;#保存结果
        flag=False;#指数是否为负数
        #底数为0
        if base==0:
            return 0

        #指数为0
        if exponent==0:
            return 1

        #指数为负数时
        if exponent<0:
            flag=True
            exponent=-exponent

        for i in range(0,exponent):
            result*=base

        #指数为负数时
        if flag==True:
            result=1/result

        return result

print(Solution().Power(2,-2))
        