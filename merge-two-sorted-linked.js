function ListNode(x){
    this.val = x;
    this.next = null;
}
function Merge(pHead1, pHead2)
{
    if(pHead1===null){
        return pHead2;
    }
    else if(pHead2===null){
        return pHead1;
    }
    var mergeHead=null;
    if(pHead1.val<pHead2.val){
        mergeHead=pHead1;
        mergeHead.next=Merge(pHead1.next,pHead2);
    }
    else{
        mergeHead=pHead2;
        mergeHead.next=Merge(pHead1,pHead2.next);
    }
    return mergeHead;
}

var x1=new ListNode(1);
var x2=new ListNode(3);
var x3=new ListNode(5);
x2.next=x1.next;
x1.next=x2;
x3.next=x2.next;
x2.next=x3;


var y1=new ListNode(2);
var y2=new ListNode(4);
var y3=new ListNode(6);
y2.next=y1.next;
y1.next=y2;
y3.next=y2.next;
y2.next=y3;

var res=Merge(x1,y1);
// console.log(res.val);
while(res){
    console.log(res.val);
    res=res.next;
}