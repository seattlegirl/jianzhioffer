function Add(num1, num2)
{
    var sum=0;
    var array=0
    while(num2!=0){
        sum=num1^num2 //按位异或
        array=(num1&num2)<<1 //按位与，并左移一位
        num1=sum
        num2=array
    }
    return num1
}
console.log(Add(-1,2))
