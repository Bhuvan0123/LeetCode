"""
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], 
then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two 
children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

 """
 
def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        rev=False
        while q:
            qz=len(q)
            arr=[]
            for i in range(qz):
                Node=q.popleft()
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
                if rev:
                    arr.append(Node)
                    if i>=qz/2:
                        arr[i].val, arr[qz-1-i].val=arr[qz-1-i].val, arr[i].val
            rev=not rev
        return root
