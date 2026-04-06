#源地址：https://algo.itcharge.cn/05_tree/05_05_segment_tree_01/


"""
核心要点:
线段树通过对区间反复二分，让每个节点维护一个子区间的聚合信息（如和、最值）。
使用数组顺序存储，容量通常取约4×n，查询/更新沿树高进行。
引入懒惰标记后，区间更新无需遍历到所有叶子，保持对数级复杂度。
聚合函数可配置（sum/max/min/自定义），需满足可结合性以支持自底向上合并。


算法特点:
优点：
区间查询与区间更新效率高（均为O(logn)）。
适配多种聚合函数，扩展性强。
支持动态数据的在线维护。

缺点：
实现复杂度与常数因子较大，代码易错。
对聚合函数有约束（需可结合），不适合不可结合的运算。
多维线段树实现复杂，内存与常数进一步增大；对于简单前缀和/仅单点更新的场景，树状数组往往更简洁高效
"""



#代码复现


# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1          # 区间左边界
        self.right = -1         # 区间右边界
        self.val = val          # 节点值（区间值，如区间和、区间最大值等）
        self.lazy_tag = None    # 区间延迟更新标记（如区间加法、区间赋值等懒惰标记）

# 线段树类
class SegmentTree:
    def __init__(self, nums, function):
        """
        :param nums: 原始数据数组
        :param function: 区间聚合函数（如 sum, max, min 等）
        """
        self.size = len(nums)
        # 线段树最多需要 4 * n 个节点，使用数组存储
        self.tree = [TreeNode() for _ in range(4 * self.size)]
        self.nums = nums
        self.function = function
        if self.size > 0:
            self.__build(0, 0, self.size - 1)

    def __build(self, index, left, right):
        """
        递归构建线段树
        :param index: 当前节点在数组中的下标
        :param left: 当前节点管理的区间左端点
        :param right: 当前节点管理的区间右端点
        """
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            # 叶子节点，直接赋值为原数组对应元素
            self.tree[index].val = self.nums[left]
            return

        mid = left + (right - left) // 2
        left_index = index * 2 + 1      # 左子节点下标
        right_index = index * 2 + 2     # 右子节点下标
        self.__build(left_index, left, mid)         # 构建左子树
        self.__build(right_index, mid + 1, right)   # 构建右子树
        self.__pushup(index)                        # 更新当前节点的区间值

    def __pushup(self, index):
        """
        向上更新当前节点的区间值
        :param index: 当前节点在数组中的下标
        """
        left_index = index * 2 + 1      # 左子节点下标
        right_index = index * 2 + 2     # 右子节点下标
        # 当前节点的区间值由左右子节点的区间值聚合得到
        self.tree[index].val = self.function(
            self.tree[left_index].val,
            self.tree[right_index].val
        )


def update_point(self, i, val):
    """
    单点更新：将原数组 nums[i] 的值修改为 val，并同步更新线段树
    :param i: 需要更新的元素下标
    :param val: 新的值
    """
    self.nums[i] = val  # 更新原数组
    self.__update_point(i, val, 0, 0, self.size - 1)  # 从根节点递归更新线段树

def __update_point(self, i, val, index, left, right):
    """
    递归实现单点更新
    :param i: 需要更新的元素下标
    :param val: 新的值
    :param index: 当前节点在线段树数组中的下标
    :param left: 当前节点管理的区间左端点
    :param right: 当前节点管理的区间右端点
    """
    # 如果到达叶子节点，直接更新节点值
    if self.tree[index].left == self.tree[index].right:
        self.tree[index].val = val  # 叶子节点，节点值修改为 val
        return

    mid = left + (right - left) // 2  # 计算区间中点
    left_index = index * 2 + 1        # 左子节点的下标
    right_index = index * 2 + 2       # 右子节点的下标

    # 判断 i 属于左子树还是右子树，递归更新
    if i <= mid:
        self.__update_point(i, val, left_index, left, mid)  # 在左子树中更新
    else:
        self.__update_point(i, val, right_index, mid + 1, right)  # 在右子树中更新

    self.__pushup(index)  # 向上更新当前节点的区间值





# 区间查询，查询区间 [q_left, q_right] 的区间聚合值
def query_interval_2(self, q_left, q_right):
    """
    查询区间 [q_left, q_right] 的区间聚合值（如区间和、区间最值等）

    :param q_left: 查询区间左端点
    :param q_right: 查询区间右端点
    :return: 区间 [q_left, q_right] 的聚合值
    """
    return self.__query_interval(q_left, q_right, 0, 0, self.size - 1)

# 区间查询的递归实现
def __query_interval(self, q_left, q_right, index, left, right):
    """
    递归查询线段树节点 [left, right] 区间与查询区间 [q_left, q_right] 的交集部分的聚合值

    :param q_left: 查询区间左端点
    :param q_right: 查询区间右端点
    :param index: 当前节点在线段树数组中的下标
    :param left: 当前节点管理的区间左端点
    :param right: 当前节点管理的区间右端点
    :return: 区间 [q_left, q_right] 与 [left, right] 的交集部分的聚合值
    """
    # 情况 1：当前节点区间被查询区间完全覆盖，直接返回节点值
    if left >= q_left and right <= q_right:
        return self.tree[index].val
    # 情况 2：当前节点区间与查询区间无交集，返回单位元（如区间和为 0，区间最小值为正无穷等）
    if right < q_left or left > q_right:
        return 0

    # 情况 3：当前节点区间与查询区间有部分重叠，递归查询左右子区间
    self.__pushdown(index)  # 下推懒惰标记，保证子节点信息正确

    mid = left + (right - left) // 2        # 计算区间中点
    left_index = index * 2 + 1              # 左子节点下标
    right_index = index * 2 + 2             # 右子节点下标
    res_left = 0                            # 左子树查询结果初始化
    res_right = 0                           # 右子树查询结果初始化
    if q_left <= mid:                       # 查询区间与左子区间有交集
        res_left = self.__query_interval(q_left, q_right, left_index, left, mid)
    if q_right > mid:                       # 查询区间与右子区间有交集
        res_right = self.__query_interval(q_left, q_right, right_index, mid + 1, right)
    return self.function(res_left, res_right)  # 合并左右子树结果并返回





#区间赋值（延迟标记）
def update_interval_2(self, q_left, q_right, val):
    """
    对区间 [q_left, q_right] 进行区间赋值操作，将该区间内所有元素修改为 val
    """
    self.__update_interval(q_left, q_right, val, 0, 0, self.size - 1)

def __update_interval_2(self, q_left, q_right, val, index, left, right):
    """
    递归实现区间赋值更新
    参数说明：
        q_left, q_right: 待更新的目标区间
        val: 赋值的目标值
        index: 当前节点在线段树数组中的下标
        left, right: 当前节点所表示的区间范围
    """
    # 情况 1：当前节点区间被 [q_left, q_right] 完全覆盖，直接更新并打懒惰标记
    if left >= q_left and right <= q_right:
        interval_size = (right - left + 1)  # 当前区间长度
        self.tree[index].val = interval_size * val  # 区间所有元素赋值为 val
        self.tree[index].lazy_tag = val             # 打上懒惰标记
        return
    # 情况 2：当前节点区间与 [q_left, q_right] 无交集，直接返回
    if right < q_left or left > q_right:
        return

    # 情况 3：部分重叠，先下推懒惰标记，再递归更新左右子区间
    self.__pushdown(index)

    mid = left + (right - left) // 2            # 区间中点
    left_index = index * 2 + 1                  # 左子节点下标
    right_index = index * 2 + 2                 # 右子节点下标
    if q_left <= mid:                           # 左子区间有交集
        self.__update_interval(q_left, q_right, val, left_index, left, mid)
    if q_right > mid:                           # 右子区间有交集
        self.__update_interval(q_left, q_right, val, right_index, mid + 1, right)

    self.__pushup(index)                        # 回溯时更新当前节点的值


def __pushdown_2(self, index):
    """
    将当前节点的懒惰标记下推到左右子节点，并更新子节点的值
    """
    lazy_tag = self.tree[index].lazy_tag
    if lazy_tag is None:
        return

    left_index = index * 2 + 1                  # 左子节点下标
    right_index = index * 2 + 2                 # 右子节点下标

    # 更新左子节点的懒惰标记和值
    self.tree[left_index].lazy_tag = lazy_tag
    left_size = self.tree[left_index].right - self.tree[left_index].left + 1
    self.tree[left_index].val = lazy_tag * left_size

    # 更新右子节点的懒惰标记和值
    self.tree[right_index].lazy_tag = lazy_tag
    right_size = self.tree[right_index].right - self.tree[right_index].left + 1
    self.tree[right_index].val = lazy_tag * right_size

    # 清除当前节点的懒惰标记
    self.tree[index].lazy_tag = None






# 区间更新，将区间 [q_left, q_right] 上的所有元素增加 val,区间加减操作（延迟标记）
def update_interval_3(self, q_left, q_right, val):
    """
    对区间 [q_left, q_right] 内的所有元素增加 val
    """
    self.__update_interval(q_left, q_right, val, 0, 0, self.size - 1)

def __update_interval_3(self, q_left, q_right, val, index, left, right):
    """
    递归实现区间加法更新
    参数:
        q_left, q_right: 待更新的区间范围
        val: 增加的值
        index: 当前节点在线段树数组中的下标
        left, right: 当前节点所表示的区间范围
    """
    # 情况 1：当前节点区间被 [q_left, q_right] 完全覆盖，直接打懒惰标记并更新区间和
    if left >= q_left and right <= q_right:
        interval_size = right - left + 1  # 当前节点区间长度
        if self.tree[index].lazy_tag is not None:
            self.tree[index].lazy_tag += val  # 累加懒惰标记
        else:
            self.tree[index].lazy_tag = val   # 新建懒惰标记
        self.tree[index].val += val * interval_size  # 区间和增加
        return

    # 情况2：当前节点区间与 [q_left, q_right] 无交集，直接返回
    if right < q_left or left > q_right:
        return

    # 情况3：部分重叠，先下推懒惰标记，再递归更新左右子区间
    self.__pushdown(index)

    mid = left + (right - left) // 2
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    if q_left <= mid:
        self.__update_interval(q_left, q_right, val, left_index, left, mid)
    if q_right > mid:
        self.__update_interval(q_left, q_right, val, right_index, mid + 1, right)

    self.__pushup(index)  # 回溯时更新当前节点的区间和

def __pushdown_3(self, index):
    """
    将当前节点的懒惰标记下推到左右子节点，并同步更新子节点的区间和
    """
    lazy_tag = self.tree[index].lazy_tag
    if lazy_tag is None:
        return

    left_index = index * 2 + 1
    right_index = index * 2 + 2

    # 处理左子节点
    if self.tree[left_index].lazy_tag is not None:
        self.tree[left_index].lazy_tag += lazy_tag
    else:
        self.tree[left_index].lazy_tag = lazy_tag
    left_size = self.tree[left_index].right - self.tree[left_index].left + 1
    self.tree[left_index].val += lazy_tag * left_size

    # 处理右子节点
    if self.tree[right_index].lazy_tag is not None:
        self.tree[right_index].lazy_tag += lazy_tag
    else:
        self.tree[right_index].lazy_tag = lazy_tag
    right_size = self.tree[right_index].right - self.tree[right_index].left + 1
    self.tree[right_index].val += lazy_tag * right_size

    # 清除当前节点的懒惰标记
    self.tree[index].lazy_tag = None



