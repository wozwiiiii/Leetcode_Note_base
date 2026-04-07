#https://algo.itcharge.cn/06_graph/06_09_graph_multi_source_shortest_path/


#Floyd-Warshall算法
def floyd_warshall(graph, n):
    """
    Floyd-Warshall 算法，计算所有点对之间的最短路径。
    :param graph: 邻接表，graph[i] = {j: weight, ...}，节点编号为 0~n-1
    :param n: 节点总数
    :return: dist 矩阵，dist[i][j] 表示 i 到 j 的最短路径长度
    """
    # 初始化距离矩阵，所有点对距离设为无穷大
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 距离矩阵对角线设为 0，表示自己到自己的距离为 0
    for i in range(n):
        dist[i][i] = 0
        # 设置直接相连的顶点之间的距离
        for j, weight in graph.get(i, {}).items():
            dist[i][j] = weight

    # 三重循环，枚举每个中间点 k
    for k in range(n):
        for i in range(n):
            # 跳过不可达的起点
            if dist[i][k] == float('inf'):
                continue
            for j in range(n):
                # 跳过不可达的终点
                if dist[k][j] == float('inf'):
                    continue
                # 如果经过 k 能让 i 到 j 更短，则更新
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist




#Johnson算法
from collections import defaultdict
import heapq

def johnson(graph, n):
    """
    Johnson 算法：多源最短路径，支持负权边但不支持负权环。
    :param graph: 邻接表，graph[u] = {v: w, ...}，节点编号 0~n-1
    :param n: 节点总数
    :return: dist 矩阵，dist[i][j] 表示 i 到 j 的最短路径长度；如果有负权环返回 None
    """
    # 1. 构建新图，添加超级源点 s（编号为 n），从 s 向所有顶点连权重为 0 的边
    new_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            new_graph[u][v] = w
    for u in range(n):
        new_graph[n][u] = 0  # s -> u，权重为 0

    # 2. Bellman-Ford 算法，计算超级源点 s 到每个顶点的最短距离 h(v)
    h = [float('inf')] * (n + 1)
    h[n] = 0  # s 到自身距离为 0
    # 最多 n 轮松弛
    for _ in range(n):
        updated = False
        for u in new_graph:
            for v, w in new_graph[u].items():
                if h[u] != float('inf') and h[v] > h[u] + w:
                    h[v] = h[u] + w
                    updated = True
        if not updated:
            break

    # 检查负权环：如果还能松弛，说明有负环
    for u in new_graph:
        for v, w in new_graph[u].items():
            if h[u] != float('inf') and h[v] > h[u] + w:
                return None  # 存在负权环

    # 3. 重新赋权：w'(u,v) = w(u,v) + h[u] - h[v]，保证所有边权非负
    reweighted_graph = defaultdict(dict)
    for u in graph:
        for v, w in graph[u].items():
            reweighted_graph[u][v] = w + h[u] - h[v]

    # 4. 对每个顶点运行 Dijkstra 算法，计算最短路径
    dist = [[float('inf')] * n for _ in range(n)]
    for source in range(n):
        d = [float('inf')] * n
        d[source] = 0
        heap = [(0, source)]
        visited = [False] * n
        while heap:
            cur_dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in reweighted_graph[u].items():
                if d[v] > cur_dist + w:
                    d[v] = cur_dist + w
                    heapq.heappush(heap, (d[v], v))
        # 5. 还原原图权重
        for v in range(n):
            if d[v] != float('inf'):
                dist[source][v] = d[v] - h[source] + h[v]
    return dist