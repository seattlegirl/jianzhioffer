# -*- coding:utf-8 -*-
"""
在Python中，对于超出32位的大整数，会自动进行大整数的转变，这就导致了在右移位过程中，不会出现移到了0的情况，
也就会造成了死循环。需要在移动的过程中加一下判断就行了,和0xFFFFFFFF做一下比较
"""
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num2!=0):
            num1,num2=(num1^num2) & 0xFFFFFFFF,((num1&num2)<<1) & 0xFFFFFFFF
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)
if __name__ == "__main__":
    print (Solution().Add(-1,2))
    
