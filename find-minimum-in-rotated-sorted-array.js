function minNumberInRotateArray(rotateArray)
{
    // write code here
    if (rotateArray.length<1){
        return 0;
    }
    if (rotateArray.length==1){
        return rotateArray[0];
    }
    var index1=0;
    var index2=rotateArray.length-1;
    var midindex=index1; //当原顺序数组中的0个进行了反转时，即没有翻转，最小值是第一个
    while (rotateArray[index1]>=rotateArray[index2]){
        //最后两个指针指向相邻的数字，则第二个指针指向的是最小的数字
        if (index2-index1===1){
            midindex=index2;
            break;
        }
        midindex=parseInt(index1+(index2-index1)/2);//不加parseInt有很多测试用例无法通过！！
        //当前一个指针后一个指针中间指针的数值相等时，无法判断中间指针属于前面还是后面，只能采用顺序查找
        if(rotateArray[index1]===rotateArray[index2]===rotateArray[midindex]){
            return MinInOrder(rotateArray,index1,index2);
        }
        else if(rotateArray[midindex]>=rotateArray[index1]){
            index1=midindex;
        }
        else{
            index2=midindex;
        }
    }       
    return rotateArray[midindex];
}
function MinInOrder(rotateArray,index1,index2){
    var result=rotateArray[index1];
    var i;
    for (i=index1+1;i<=index2;i++){
        if(rotateArray[i]>result){
            result=rotateArray[i];
        }    
    }
    return result;
}

//var array=[6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
var array=[4,5,6,7,1,2]
console.log(minNumberInRotateArray(array))