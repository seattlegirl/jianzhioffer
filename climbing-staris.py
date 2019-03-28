# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
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
            result[i]=result[i-1]+result[i-2]
        return result[number]
        # return self.jumpFloor(number-1)+self.jumpFloor(number-2)

if __name__ == "__main__":
    print(Solution().jumpFloor(3))
    
