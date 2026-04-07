#https://algo.itcharge.cn/06_graph/06_08_graph_shortest_path_02/


#代码复现

#Bellman-Ford算法
class Solution_1:
    def bellmanFord(self, graph, n, source):
        """
        Bellman-Ford 算法求解单源最短路径，可处理负权边，并检测负权环。
        :param graph: 邻接表，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist 数组，dist[i] 表示源点到 i 的最短距离；如果存在负权环返回 None
        """
        # 初始化距离数组，所有点距离为正无穷，源点距离为 0
        dist = [float('inf')] * (n + 1)
        dist[source] = 0

        # 进行 n - 1 轮松弛操作
        for i in range(n - 1):
            updated = False  # 优化：记录本轮是否有更新
            # 遍历所有边，尝试松弛
            for u in graph:
                for v, w in graph[u].items():
                    # 如果 u 可达，且通过 u 到 v 更短，则更新
                    if dist[u] != float('inf') and dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        updated = True
            # 如果本轮没有任何更新，说明已提前收敛，可终止
            if not updated:
                break

        # 再遍历一遍所有边，检查是否还能松弛，如果能则存在负权环
        for u in graph:
            for v, w in graph[u].items():
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    return None  # 存在负权环

        return dist
    


#SPFA算法
from collections import deque

def spfa(graph, n, source):
    """
    SPFA（Shortest Path Faster Algorithm）算法，求解单源最短路径，可处理负权边，并检测负权环。
    :param graph: 邻接表，graph[u] = {v: w, ...}
    :param n: 节点总数（节点编号从 1 到 n）
    :param source: 源点编号
    :return: dist 数组，dist[i] 表示源点到 i 的最短距离；如果存在负权环返回 None
    """
    # 距离数组，初始化为无穷大，dist[i] 表示源点到 i 的最短距离
    dist = [float('inf')] * (n + 1)
    dist[source] = 0  # 源点到自身距离为 0

    # 队列，存储待处理的节点
    queue = deque()
    queue.append(source)

    # 标记数组，in_queue[i] 表示节点 i 是否在队列中，避免重复入队
    in_queue = [False] * (n + 1)
    in_queue[source] = True

    # 记录每个节点的入队次数，用于检测负权环
    count = [0] * (n + 1)
    count[source] = 1  # 源点已入队一次

    while queue:
        u = queue.popleft()
        in_queue[u] = False  # 当前节点出队

        # 遍历 u 的所有邻居 v
        for v, w in graph.get(u, {}).items():
            # 如果通过 u 到 v 的距离更短，则更新
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                # 只有距离被更新，才需要考虑入队
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    # 如果某个节点入队次数超过 n-1，说明存在负权环
                    if count[v] >= n:
                        return None  # 存在负权环，返回 None

    return dist   