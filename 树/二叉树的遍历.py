#原教程地址：https://algo.itcharge.cn/05_tree/05_02_binary_tree_traverse/

"""
优缺点分析

前序遍历
优点：
递归实现简单直观，易于理解
适合需要先处理根节点再处理子节点的场景
常用于树的复制、序列化等操作
缺点：
非递归实现需要特别注意入栈顺序
对于深度很大的树，递归可能导致栈溢出

中序遍历
优点：
对于二叉搜索树，中序遍历得到有序序列
递归实现逻辑清晰
适合需要按顺序处理节点的场景
缺点：
非递归实现相对复杂
需要理解"左-根-右"的访问时机

后序遍历
优点：
适合需要先处理子节点再处理父节点的场景
常用于树的删除、后序表达式计算等
递归实现简单
缺点：
非递归实现最复杂，需要额外的访问状态标记
理解难度较高

层序遍历
优点：
直观反映树的层次结构
适合需要按层处理节点的场景
非递归实现相对简单
缺点：
不适用于递归实现
空间复杂度可能较高（对于宽树
"""


#代码复现

#定义二叉树实现类
class TreeNode:
    """
    二叉树节点定义（链式存储结构）

    属性:
        val: 节点存储的值
        left: 指向左子节点的指针（无左子节点时为 None）
        right: 指向右子节点的指针（无右子节点时为 None）
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # 节点的值
        self.left = left        # 左子节点指针
        self.right = right      # 右子节点指针


#前序遍历递归实现
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树的前序遍历（递归实现）
        参数:
            root: TreeNode，二叉树的根节点
        返回:
            List[int]，前序遍历的节点值列表
        """
        res = []  # 用于存储遍历结果

        def preorder(node):
            if not node:
                return  # 递归终止条件：节点为空
            res.append(node.val)      # 1. 访问根节点
            preorder(node.left)       # 2. 递归遍历左子树
            preorder(node.right)      # 3. 递归遍历右子树

        preorder(root)  # 从根节点开始递归
        return res



#非递归（显式栈）   
class Solution_2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        二叉树的前序遍历（非递归/显式栈实现）
        参数:
            root: Optional[TreeNode]，二叉树的根节点
        返回:
            List[int]，前序遍历的节点值列表
        """
        if not root:  # 特判：二叉树为空，直接返回空列表
            return []

        res = []              # 用于存储遍历结果
        stack = [root]        # 初始化栈，根节点先入栈

        while stack:          # 当栈不为空时循环
            node = stack.pop()        # 弹出栈顶节点
            res.append(node.val)      # 访问当前节点（根节点）
            # 注意：先右后左，保证左子树先被遍历
            if node.right:            # 如果右子节点存在，先将其入栈
                stack.append(node.right)
            if node.left:             # 如果左子节点存在，再将其入栈
                stack.append(node.left)

        return res  # 返回前序遍历结果
    

#二叉树中序遍历（递归）
class Solution_3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树中序遍历（递归实现）

        参数:
            root: TreeNode，二叉树的根节点
        返回:
            List[int]，中序遍历的节点值列表
        """
        res = []  # 用于存储遍历结果

        def inorder(node):
            if not node:
                return  # 递归终止条件：节点为空
            inorder(node.left)         # 递归遍历左子树
            res.append(node.val)       # 访问当前节点
            inorder(node.right)        # 递归遍历右子树

        inorder(root)  # 从根节点开始递归
        return res     # 返回中序遍历结果


#中序遍历（非递归）
class Solution_4:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        二叉树中序遍历（非递归/显式栈实现）

        参数:
            root: Optional[TreeNode]，二叉树的根节点
        返回:
            List[int]，中序遍历的节点值列表
        """
        res = []    # 用于存储遍历结果
        stack = []  # 显式栈，用于模拟递归过程
        cur = root  # 当前遍历的节点指针

        while cur or stack:  # 只要当前节点不为空或栈不为空就继续
            # 不断向左子树深入，将沿途节点全部入栈
            while cur:
                stack.append(cur)      # 当前节点入栈
                cur = cur.left         # 继续遍历左子树

            # 此时已到达最左侧，弹出栈顶节点
            node = stack.pop()         # 弹出最左侧节点
            res.append(node.val)       # 访问该节点（中序遍历的「根」）
            cur = node.right           # 转向右子树，继续上述过程

        return res



#后序遍历（递归实现）
class Solution_5:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树后序遍历（递归实现）
        参数:
            root: TreeNode，二叉树的根节点
        返回:
            List[int]，后序遍历的节点值列表
        """
        res = []  # 用于存储遍历结果

        def postorder(node):
            if not node:
                return
            # 递归遍历左子树
            postorder(node.left)
            # 递归遍历右子树
            postorder(node.right)
            # 访问当前节点
            res.append(node.val)

        postorder(root)
        return res
    


#后序遍历（非递归）
class Solution_6:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        二叉树后序遍历（非递归/显式栈实现）
        参数:
            root: Optional[TreeNode]，二叉树的根节点
        返回:
            List[int]，后序遍历的节点值列表
        """
        res = []        # 用于存储遍历结果
        stack = []      # 显式栈，用于模拟递归过程
        prev = None     # 记录上一个访问的节点，用于判断右子树是否已访问

        while root or stack:  # 只要当前节点不为空或栈不为空就继续遍历
            # 一直向左走，将所有左子节点入栈
            while root:
                stack.append(root)      # 当前节点入栈
                root = root.left        # 继续遍历左子树

            node = stack.pop()          # 弹出栈顶节点，准备访问或遍历其右子树

            # 判断是否可以访问当前节点
            # 1. 没有右子树
            # 2. 右子树已经访问过（即上一次访问的节点是当前节点的右子节点）
            if not node.right or node.right == prev:
                res.append(node.val)    # 访问当前节点
                prev = node             # 更新上一次访问的节点
                root = None             # 当前节点已访问，重置root，防止重复入栈
            else:
                # 右子树还未访问，当前节点重新入栈，转而遍历右子树
                stack.append(node)
                root = node.right

        return res
    


#层序遍历
class Solution_7:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        二叉树层序遍历（广度优先搜索，BFS）
        返回每一层的节点值组成的二维列表
        """
        if not root:
            return []  # 空树直接返回空列表

        from collections import deque  # 推荐使用 deque 提高队列效率
        queue = deque([root])  # 初始化队列，根节点入队
        order = []             # 用于存储最终结果

        while queue:
            level = []                 # 存储当前层的节点值
            size = len(queue)          # 当前层的节点数量
            for _ in range(size):
                curr = queue.popleft() # 弹出队首节点
                level.append(curr.val) # 访问当前节点
                if curr.left:
                    queue.append(curr.left)   # 左子节点入队
                if curr.right:
                    queue.append(curr.right)  # 右子节点入队
            if level:
                order.append(level)     # 当前层结果加入总结果

        return order    