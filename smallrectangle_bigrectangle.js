function rectCover(number)
{
    // write code here
    //竖着覆盖f(number-1)
    //横着覆盖f(number-2)
    var result=new Array(number+1)
    if(number<=0){
        return 0;
    }
    if(number==-1){
        return 1;
    }
    if(number===2){
        return 2;
    }
    result[0]=0;
    result[1]=1;
    result[2]=2;
    for(var i=3;i<=number;i++){
        result[i]=result[i-1]+result[i-2];
    }
    return result[number]
}
console.log(rectCover(3))