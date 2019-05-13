//法一 只能实现前面是奇数，后面是偶数，无法保持相对位置不变
function reOrderArray1(array)
{
    // write code here
    var l=0;
    var r=array.length-1;
    while(l<r){
        while(l<r && !isEven(array[l])){
            l++;
        }
        while(l<r && isEven(array[r])){
            r--;
        }
        if(l<r){
            var temp;
            temp=array[l];
            array[l]=array[r];
            array[r]=temp;
        }
         
    }

    return array;
}
//是不是偶数
function isEven(n){
    if(n%2==0){
        return true;
    }
    else{
        return false;
    }
}

//开辟多个数组，遍历，能保证前面是奇数，后面是偶数，且保持相对位置不变
function reOrderArray2(array)
{
    // write code here
    var arr1=[];//存奇数
    var arr2=[];//存偶数
    for(var i=0;i<array.length;i++){
        if(array[i]%2==0){
            arr2.push(array[i]);
        }
        else{
            arr1.push(array[i]);
        }
    }
    var arr3=[];
    arr3=arr1.concat(arr2);
    return arr3;
}

var arr=reOrderArray2([1,2,3,4,5]);
for(var k=0;k<arr.length;k++){
    console.log(arr[k]);
}
