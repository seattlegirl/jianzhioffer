function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} 

function similar(p,q){
    //递归跳出条件
    //如果tree2已经遍历完成，返回true
    if(q==null){
        return true;
    }
    //如果tree2还没有遍历完，tree1遍历完成，返回false
    if(p==null){
        return false;
    }
    //如果其中有一个点对不上了，返回false
    if(p.val!=q.val){
        return false;
    }
    //根节点对上就去子节点找
    return (similar(p.left,q.left)&&similar(p.right,q.right));
}

function HasSubtree(pRoot1, pRoot2)
{
    // write code here
    var result=false;
    //两个根节点都不为空，开始判断
    if(pRoot1!=null && pRoot2!=null){
        //两个根节点相等
        if(pRoot1.val==pRoot2.val){
            //判断两个根节点的子节点
            result=similar(pRoot1,pRoot2);
        }
        //如果根节点那没找到，就去找左儿子节点为根节点
        if(result==false){
            result=HasSubtree(pRoot1.left,pRoot2);
        }
        //如果左儿子还没找到，就去找右儿子为根节点
        if(result==false){
            result=HasSubtree(pRoot1.right,pRoot2);
        }
    }
    return result;
}

var tree1=new TreeNode(8);
tree1.left=new TreeNode(9);
tree1.right=new TreeNode(2);

var tree2=new TreeNode(8);
tree2.left=new TreeNode(9);

console.log(HasSubtree(tree1,tree2));