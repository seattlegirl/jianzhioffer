function ListNode(x){
    this.val = x;
    this.next = null;
}
//????????
var reverseList = function(head) {
    if (head==null || head.next==null){
       return head;
   }
   var pre = null;
   var next = null;
   while (head != null) {
       next = head.next;
       head.next = pre;
       pre = head;
       head = next;
   }
   return pre;  
};

//法二
var reverseList = function(head) {
   if(head==null || head.next==null){
       return head;
   }
   var list = head;
   var p = list;
   var q= null;
   while(p.next!=null) {
       q = p.next;
       p.next = q.next;
       q.next = list;
       list = q;     
   }
   return list;
}
