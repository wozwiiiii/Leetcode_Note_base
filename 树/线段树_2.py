#原教程地址：https://algo.itcharge.cn/05_tree/05_06_segment_tree_02/


"""
该节教程主要总结了一些题目类型的解法

"""



#代码复现
# 动态开点线段树节点类
class TreeNode:
    def __init__(self, left=-1, right=-1, val=0):
        self.left = left                            # 区间左边界
        self.right = right                          # 区间右边界
        self.mid = left + (right - left) // 2       # 区间中点
        self.leftNode = None                        # 左子节点
        self.rightNode = None                       # 右子节点
        self.val = val                              # 区间聚合值
        self.lazy_tag = None                        # 懒惰标记（延迟更新）

# 动态开点线段树
class SegmentTree:
    def __init__(self, function):
        self.tree = TreeNode(0, int(1e9))           # 根节点，维护区间 [0, 1e9]
        self.function = function                    # 区间聚合函数（如 sum, max, min）

    def __pushup(self, node):
        """
        向上更新当前节点的区间值，由左右子节点聚合得到
        """
        leftNode = node.leftNode
        rightNode = node.rightNode
        if leftNode and rightNode:
            node.val = self.function(leftNode.val, rightNode.val)
        elif leftNode:
            node.val = leftNode.val
        elif rightNode:
            node.val = rightNode.val
        # 如果左右子节点都不存在，val 保持不变

    def update_point(self, i, val):
        """
        单点更新：将下标 i 的元素修改为 val
        """
        self.__update_point(i, val, self.tree)

    def __update_point(self, i, val, node):
        """
        递归实现单点更新
        """
        if node.left == node.right:
            node.val = val                          # 叶子节点，直接赋值
            node.lazy_tag = None                    # 清除懒惰标记
            return

        self.__pushdown(node)                       # 下推懒惰标记，保证更新正确

        if i <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_point(i, val, node.leftNode)
        else:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         # 向上更新

    def query_interval(self, q_left, q_right):
        """
        区间查询：[q_left, q_right] 区间的聚合值
        """
        return self.__query_interval(q_left, q_right, self.tree)

    def __query_interval(self, q_left, q_right, node):
        """
        递归实现区间查询
        """
        if node.left > q_right or node.right < q_left:
            # 当前节点区间与查询区间无交集
            return 0
        if node.left >= q_left and node.right <= q_right:
            # 当前节点区间被查询区间完全覆盖
            return node.val

        self.__pushdown(node)                       # 下推懒惰标记

        res_left = 0
        res_right = 0
        if q_left <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果

    def update_interval(self, q_left, q_right, val):
        """
        区间更新：将 [q_left, q_right] 区间内所有元素增加 val
        """
        self.__update_interval(q_left, q_right, val, self.tree)

    def __update_interval(self, q_left, q_right, val, node):
        """
        递归实现区间更新（区间加法）
        """
        if node.left > q_right or node.right < q_left:
            # 当前节点区间与更新区间无交集
            return

        if node.left >= q_left and node.right <= q_right:
            # 当前节点区间被更新区间完全覆盖
            interval_size = node.right - node.left + 1
            if node.lazy_tag is not None:
                node.lazy_tag += val
            else:
                node.lazy_tag = val
            node.val += val * interval_size
            return

        self.__pushdown(node)                       # 下推懒惰标记

        if q_left <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_interval(q_left, q_right, val, node.rightNode)

        self.__pushup(node)                         # 向上更新

    def __pushdown(self, node):
        """
        懒惰标记下推：将当前节点的延迟更新传递给左右子节点
        """
        if node.lazy_tag is None:
            return

        # 动态创建左右子节点
        if not node.leftNode:
            node.leftNode = TreeNode(node.left, node.mid)
        if not node.rightNode:
            node.rightNode = TreeNode(node.mid + 1, node.right)

        # 更新左子节点
        left_size = node.leftNode.right - node.leftNode.left + 1
        if node.leftNode.lazy_tag is not None:
            node.leftNode.lazy_tag += node.lazy_tag
        else:
            node.leftNode.lazy_tag = node.lazy_tag
        node.leftNode.val += node.lazy_tag * left_size

        # 更新右子节点
        right_size = node.rightNode.right - node.rightNode.left + 1
        if node.rightNode.lazy_tag is not None:
            node.rightNode.lazy_tag += node.lazy_tag
        else:
            node.rightNode.lazy_tag = node.lazy_tag
        node.rightNode.val += node.lazy_tag * right_size

        node.lazy_tag = None                        # 清除当前节点的懒惰标记