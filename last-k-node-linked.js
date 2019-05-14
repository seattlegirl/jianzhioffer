function ListNode(x){
    this.val = x;
    this.next = null;
}
function FindKthToTail(head, k)
{
    // 链表为空时，k为0时
    if(head===null || k==0){
        return 0;
    }
    var first=head;
    var second;
    for(var i=0;i<k-1;i++){
        if(first.next!=null){//判断节点个数是否小于k
            first=first.next;
        }
        else{
            return 0;
        }
    }
    second=head;
    while(first.next!=null){
        first=first.next;
        second=second.next;
    }
    return second;
}
var x=new ListNode(1);
var y=new ListNode(2);
var z=new ListNode(3);
y.next=x.next;
x.next=y;
z.next=y.next;
y.next=z;
var res=FindKthToTail(x,1);
console.log(res.val);
// while(res){
//     console.log(res.val);
//     res=res.next;
// }
