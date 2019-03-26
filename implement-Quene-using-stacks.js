var stack1=[];//新建两个数组
var stack2=[];

function push(node)
{
    // write code here
    stack1.push(node) //push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度。
}
function pop()
{
    // write code here
    //pop() 方法用于删除数组的最后一个元素并返回删除的元素。
    //shift() 方法用于把数组的第一个元素从其中删除，并返回第一个元素的值。
    if(stack1.length==0){
        return false
    }
    return stack1.shift()
}