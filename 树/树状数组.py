#原教程地址：https://algo.itcharge.cn/05_tree/05_07_binary_indexed_tree/

"""
并查集的算法分析
时间复杂度：在同时使用「路径压缩」和「按秩合并」优化后，合并（union）和查找（find）操作的均摊时间复杂度非常接近 O(1)。
更精确地说，m 次操作的总时间复杂度为 O(m×α(n))，其中 α(n) 是阿克曼函数的反函数，增长极其缓慢，实际应用中可视为常数。
空间复杂度：主要由数组fa（父节点数组）构成，如果采用「按秩合并」优化，还需额外的rank 或size 数组。整体空间复杂度为O(n)，其中n 为元素个数


并查集的推荐实现方式
推荐并查集的实现策略如下：优先采用「隔代压缩」优化，一般情况下无需引入「按秩合并」。
这种做法的优势在于代码简洁、易于实现，同时性能表现也非常优秀。
只有在遇到性能瓶颈时，再考虑引入「按秩合并」进一步优化。
"""


#代码复写


#树状数组的建立
class BinaryIndexedTree_1:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def build(self, arr):
        for i in range(len(arr)):
            self.update(i + 1, arr[i])


#树状数组的修改
    def update(self,index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)

#树状数组的求和
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res



#树状数组的应用

#单点更新+区间求值
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)

# 使用示例
def example_single_point_update():
    # 初始化数组 [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    bit = BinaryIndexedTree(n)
    
    # 构建树状数组
    for i in range(n):
        bit.update(i + 1, arr[i])
    
    # 单点更新：将第3个元素加2
    bit.update(3, 2)  # arr[2] += 2
    
    # 查询区间和：查询[2,4]的和
    sum_range = bit.query_range(2, 4)
    print(f"区间[2,4]的和为：{sum_range}")  # 输出：区间[2,4]的和为：11




#区间更新+单点求值
class RangeUpdateBIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def range_update(self, left, right, val):
        # 在left位置加上val
        self.update(left, val)
        # 在right+1位置减去val
        self.update(right + 1, -val)

# 使用示例
def example_range_update():
    # 初始化数组 [0, 0, 0, 0, 0]
    n = 5
    bit = RangeUpdateBIT(n)
    
    # 区间更新：[2,4]区间所有元素加3
    bit.range_update(2, 4, 3)
    
    # 单点查询：查询第3个元素的值
    value = bit.query(3)
    print(f"第3个元素的值为：{value}")  # 输出：第3个元素的值为：3




#求逆序对数
class InversionCountBIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def count_inversions(self, arr):
        # 离散化处理
        sorted_arr = sorted(set(arr))
        rank = {val: i + 1 for i, val in enumerate(sorted_arr)}
        
        # 从后向前遍历，统计逆序对
        count = 0
        for i in range(len(arr) - 1, -1, -1):
            # 查询当前数前面比它大的数的个数
            count += self.query(rank[arr[i]] - 1)
            # 更新当前数的出现次数
            self.update(rank[arr[i]], 1)
        
        return count

# 使用示例
def example_inversion_count():
    # 测试数组 [5, 2, 6, 1, 3]
    arr = [5, 2, 6, 1, 3]
    n = len(arr)
    bit = InversionCountBIT(n)
    
    # 计算逆序对数量
    inversions = bit.count_inversions(arr)
    print(f"数组中的逆序对数量为：{inversions}")  # 输出：数组中的逆序对数量为：6



#快速查询（数组结构）
class UnionFind_3:
    def __init__(self, n):
        """
        初始化并查集，将每个元素的集合编号初始化为其自身下标。
        :param n: 元素总数
        """
        self.ids = [i for i in range(n)]  # ids[i] 表示元素 i 所在集合的编号

    def find(self, x):
        """
        查找元素 x 所在集合的编号。
        :param x: 元素编号
        :return: x 所在集合的编号
        """
        return self.ids[x]

    def union(self, x, y):
        """
        合并包含元素 x 和 y 的两个集合。
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果 x 和 y 原本就在同一集合，返回 False；否则合并并返回 True
        """
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            # x 和 y 已经在同一个集合，无需合并
            return False

        # 遍历所有元素，将属于 y_id 集合的元素编号改为 x_id，实现合并
        for i in range(len(self.ids)):
            if self.ids[i] == y_id:
                self.ids[i] = x_id
        return True

    def is_connected(self, x, y):
        """
        判断元素 x 和 y 是否属于同一个集合。
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果属于同一集合返回 True，否则返回 False
        """
        return self.find(x) == self.find(y)    
    


#快速查询（基于森林实现）
class UnionFind_4:
    def __init__(self, n):
        """
        初始化并查集，将每个元素的父节点初始化为自身
        :param n: 元素个数
        """
        self.fa = [i for i in range(n)]  # fa[x] 表示 x 的父节点，初始时每个节点自成一个集合

    def find(self, x):
        """
        查找元素 x 所在集合的根节点（代表元）
        :param x: 待查找的元素
        :return: x 所在集合的根节点编号
        """
        # 循环查找父节点，直到找到根节点（fa[x] == x）
        while self.fa[x] != x:
            x = self.fa[x]
        return x

    def union(self, x, y):
        """
        合并 x 和 y 所在的两个集合
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果 x 和 y 原本属于同一集合，返回 False；否则合并并返回 True
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # x 和 y 已经在同一个集合中，无需合并
            return False
        self.fa[root_x] = root_y  # 将 x 的根节点连接到 y 的根节点
        return True

    def is_connected(self, x, y):
        """
        判断 x 和 y 是否属于同一个集合
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果属于同一集合返回 True，否则返回 False
        """
        return self.find(x) == self.find(y)



#隔代压缩的查找
def find(self, x):
    """
    查找元素 x 所在集合的根节点（带隔代路径压缩）
    :param x: 待查找的元素
    :return: x 所在集合的根节点编号
    """
    while self.fa[x] != x:
        # 将 x 的父节点直接指向其祖父节点，实现隔代压缩
        self.fa[x] = self.fa[self.fa[x]]
        x = self.fa[x]  # 继续向上查找
    return x  # 返回根节点编号



#完全压缩
def find_2(self, x):
    """
    查找元素 x 所在集合的根节点（带完全路径压缩）
    :param x: 待查找的元素
    :return: x 所在集合的根节点编号
    """
    if self.fa[x] != x:                             # 如果 x 不是根节点，递归查找其父节点
        self.fa[x] = self.find(self.fa[x])          # 路径压缩：将 x 直接连接到根节点
    return self.fa[x]                               # 返回根节点编号




#按深度合并
class UnionFind_1:
    def __init__(self, n):
        """
        初始化并查集
        :param n: 元素个数
        """
        self.fa = [i for i in range(n)]     # fa[i] 表示元素 i 的父节点，初始时每个元素自成一个集合
        self.rank = [1 for _ in range(n)]   # rank[i] 表示以 i 为根的树的深度，初始为 1

    def find(self, x):
        """
        查找元素 x 所在集合的根节点（带路径压缩，隔代压缩）
        :param x: 待查找的元素
        :return: x 所在集合的根节点编号
        """
        while self.fa[x] != x:              # 如果 x 不是根节点，继续查找其父节点
            self.fa[x] = self.fa[self.fa[x]]# 路径压缩：将 x 直接连接到祖父节点，实现隔代压缩
            x = self.fa[x]
        return x                            # 返回根节点编号

    def union(self, x, y):
        """
        合并操作：将 x 和 y 所在的集合合并
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果合并成功返回 True，如果已在同一集合返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:                # x 和 y 已经在同一个集合
            return False

        # 按秩合并：将深度较小的树合并到深度较大的树下
        if self.rank[root_x] < self.rank[root_y]:
            self.fa[root_x] = root_y        # x 的根节点连接到 y 的根节点
        elif self.rank[root_x] > self.rank[root_y]:
            self.fa[root_y] = root_x        # y 的根节点连接到 x 的根节点
        else:
            self.fa[root_x] = root_y        # 深度相同，任选一方作为新根
            self.rank[root_y] += 1          # 新根的深度加 1
        return True

    def is_connected(self, x, y):
        """
        查询操作：判断 x 和 y 是否属于同一个集合
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果属于同一集合返回 True，否则返回 False
        """
        return self.find(x) == self.find(y)
    



#按大小合并
class UnionFind_2:
    def __init__(self, n):
        """
        初始化并查集
        :param n: 元素个数
        """
        self.fa = [i for i in range(n)]     # fa[i] 表示元素 i 的父节点，初始时每个元素自成一个集合
        self.size = [1 for _ in range(n)]   # size[i] 表示以 i 为根的集合的元素个数，初始为 1

    def find(self, x):
        """
        查找元素 x 所在集合的根节点（带隔代路径压缩）
        :param x: 待查找的元素
        :return: x 所在集合的根节点编号
        """
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]  # 隔代路径压缩，将 x 直接连接到祖父节点
            x = self.fa[x]
        return x

    def union(self, x, y):
        """
        合并操作：将 x 和 y 所在的集合合并（按集合大小合并）
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果合并成功返回 True，如果已在同一集合返回 False
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # x 和 y 已经在同一个集合，无需合并

        # 按集合大小合并：小集合合并到大集合
        if self.size[root_x] < self.size[root_y]:
            self.fa[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.size[root_x] > self.size[root_y]:
            self.fa[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            # 集合大小相等，任选一方作为新根
            self.fa[root_x] = root_y
            self.size[root_y] += self.size[root_x]

        return True

    def is_connected(self, x, y):
        """
        查询操作：判断 x 和 y 是否属于同一个集合
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果属于同一集合返回 True，否则返回 False
        """
        return self.find(x) == self.find(y)




#「隔代压缩」且不使用「按秩合并」的并查集实现
class UnionFind_gedaiyasuo_bushiyong_anzhihebing:
    def __init__(self, n):                          # 初始化
        self.fa = [i for i in range(n)]             # 每个元素的集合编号初始化为数组 fa 的下标索引
    
    def find(self, x):                              # 查找元素根节点的集合编号内部实现方法
        while self.fa[x] != x:                      # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.fa[self.fa[x]]        # 隔代压缩优化
            x = self.fa[x]
        return x                                    # 返回元素根节点的集合编号

    def union(self, x, y):                          # 合并操作：令其中一个集合的树根节点指向另一个集合的树根节点
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:                        # x 和 y 的根节点集合编号相同，说明 x 和 y 已经同属于一个集合
            return False
        
        self.fa[root_x] = root_y                    # x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.find(x) == self.find(y)
    



#「隔代压缩」，使用「按秩合并」的并查集
class UnionFind_gedaiyasuo_and_anzhihebing:
    def __init__(self, n):                          # 初始化
        self.fa = [i for i in range(n)]             # 每个元素的集合编号初始化为数组 fa 的下标索引
        self.rank = [1 for i in range(n)]           # 每个元素的深度初始化为 1
    
    def find(self, x):                              # 查找元素根节点的集合编号内部实现方法
        while self.fa[x] != x:                      # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.fa[self.fa[x]]        # 隔代压缩优化
            x = self.fa[x]
        return x                                    # 返回元素根节点的集合编号

    def union(self, x, y):                          # 合并操作：令其中一个集合的树根节点指向另一个集合的树根节点
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:                        # x 和 y 的根节点集合编号相同，说明 x 和 y 已经同属于一个集合
            return False
        
        if self.rank[root_x] < self.rank[root_y]:   # x 的根节点对应的树的深度 小于 y 的根节点对应的树的深度
            self.fa[root_x] = root_y                # x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        elif self.rank[root_x] > self.rank[root_y]: # x 的根节点对应的树的深度 大于 y 的根节点对应的树的深度
            self.fa[root_y] = root_x                # y 的根节点连接到 x 的根节点上，成为 x 的根节点的子节点
        else:                                       # x 的根节点对应的树的深度 等于 y 的根节点对应的树的深度
            self.fa[root_x] = root_y                # 向任意一方合并即可
            self.rank[root_y] += 1                  # 因为层数相同，被合并的树必然层数会 +1
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.find(x) == self.find(y)
    


    