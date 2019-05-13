//法一
function NumberOf1_1(n)
{
    // n每次和1做与运算，1每次左移。一共左移次数为n的位数
    var count=0;
    var flag=1;
    while(flag){
        if(n&flag){
            count+=1;
        }
        flag=flag<<1;
    }
    return count;
}

//法二
function NumberOf1_2(n)
{
    //n减去1，再和原整数做与运算，把该整数最右边的1变成0.二进制中有几个1进行几次这样的运算。循环的次数为n中1的的个数。
    var count=0;
    while(n){
        count+=1;
        n=(n-1)&n;
    }
    return count;
}
console.log(NumberOf1_2(9));
