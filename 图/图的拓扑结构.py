#原教程地址：https://algo.itcharge.cn/06_graph/06_05_graph_topological_sorting/


"""

"""


#代码复现

#Kahn算法实现
import collections

class Solution_1:
    # 拓扑排序，graph 中包含所有顶点的有向边关系（包括无边顶点）
    def topologicalSortingKahn(self, graph: dict):
        # 初始化所有顶点的入度为 0
        indegrees = {u: 0 for u in graph}
        # 统计每个顶点的入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1

        # 将所有入度为 0 的顶点加入队列 S
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []  # 用于存储拓扑序列

        while S:
            u = S.pop()  # 取出一个入度为 0 的顶点
            order.append(u)  # 加入拓扑序列
            for v in graph[u]:  # 遍历 u 的所有邻接点
                indegrees[v] -= 1  # 删除 u 指向 v 的边，v 入度减 1
                if indegrees[v] == 0:
                    S.append(v)  # 如果 v 入度为 0，加入队列

        # 如果 order 长度小于顶点数，说明有环，无法拓扑排序
        if len(order) != len(indegrees):
            return []
        return order  # 返回拓扑序列

    def findOrder(self, n: int, edges):
        """
        n: 顶点个数，编号为 0 ~ n - 1
        edges: 边列表，每条边为 (u, v)，表示 u 指向 v
        返回一个拓扑序列（如果有环则返回空列表）
        """
        # 构建邻接表
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
        # 调用 Kahn 算法进行拓扑排序
        return self.topologicalSortingKahn(graph)
    




#DFS深度有限搜索
import collections

class Solution_2:
    # 基于 DFS 的拓扑排序，graph 为邻接表，包含所有顶点（即使无出边也要有键）
    def topologicalSortingDFS(self, graph: dict):
        visited = set()      # 记录已访问过的顶点，防止重复遍历
        onStack = set()      # 记录当前递归路径上的顶点，用于检测环
        order = []           # 存储拓扑序列（后序遍历结果）
        hasCycle = False     # 标记图中是否存在环

        def dfs(u):
            nonlocal hasCycle
            if hasCycle:     # 已经检测到环，直接返回
                return
            if u in onStack:
                # 当前节点在递归栈中，说明存在环
                hasCycle = True
                return
            if u in visited:
                # 已访问过，无需重复遍历
                return

            visited.add(u)       # 标记 u 已访问
            onStack.add(u)       # 标记 u 在当前递归路径上

            for v in graph[u]:   # 遍历 u 的所有邻接点
                dfs(v)           # 递归访问 v

            order.append(u)      # 后序位置加入拓扑序列
            onStack.remove(u)    # 回溯时移除 u，恢复递归路径标记

        # 对所有顶点做 DFS，防止图不连通
        for u in graph:
            if u not in visited:
                dfs(u)

        if hasCycle:
            # 有环，无法拓扑排序
            return []
        order.reverse()  # 后序遍历逆序即为拓扑序
        return order

    def findOrder(self, n: int, edges):
        """
        n: 顶点个数，编号为 0 ~ n-1
        edges: 边列表，每条边为 (u, v)，表示 u 指向 v
        返回一个拓扑序列（有环则返回空列表）
        """
        # 构建邻接表，确保每个顶点都在 graph 中
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
        return self.topologicalSortingDFS(graph)



