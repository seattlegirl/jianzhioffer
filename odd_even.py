# -*- coding:utf-8 -*-
#法一 只能实现前面是奇数，后面是偶数，无法保持相对位置不变
class Solution:
    def reOrderArray1(self, array):
        # write code here
        l=0
        r=len(array)-1
        while(l<r):
            while(l<r and not isEven(array[l])):
                l+=1
            
            while(l<r and isEven(array[r])):
                r-=1
                
            if(l<r):
                temp=array[l]
                array[l]=array[r]
                array[r]=temp

        return array;

        #是不是偶数
        def isEven(n):
            if n%2==0:
                return true;
            else:
                return false;

#开辟多个数组，遍历，能保证前面是奇数，后面是偶数，且保持相对位置不变
class Solution:
    def reOrderArray2(self, array):
        arr1=[]
        arr2=[]
        for i in range(0,len(array)):
            if(array[i]%2==0):
                arr2.append(array[i]);      
            else:
                arr1.append(array[i]);
        arr3=[]
        arr3=arr1+arr2
        return arr3

arr=Solution().reOrderArray2([1,2,3,4,5,6,7]);
for k in range(0,len(arr)):
    print(arr[k])

