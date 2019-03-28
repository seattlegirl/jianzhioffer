# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        result=[0]*(n+1)
        if n==0:
            return 0
        if n==1:
            return 1
        result[0]=0
        result[1]=1
        for i in range(2,n+1):
            result[i]=result[i-1]+result[i-2]
        return result[n]

if __name__ == "__main__":
    print(Solution().Fibonacci(0))
    