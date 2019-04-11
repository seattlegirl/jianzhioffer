function ListNode(x){
    this.val = x;
    this.next = null;
}


//法一：利用三个指针遍历
function ReverseList1(head){
    if(head===null){
        return head;
    }
    var p=head;
    var q=null;
    var r=null;
    while(p!=null){
        q=p.next;
        p.next=r;
        r=p;
        p=q;
    }
    return r;
}

//法二：尾插法
function ReverseList2(head){
    if(head==null){
        return head;
    }
    var p=head;
    var q=null;
    var r=p;
    while(p.next!=null){
        q=p.next;
        p.next=q.next;
        q.next=r;
        r=q;
    }
    return r;
}

//法三：递归
function ReverseList3(head){
    if(head.next==null){//递归跳出条件
        return head;
    }
    var newHead=ReverseList3(head.next);
    head.next.next=head;
    head.next=null;
    return newHead;
}

var l1=new ListNode(3);
l1.next=new ListNode(2);
l1.next.next=new ListNode(1);
l1.next.next.next=new ListNode(99);

var l2=ReverseList3(l1);

while(l2!=null){
    console.log(l2.val);
    l2=l2.next;
}