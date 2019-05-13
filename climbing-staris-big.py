# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
    # //第一次跳1个台阶，剩下的数目是f(n-1)
    # //第一次跳2个台阶，剩下的数目是f(n-2)
    # //.......
    # //第一次跳n-2个台阶，剩下的数目是f(2)=2
    # //第一次跳n-1个台阶，剩下的数目是f(1)=1
    # //第一次跳n个，数目直接是1次
    # //f(n)=f(n-1)+f(n-2)+f(n-3)+......f(2)+f(1)+1
    # //f(n)-f(n-1)=f(n-1)
    # //f(n)=2f(n-1)
        if number<=0:
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
            result[i]=2*result[i-1]
        return result[number]

if __name__ == "__main__":
    print(Solution().jumpFloorII(3))
    