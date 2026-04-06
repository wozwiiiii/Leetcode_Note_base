#源地址：https://algo.itcharge.cn/06_graph/06_02_graph_structure/


"""
邻接矩阵的算法分析
时间复杂度：
初始化：O(n^2)。需要为 n 个顶点分配 n×n 的二维数组空间。
查询、添加或删除一条边：O(1)。通过下标即可直接访问和修改边的信息。
获取某个顶点的所有邻接边：O(n)。需遍历该顶点所在的整行或整列。
遍历整张图：O(n^2)。需要访问整个邻接矩阵。

空间复杂度：
O(n^2)。无论实际边数多少，均需分配n×n 的空间。




邻接表的算法分析
时间复杂度分析：
图的初始化与创建：O(n+m)，其中 n 表示顶点数，m 表示边数。
因为需要为每个顶点分配空间，并依次插入每条边。

查询是否存在Vi到Vj 的边：O(TD(Vi))，其中TD(Vi)表示顶点Vi的出度。
由于邻接表只存储与Vi直接相连的边，因此需要遍历Vi的所有邻接点，最坏情况下需遍历Vi的全部出边。

遍历某个顶点的所有边：O(TD(Vi))，即与该顶点相连的所有边都需访问一遍，效率较高。
遍历整张图的所有边：O(n+m)。遍历所有顶点，每个顶点的邻接表总共包含 m 条边，因此整体遍历代价为 O(n+m)。

空间复杂度分析：
O(n+m)，邻接表需要为每个顶点分配一个链表头结点（O(n)），并为每条边分配一个边节点O(m)），因此总空间复杂度为O(n+m)。
相比邻接矩阵，邻接表在稀疏图中能显著节省空间




链式前向星的算法分析
时间复杂度：
图的初始化和创建操作：O(n+m)，其中 n 表示顶点数，m 表示边数。
初始化时需要为每个顶点分配空间，并依次插入每条边，因此总耗时与顶点和边的数量成线性关系。

查询是否存在Vi到Vj的边：TD(Vi)，其中TD(Vi)表示顶点Vi的出度。
因为链式前向星存储结构需要遍历Vi的所有出边才能判断是否存在到Vj的边，最坏情况下需要遍历Vi的所有出边。

遍历某个点的所有边：O(TD(Vi))。由于每个顶点的出边在链表中连续存储，遍历时只需顺序访问即可，效率较高。
遍历整张图的所有边：O(n+m)。遍历所有顶点并依次访问每个顶点的所有出边，总共访问 n 个顶点和 m 条边，整体复杂度为线性。

空间复杂度：
O(n+m)。需要为每个顶点分配一个头指针（O(n)），并为每条边分配一个边节点（O(m)），因此总空间消耗与顶点数和边数之和成正比。




哈希表实现邻接表的算法分析
时间复杂度：
图的初始化与构建：O(n+m)，其中 n 表示顶点数，m 表示边数。每个顶点的邻接表初始化为 O(n)，每条边的插入操作为 O(1)，总共 m 条边，因此整体为O(n+m)。
边的存在性查询：O(1)。判断是否存在从Vi到Vj的边，利用哈希表查找，平均时间复杂度为 O(1)，即常数时间即可完成。
遍历某一顶点的所有邻接边：遍历顶点Vi的所有出边，时间复杂度为TD(Vi)，其中TD(Vi) 表示顶点Vi的出度（即邻接点个数）。这是因为只需顺序访问该顶点邻接表中的所有元素。
遍历整张图的所有边：遍历所有顶点及其邻接表，整体时间复杂度为 O(n+m)。O(n) 用于访问所有顶点，O(m) 用于访问所有边。

空间复杂度：
O(n+m)，其中 O(n) 用于存储所有顶点的邻接表结构，O(m) 用于存储所有边的信息。相比邻接矩阵，邻接表在稀疏图（m≪n^2）时能显著节省空间。



在邻接表实现之后为图论题目总结，详见原教程地址
"""


#代码复现


#邻接矩阵
class Graph_1:                                       # 邻接矩阵实现的图
    def __init__(self, ver_count, directed=False, inf=float('inf')):
        self.n = ver_count                         # 顶点数量 n
        self.directed = directed                   # 是否为有向图
        self.inf = inf                             # 无边时的填充值（带权图用 ∞ 表示无边）
        # 邻接矩阵，采用 1..n 顶点编号；0 号行列弃用，便于直观
        self.adj = [[inf] * (ver_count + 1) for _ in range(ver_count + 1)]
        for i in range(1, ver_count + 1):
            self.adj[i][i] = 0                    # 自环距离为 0（无权图也可视作 0）

    def add_edge(self, vi, vj, w=1):               # 添加边 vi -> vj，权重默认为 1
        self.adj[vi][vj] = w
        if not self.directed:                      # 无向图需要对称赋值
            self.adj[vj][vi] = w

    def get_edge(self, vi, vj):                    # 查询边权，不存在返回 None
        if self.adj[vi][vj] != self.inf:
            return self.adj[vi][vj]
        return None

    def printMatrix(self):                         # 打印邻接矩阵，∞ 表示无边
        for i in range(1, self.n + 1):
            row = [self.adj[i][j] if self.adj[i][j] != self.inf else '∞' for j in range(1, self.n + 1)]
            print(' '.join(map(str, row)))


# 示例：构建一个有向带权图，并进行查询与打印
graph = Graph_1(6, directed=True)
edges = [(1, 2, 5), (1, 5, 6), (2, 4, 7), (4, 3, 9), (3, 1, 2), (5, 6, 8), (6, 4, 3)]
for u, v, w in edges:
    graph.add_edge(u, v, w)

print(graph.get_edge(4, 3))   # 输出 9（存在边 4->3，权重 9）
print(graph.get_edge(4, 5))   # 输出 None（不存在边 4->5）
graph.printMatrix()           # 打印 6x6 邻接矩阵




#邻接表
class EdgeNode_2:                                 # 边结点：存储终点、权值与下一条边
    def __init__(self, vj, val):
        self.vj = vj                            # 边的终点
        self.val = val                          # 边的权值（无权图可默认 1）
        self.next = None                        # 指向下一条同起点的边

class VertexNode_2:                               # 顶点结点：存储顶点编号与其第一条邻接边
    def __init__(self, vi):
        self.vi = vi                            # 顶点编号
        self.head = None                        # 指向该顶点的第一条邻接边

class Graph_2:                                    # 邻接表实现的图
    def __init__(self, ver_count, directed=False):
        self.n = ver_count                      # 顶点数量 n
        self.directed = directed                # 是否为有向图
        # 使用 1..n 的顶点编号，0 号位置空置，便于直观
        self.vertices = [None] + [VertexNode_2(i) for i in range(1, ver_count + 1)]

    def _valid(self, v):                        # 顶点合法性检查
        return 1 <= v <= self.n

    def add_edge(self, vi, vj, val=1):          # 添加边 vi -> vj，权重默认 1
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError("invalid vertex: {} or {}".format(vi, vj))
        edge = EdgeNode_2(vj, val)                # 头插法加入邻接链表
        edge.next = self.vertices[vi].head
        self.vertices[vi].head = edge
        if not self.directed:                   # 无向图需要加反向边
            rev = EdgeNode_2(vi, val)
            rev.next = self.vertices[vj].head
            self.vertices[vj].head = rev

    def get_edge(self, vi, vj):                 # 查询 vi -> vj 的边权，如果无边返回 None
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError("invalid vertex: {} or {}".format(vi, vj))
        cur = self.vertices[vi].head
        while cur:
            if cur.vj == vj:
                return cur.val
            cur = cur.next
        return None

    def neighbors(self, vi):                    # 遍历顶点 vi 的所有邻接边 (vj, val)
        cur = self.vertices[vi].head
        while cur:
            yield cur.vj, cur.val
            cur = cur.next

    def printGraph(self):                       # 打印所有边
        for vi in range(1, self.n + 1):
            cur = self.vertices[vi].head
            while cur:
                print(str(vi) + ' - ' + str(cur.vj) + ' : ' + str(cur.val))
                cur = cur.next


# 示例：构建有向带权图并查询/打印
graph = Graph_2(6, directed=True)
edges = [(1, 2, 5), (1, 5, 6), (2, 4, 7), (4, 3, 9), (3, 1, 2), (5, 6, 8), (6, 4, 3)]
for u, v, w in edges:
    graph.add_edge(u, v, w)

print(graph.get_edge(4, 3))   # 9
print(graph.get_edge(4, 5))   # None（无此边）
graph.printGraph()





#链式前向星
class EdgeNode_3:
    """边信息类，存储终点、权值和下一条边的下标"""
    def __init__(self, vj, val, next_idx):
        self.vj = vj        # 边的终点
        self.val = val      # 边的权值
        self.next = next_idx  # 下一条边在边集数组中的下标

class Graph_3:
    """链式前向星图结构"""
    def __init__(self, ver_count):
        self.n = ver_count          # 顶点个数
        self.head = [-1] * self.n   # 头节点数组，head[i]为顶点i的第一条出边下标
        self.edges = []             # 边集数组

    def _valid(self, v):
        """判断顶点编号是否合法（0 ~ n - 1）"""
        return 0 <= v < self.n

    def add_edge(self, vi, vj, val):
        """
        添加一条边 vi -> vj，权值为 val
        vi, vj 均为 0 ~ n - 1 的顶点编号
        """
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError(f"{vi} 或 {vj} 不是有效顶点编号")
        # 新边的 next 指向 vi 原来的第一条出边
        edge = EdgeNode_3(vj, val, self.head[vi])
        self.edges.append(edge)
        self.head[vi] = len(self.edges) - 1  # head[vi] 指向新加边的下标

    def build(self, edge_list):
        """批量建图，edge_list 为 [(vi, vj, val), ...]，顶点编号从 1 开始"""
        for vi, vj, val in edge_list:
            # 由于输入的顶点编号是从 1 开始，内部实现是从 0 开始，所以需要减 1
            self.add_edge(vi - 1, vj - 1, val)  

    def get_edge(self, vi, vj):
        """
        查询 vi -> vj的边权，vi, vj 为 1-based 编号
        返回权值或 None
        """
        vi -= 1
        vj -= 1
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError(f"{vi + 1} 或 {vj + 1} 不是有效顶点编号")
        idx = self.head[vi]
        while idx != -1:
            edge = self.edges[idx]
            if edge.vj == vj:
                return edge.val
            idx = edge.next
        return None

    def printGraph(self):
        """打印所有边，顶点编号输出为 1-based"""
        for vi in range(self.n):
            idx = self.head[vi]
            while idx != -1:
                edge = self.edges[idx]
                print(f"{vi+1} - {edge.vj+1} : {edge.val}")
                idx = edge.next

# 示例：构建有向带权图并查询 / 打印
graph = Graph_3(7)  # 顶点编号 1 ~ 7
edges = [
    [1, 2, 5], [1, 5, 6], [2, 4, 7],
    [4, 3, 9], [3, 1, 2], [5, 6, 8], [6, 4, 3]
]
graph.build(edges)
print(graph.get_edge(4, 3))   # 输出 9
print(graph.get_edge(4, 5))   # 输出 None（无此边）
graph.printGraph()





#哈希表实现邻接表
class Graph_4:
    """哈希表实现的邻接表图结构"""
    def __init__(self, ver_count, directed=False):
        self.n = ver_count                    # 顶点数量
        self.directed = directed              # 是否为有向图
        # 使用字典存储邻接表，键为顶点编号，值为邻接边字典
        # 邻接边字典：键为相邻顶点编号，值为边权重
        self.adj = {i: {} for i in range(1, ver_count + 1)}

    def _valid(self, v):
        """判断顶点编号是否合法（1 ~ n）"""
        return 1 <= v <= self.n

    def add_edge(self, vi, vj, val=1):
        """
        添加一条边 vi -> vj，权值为 val
        vi, vj 为 1-based 顶点编号
        """
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError(f"顶点编号 {vi} 或 {vj} 超出范围 [1, {self.n}]")
        
        # 添加边 vi -> vj
        self.adj[vi][vj] = val
        
        # 如果是无向图，添加反向边
        if not self.directed:
            self.adj[vj][vi] = val

    def build(self, edge_list):
        """
        批量建图
        edge_list: [(vi, vj, val), ...] 边列表，顶点编号从1开始
        """
        for vi, vj, val in edge_list:
            self.add_edge(vi, vj, val)

    def get_edge(self, vi, vj):
        """
        查询 vi -> vj 的边权
        返回权值，如果不存在该边则返回 None
        """
        if not self._valid(vi) or not self._valid(vj):
            raise ValueError(f"顶点编号 {vi} 或 {vj} 超出范围 [1, {self.n}]")
        
        return self.adj[vi].get(vj, None)

    def has_edge(self, vi, vj):
        """
        判断是否存在 vi -> vj 的边
        返回 True 或 False
        """
        if not self._valid(vi) or not self._valid(vj):
            return False
        return vj in self.adj[vi]

    def neighbors(self, vi):
        """
        遍历顶点 vi 的所有邻接边
        返回生成器，每次产生 (邻接顶点, 边权)
        """
        if not self._valid(vi):
            raise ValueError(f"顶点编号 {vi} 超出范围 [1, {self.n}]")
        
        for vj, val in self.adj[vi].items():
            yield vj, val

    def get_degree(self, vi):
        """
        获取顶点 vi 的出度
        """
        if not self._valid(vi):
            raise ValueError(f"顶点编号 {vi} 超出范围 [1, {self.n}]")
        return len(self.adj[vi])

    def print_graph(self):
        """打印所有边"""
        for vi in range(1, self.n + 1):
            for vj, val in self.adj[vi].items():
                print(f"{vi} -> {vj} : {val}")


# 示例：构建有向带权图并测试各种操作

# 创建有向图
graph = Graph_4(6, directed=True)

# 添加边
edges = [(1, 2, 5), (1, 5, 6), (2, 4, 7), (4, 3, 9), (3, 1, 2), (5, 6, 8), (6, 4, 3)]
graph.build(edges)

print("=== 图的基本信息 ===")
print(f"顶点数: {graph.n}")
print(f"是否为有向图: {graph.directed}")

print("\n=== 边的查询操作 ===")
print(f"边 4->3 的权重: {graph.get_edge(4, 3)}")  # 输出: 9
print(f"边 4->5 的权重: {graph.get_edge(4, 5)}")  # 输出: None
print(f"是否存在边 1->2: {graph.has_edge(1, 2)}")  # 输出: True
print(f"是否存在边 2->1: {graph.has_edge(2, 1)}")  # 输出: False

print("\n=== 邻接点遍历 ===")
for vi in range(1, 7):
    neighbors = list(graph.neighbors(vi))
    print(f"顶点 {vi} 的邻接点: {neighbors}, 出度: {graph.get_degree(vi)}")

print("\n=== 所有边 ===")
graph.print_graph()