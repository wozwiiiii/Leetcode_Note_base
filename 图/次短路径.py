#https://algo.itcharge.cn/06_graph/06_10_graph_the_second_shortest_path/


#代码复现
#拓展版Dijkstra算法
import heapq
from collections import defaultdict

def second_shortest_path(n, edges, s, t):
    """
    求解有向/无向图中从 s 到 t 的次短路径长度（严格大于最短路径的最小路径）。
    参数说明：
        n: 节点数（编号 0 ~ n - 1）
        edges: List[(u, v, w)]，每条边 (u, v, w) 表示 u 到 v 有一条权重为 w 的边
        s: 起点编号
        t: 终点编号
    返回：
        s 到 t 的次短路径长度，如果不存在返回 float('inf')
    注意：
        - 默认边权非负
        - 如果为无向图，请取消 graph[v].append((u, w))的注释
    """
    # 构建邻接表
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        # 如果是无向图，取消下行注释
        # graph[v].append((u, w))

    INF = float('inf')
    dist1 = [INF] * n  # dist1[i]：s 到 i 的最短路径长度
    dist2 = [INF] * n  # dist2[i]：s 到 i 的严格次短路径长度

    dist1[s] = 0
    # 优先队列，元素为(当前路径长度, 节点编号)
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        # 剪枝：如果当前弹出的距离已大于该点的次短路，则无需处理
        if d > dist2[u]:
            continue
        # 遍历 u 的所有邻居
        for v, w in graph[u]:
            nd = d + w  # 新的路径长度
            # 如果找到更短的路径，更新最短和次短
            if nd < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = nd
                heapq.heappush(pq, (dist1[v], v))
            # 如果新路径严格介于最短和次短之间，更新次短
            elif dist1[v] < nd < dist2[v]:
                dist2[v] = nd
                heapq.heappush(pq, (dist2[v], v))
            # 其他情况（如 nd 等于 dist1[v] 或大于等于 dist2[v]）无需处理

    return dist2[t]  # 如果为 INF 表示不存在次短路径