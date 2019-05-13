function ListNode(x){
    this.val = x;
    this.next = null;
}
function printListFromTailToHead(head)
{
    // write code here
    var array=[];
    var arr=[];
    while(head){
        array.push(head.val);
        head=head.next;
    }
    while(array.length){
        arr.push(array.pop())
    }
    return arr;
}
