#原教程地址：https://algo.itcharge.cn/05_tree/05_04_binary_search_tree/


"""
核心特性
二叉搜索树（BST）是一种 有序的二叉树结构，其核心特性是：
  左子树所有节点值 < 根节点值 < 右子树所有节点值
  中序遍历结果是有序的（递增序列）
  每个节点的左右子树也都是二叉搜索树


算法特点
优点：
查找、插入、删除效率高（平均 O(log n)）
支持范围查询和有序遍历
实现相对简单，易于理解
缺点：
插入顺序影响树的高度和性能
不平衡时可能退化为链表（O(n) 复杂度）
需要额外的平衡机制（如 AVL 树、红黑树）
"""


#代码复现


#查找算法实现
class TreeNode_1:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution_1:
    def searchBST(self, root: TreeNode_1, val: int) -> TreeNode_1:
        """
        在二叉搜索树中查找值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待查找的目标值
        返回:
            TreeNode，值为 val 的节点，如果未找到则返回 None
        """
        if not root:
            return None  # 空树或查找失败，返回 None

        if val == root.val:
            return root  # 找到目标节点，返回
        elif val < root.val:
            # 目标值小于当前节点值，递归查找左子树
            return self.searchBST(root.left, val)
        else:
            # 目标值大于当前节点值，递归查找右子树
            return self.searchBST(root.right, val)
        



#二叉搜索树插入
class TreeNode_2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # 节点值
        self.left = left        # 左子节点
        self.right = right      # 右子节点

class Solution_2:
    def insertIntoBST(self, root: TreeNode_2, val: int) -> TreeNode_2:
        """
        在二叉搜索树中插入一个值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待插入的节点值
        返回:
            TreeNode，插入后的二叉搜索树根节点
        """
        if root is None:
            # 当前子树为空，直接创建新节点并返回
            return TreeNode_2(val)

        if val < root.val:
            # 待插入值小于当前节点值，递归插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 待插入值大于当前节点值，递归插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # 如果 val == root.val，不插入（不允许重复），直接返回原树
        return root        
    



#二叉搜索树的创建
class TreeNode_3:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # 节点值
        self.left = left        # 左子节点
        self.right = right      # 右子节点

class Solution_3:
    def insertIntoBST(self, root: TreeNode_3, val: int) -> TreeNode_3:
        """
        在二叉搜索树中插入一个值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待插入的节点值
        返回:
            TreeNode，插入后的二叉搜索树根节点
        """
        if root is None:
            # 当前子树为空，直接创建新节点并返回
            return TreeNode(val)
        if val < root.val:
            # 待插入值小于当前节点值，递归插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 待插入值大于当前节点值，递归插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # 如果 val == root.val，不插入（不允许重复），直接返回原树
        return root

    def buildBST(self, nums) -> TreeNode_3:
        """
        根据给定数组 nums 创建一棵二叉搜索树

        参数:
            nums: List[int]，待插入的节点值数组
        返回:
            TreeNode，构建好的二叉搜索树根节点
        """
        root = None  # 初始化根节点为空
        for num in nums:
            root = self.insertIntoBST(root, num)  # 依次插入每个元素
        return root    
    

#二插搜索树删除
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, val: int) -> TreeNode:
        """
        在二叉搜索树中删除值为 val 的节点，并返回新的根节点

        参数:
            root: TreeNode，当前子树的根节点
            val: int，待删除的节点值
        返回:
            TreeNode，删除节点后的新根节点
        """
        if not root:
            # 递归终止条件：未找到目标节点，直接返回
            return None

        if val < root.val:
            # 待删除值小于当前节点，递归去左子树删除
            root.left = self.deleteNode(root.left, val)
            return root
        elif val > root.val:
            # 待删除值大于当前节点，递归去右子树删除
            root.right = self.deleteNode(root.right, val)
            return root
        else:
            # 找到目标节点，分三种情况处理
            if not root.left:
                # 情况 1：左子树为空，直接返回右子树
                return root.right
            elif not root.right:
                # 情况 2：右子树为空，直接返回左子树
                return root.left
            else:
                # 情况 3：左右子树均不为空
                # 找到右子树的最左节点（即后继节点）
                successor = root.right
                while successor.left:
                    successor = successor.left
                # 用后继节点的值替换当前节点
                root.val = successor.val
                # 在右子树中递归删除后继节点
                root.right = self.deleteNode(root.right, successor.val)
                return root    