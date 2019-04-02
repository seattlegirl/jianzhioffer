# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        #竖着覆盖f(number-1)
        #横着覆盖f(number-2)
        # write code here
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        result=[0]*(number+1)
        result[0]=0
        result[1]=1
        result[2]=2
        for i in range(3,number+1):
            result[i]=result[i-1]+result[i-2]
        return result[number]
if __name__ == "__main__":
    print(Solution().rectCover(3))
    