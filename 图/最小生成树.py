#https://algo.itcharge.cn/06_graph/06_06_graph_minimum_spanning_tree/


#代码复现

#Prim算法
class Solution_1:
    # Prim 算法实现，graph 为邻接表（dict of dict），start 为起始顶点编号
    def Prim(self, graph, start):
        size = len(graph)
        vis = set()  # 已经加入最小生成树的顶点集合
        dist = [float('inf')] * size  # dist[i] 表示当前未加入集合的点 i 到已选集合的最小边权

        ans = 0  # 最小生成树的总权值
        dist[start] = 0  # 起点到自身距离为 0

        # 初始化 dist 数组：起点到其他点的距离
        for i in range(size):
            if i != start:
                dist[i] = graph[start][i]
        vis.add(start)  # 起点加入已访问集合

        for _ in range(size - 1):  # 还需加入 size-1 个顶点
            min_dis = float('inf')
            min_dis_pos = -1
            # 在未访问的顶点中，选择距离已选集合最近的顶点
            for i in range(size):
                if i not in vis and dist[i] < min_dis:
                    min_dis = dist[i]
                    min_dis_pos = i
            if min_dis_pos == -1:  # 图不连通，无法生成最小生成树
                return -1
            ans += min_dis  # 累加边权
            vis.add(min_dis_pos)  # 新顶点加入集合
            # 用新加入的顶点更新其他未访问顶点的最小边权
            for i in range(size):
                if i not in vis and dist[i] > graph[min_dis_pos][i]:
                    dist[i] = graph[min_dis_pos][i]
        return ans

# 示例：使用 Prim 算法计算最小生成树的权值和

# 构造一个点集，生成邻接矩阵（曼哈顿距离），并求最小生成树
points = [[0, 0]]
graph = dict()
size = len(points)
for i in range(size):
    x1, y1 = points[i]
    for j in range(size):
        x2, y2 = points[j]
        dist_ij = abs(x2 - x1) + abs(y2 - y1)  # 曼哈顿距离
        if i not in graph:
            graph[i] = dict()
        if j not in graph:
            graph[j] = dict()
        graph[i][j] = dist_ij
        graph[j][i] = dist_ij  # 无向图，双向赋值

# 调用 Prim 算法，输出最小生成树的权值和
print(Solution_1().Prim(graph, 0))



#Kruskal算法
class UnionFind_2:
    def __init__(self, n):
        # 初始化每个节点的父节点为自己
        self.parent = [i for i in range(n)]
        # 连通分量数量
        self.count = n

    def find(self, x):
        # 查找根节点
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        # 合并两个集合
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # 已经在同一个集合，无需合并
        self.parent[root_x] = root_y
        self.count -= 1
        return True  # 合并成功

    def is_connected(self, x, y):
        # 判断两个节点是否属于同一个集合
        return self.find(x) == self.find(y)


class Solution_2:
    def Kruskal(self, edges, size):
        """
        edges: 边集合，每条边为 [u, v, w]，表示 u-v 权重为 w
        size: 顶点数量
        返回最小生成树的权值和
        """
        union_find = UnionFind_2(size)
        # 按权重升序排序所有边
        edges.sort(key=lambda x: x[2])

        ans = 0  # 最小生成树的总权值
        edge_count = 0  # 已加入生成树的边数

        for u, v, w in edges:
            # 如果 u 和 v 不连通，则选这条边
            if union_find.union(u, v):
                ans += w
                edge_count += 1
                # 最小生成树边数为 n - 1 时结束
                if edge_count == size - 1:
                    break
        return ans

# 示例：使用 Kruskal 算法计算最小生成树的权值和

# 假设有 4 个顶点，边集如下（每条边为 [u, v, w]，u 和 v 为顶点编号，w 为权重）：
edges = [
    [0, 1, 1],
    [0, 2, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 2]
]
size = 4  # 顶点数量

# 调用 Kruskal ，输出最小生成树的权值和
mst_weight = Solution_2().Kruskal(edges, size)
print("最小生成树的权值和为：", mst_weight)
# 输出：最小生成树的权值和为：4