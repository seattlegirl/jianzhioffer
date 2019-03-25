function TreeNode(x) {
    this.val = x;
    this.left = null;
    this.right = null;
} 
function reConstructBinaryTree(pre, vin)
{
    // write code here
    if(pre.length===0 || vin.length===0){
        return null;
    }
    var node=new TreeNode(pre[0]);
    node.left=reConstructBinaryTree(pre.slice(1,vin.indexOf(pre[0])+1),vin.slice(0,vin.indexOf(pre[0])));
    node.right=reConstructBinaryTree(pre.slice(vin.indexOf(pre[0])+1),vin.slice(index+1));
    return node;
}