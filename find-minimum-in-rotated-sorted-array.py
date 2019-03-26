# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)<1:
            return 0
        index1=0
        index2=len(rotateArray)-1
        midindex=index1 #当原顺序数组中的0个进行了反转时，即没有翻转，最小值是第一个
        while rotateArray[index1]>=rotateArray[index2]:
            if index2-index1==1:#最后两个指针指向相邻的数字，则第二个指针指向的是最小的数字
                midindex=index2
                break

            midindex=(index1+(index2-index1)/2)
            #当前一个指针后一个指针中间指针的数值相等时，无法判断中间指针属于前面还是后面，只能采用顺序查找
            if(rotateArray[index1]==rotateArray[index2]==rotateArray[midindex]):
                return MinInOrder(rotateArray,index1,index2)

            if(rotateArray[midindex]>=rotateArray[index1]):
                index1=midindex
            elif(rotateArray[midindex]<=rotateArray[index2]):
                index2=midindex      
        return rotateArray[midindex]

    def MinInOrder(rotateArray,index1,index2):
        result=nums[index1]
        for i in range(index1+1,index2+1):
            if rotateArray[i]>result:
                result=rotateArray[i]
        return result

if __name__ == "__main__":
    array=[6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print(Solution().minNumberInRotateArray(array))
    

