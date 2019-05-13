# -*- coding:utf-8 -*-
"""
思路： 
暴力解决：分为两种情况：一种整数n>=0,直接化为二进制.一种n<0，求其补码
其中求补码的方法为将其用原码表示，然后从右边第一个为‘1’的数起往左依次取反（取反操作即与1异或，0^1=1,1^1=0）
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            num =  ('{:032b}'.format(n))
        else:
            res =  ('{:032b}'.format(-n))[1:]
            num =  '1'
            flag = 0
            for i in range(len(res)-1,-1,-1):
                if res[i] == '1':
                    index = i
                    flag = 1
                    break
            if flag:
                for i in res[:index]:
                    num += str(int(i) ^ 1)
                num += res[index:]
            else:
                num += res
            print(num,len(num))
        return num.count('1')

if __name__ == "__main__":
    print(Solution().NumberOf1(9))
    
