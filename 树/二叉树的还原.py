#原教程地址：https://algo.itcharge.cn/05_tree/05_03_binary_tree_reduction/

"""
"""


#代码复现



#前序与中序遍历重建二叉树
class Solution:
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
    


