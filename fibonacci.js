function Fibonacci(n)
{
    // write code here
    var result=new Array(10)//创建一个长度为10的数组
    if(n===0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    result[0]=0;
    result[1]=1;
    for(var i=2;i<=n;i++){
        result[i]=result[i-1]+result[i-2];
    }
    return result[n]
}
console.log(Fibonacci(5))
