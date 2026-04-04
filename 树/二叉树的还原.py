#原教程地址：https://algo.itcharge.cn/05_tree/05_03_binary_tree_reduction/

"""
叉树的还原是数据结构中的重要问题，其核心在于 利用遍历序列的特性来重建树结构。

关键规律：
前序遍历：根节点 → 左子树 → 右子树
中序遍历：左子树 → 根节点 → 右子树
后序遍历：左子树 → 右子树 → 根节点
"""


#代码复现



#前序与中序遍历重建二叉树
class Solution_1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        根据前序遍历和中序遍历序列重建二叉树

        参数:
            preorder: List[int]，二叉树的前序遍历序列
            inorder: List[int]，二叉树的中序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, inorder, n):
            """
            递归构建二叉树

            参数:
                preorder: 当前子树的前序遍历序列
                inorder: 当前子树的中序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为 0
            # 在中序遍历中查找根节点位置
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            # 创建根节点
            node = TreeNode(inorder[k])
            # 递归构建左子树
            node.left = createTree(preorder[1: k + 1], inorder[0: k], k)
            # 递归构建右子树
            node.right = createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)
            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(preorder, inorder, len(inorder))
    


#中序与后序遍历
class Solution_2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        根据中序遍历和后序遍历序列重建二叉树

        参数:
            inorder: List[int]，二叉树的中序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(inorder, postorder, n):
            """
            递归构建二叉树

            参数:
                inorder: 当前子树的中序遍历序列
                postorder: 当前子树的后序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点

            # 后序遍历的最后一个元素为当前子树的根节点
            root_val = postorder[n - 1]
            # 在中序遍历中查找根节点的位置
            k = 0
            while inorder[k] != root_val:
                k += 1

            # 创建根节点
            node = TreeNode(root_val)
            # 递归构建左子树
            # 左子树的中序区间：inorder[0:k]
            # 左子树的后序区间：postorder[0:k]
            node.left = createTree(inorder[0:k], postorder[0:k], k)
            # 递归构建右子树
            # 右子树的中序区间：inorder[k+1:n]
            # 右子树的后序区间：postorder[k:n-1]
            node.right = createTree(inorder[k+1:n], postorder[k:n-1], n - k - 1)
            return node

        # 从整棵树的中序和后序序列开始递归构建
        return createTree(inorder, postorder, len(postorder))
    

#前序与后序（无法唯一确定一棵二叉树）
class Solution_3:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        根据前序和后序遍历序列构造二叉树（不唯一）
        参数:
            preorder: List[int]，二叉树的前序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, postorder, n):
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点
            # 前序遍历的第一个元素为当前子树的根节点
            root_val = preorder[0]
            node = TreeNode(root_val)
            if n == 1:
                return node  # 只有一个节点，直接返回
            # 前序遍历的第二个元素为左子树的根节点
            left_root_val = preorder[1]
            # 在后序遍历中查找左子树根节点的位置
            k = 0
            while postorder[k] != left_root_val:
                k += 1
            # k 为左子树在 postorder 中的结尾索引，左子树节点数为 k+1
            # 划分左右子树的前序和后序区间
            # 左子树：preorder[1:k+2], postorder[0:k+1]
            # 右子树：preorder[k+2:], postorder[k+1:n-1]
            node.left = createTree(preorder[1:k+2], postorder[0:k+1], k+1)
            node.right = createTree(preorder[k+2:], postorder[k+1:n-1], n-k-1)
            return node
        # 从整棵树的前序和后序序列开始递归构建
        return createTree(preorder, postorder, len(preorder))
