function Power(base, exponent)
{
    var result=1;//保存结果
    var flag=false;//指数是否为负数
    // 底数为0
    if(base===0){
        return 0;
    }
    //指数为0
    if(exponent===0){
        return 1;
    }
    //指数为负数时
    if(exponent<0){
        flag=true;
        exponent=-exponent;
    }
    for(var i=1;i<=exponent;i++){
        result*=base;
    }
    //指数为负数时
    if(flag===true){
        result=1/result;
    }
    return result;
}

console.log(Power(2,-3))