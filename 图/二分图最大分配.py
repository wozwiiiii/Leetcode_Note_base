#https://algo.itcharge.cn/06_graph/06_12_graph_bipartite_matching/


#代码复现
#匈牙利算法
def max_bipartite_matching(graph, left_size, right_size):
    """
    二分图最大匹配（匈牙利算法，DFS 增广路实现）
    :param graph: 邻接表，graph[u] 存储左侧点 u 能连接到的所有右侧点编号（如 [[], [0,2], ...]）
    :param left_size: 左侧点个数
    :param right_size: 右侧点个数
    :return: 最大匹配数
    """
    match_right = [-1] * right_size  # 记录每个右侧点当前匹配到的左侧点编号，-1 表示未匹配
    result = 0  # 匹配数

    for left in range(left_size):
        visited = [False] * right_size  # 每次为一个左侧点增广时，重置右侧点访问标记
        if find_augmenting_path(graph, left, visited, match_right):
            result += 1  # 成功增广，匹配数加一

    return result

def find_augmenting_path(graph, left, visited, match_right):
    """
    尝试为左侧点 left 寻找一条增广路
    :param graph: 邻接表
    :param left: 当前尝试增广的左侧点编号
    :param visited: 右侧点访问标记，防止重复访问
    :param match_right: 右侧点的匹配关系
    :return: 是否找到增广路
    """
    for right in graph[left]:  # 遍历 left 能连接到的所有右侧点
        if not visited[right]:  # 只尝试未访问过的右侧点
            visited[right] = True  # 标记已访问
            # 如果右侧点未匹配，或其当前匹配的左侧点还能找到新的增广路
            if match_right[right] == -1 or find_augmenting_path(graph, match_right[right], visited, match_right):
                match_right[right] = left  # 配对成功，更新匹配关系
                return True
    return False  # 没有找到增广路




#Hopcroft-Karp算法
from collections import deque

def hopcroft_karp(graph, left_size, right_size):
    """
    Hopcroft-Karp 算法求二分图最大匹配
    :param graph: List[List[int]]，graph[i] 存储左侧点 i 能连到的所有右侧点编号
    :param left_size: 左侧点数量
    :param right_size: 右侧点数量
    :return: 最大匹配数
    """
    # match_left[i] = j 表示左侧点 i 匹配到右侧点 j，未匹配为 -1
    match_left = [-1] * left_size
    # match_right[j] = i 表示右侧点 j 匹配到左侧点 i，未匹配为 -1
    match_right = [-1] * right_size
    result = 0  # 匹配数

    while True:
        # 1. BFS 分层，dist[i] 表示左侧点 i 到未匹配状态的最短距离
        dist = [-1] * left_size
        queue = deque()
        for i in range(left_size):
            if match_left[i] == -1:
                dist[i] = 0
                queue.append(i)
        # 标记本轮是否存在增广路
        found_augmenting = False

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if match_right[v] == -1:
                    # 右侧点 v 未匹配，说明存在增广路
                    found_augmenting = True
                elif dist[match_right[v]] == -1:
                    # 沿着匹配边走，分层
                    dist[match_right[v]] = dist[u] + 1
                    queue.append(match_right[v])

        if not found_augmenting:
            # 没有增广路，算法结束
            break

        # 2. DFS 尝试批量增广
        def dfs(u):
            for v in graph[u]:
                # 如果右侧点未匹配，或者可以沿着分层图递归找到增广路
                if match_right[v] == -1 or (dist[match_right[v]] == dist[u] + 1 and dfs(match_right[v])):
                    match_left[u] = v
                    match_right[v] = u
                    return True
            # 没有找到增广路
            return False

        # 3. 对所有未匹配的左侧点尝试增广
        for i in range(left_size):
            if match_left[i] == -1:
                if dfs(i):
                    result += 1

    return result



#网络流算法
from collections import defaultdict, deque

def max_flow_bipartite_matching(graph, left_size, right_size):
    """
    使用网络流（Ford-Fulkerson 算法）求解二分图最大匹配
    :param graph: List[List[int]]，左侧每个点可连的右侧点编号列表
    :param left_size: 左侧点个数
    :param right_size: 右侧点个数
    :return: 最大匹配数
    """
    # 构建网络流图，节点编号：
    # 0 ~ left_size-1：左侧点
    # left_size ~ left_size+right_size-1：右侧点
    # source: left_size+right_size
    # sink: left_size+right_size+1
    flow_graph = defaultdict(dict)
    source = left_size + right_size
    sink = source + 1

    # 源点到左侧点，容量为 1
    for i in range(left_size):
        flow_graph[source][i] = 1
        flow_graph[i][source] = 0  # 反向边，初始为 0

    # 右侧点到汇点，容量为 1
    for i in range(right_size):
        right_node = left_size + i
        flow_graph[right_node][sink] = 1
        flow_graph[sink][right_node] = 0  # 反向边

    # 左侧点到右侧点，容量为 1
    for i in range(left_size):
        for j in graph[i]:
            right_node = left_size + j
            flow_graph[i][right_node] = 1
            flow_graph[right_node][i] = 0  # 反向边

    def bfs():
        """
        BFS 寻找一条增广路，返回每个节点的父节点
        """
        parent = [-1] * (sink + 1)
        queue = deque([source])
        parent[source] = -2  # 源点特殊标记

        while queue:
            u = queue.popleft()
            for v, capacity in flow_graph[u].items():
                # 只走有剩余容量且未访问过的点
                if parent[v] == -1 and capacity > 0:
                    parent[v] = u
                    if v == sink:
                        return parent  # 找到汇点，返回路径
                    queue.append(v)
        return None  # 未找到增广路

    def ford_fulkerson():
        """
        主流程：不断寻找增广路并更新残量网络
        """
        max_flow = 0
        while True:
            parent = bfs()
            if not parent:
                break  # 没有增广路，算法结束

            # 计算本次增广路的最小残量（本题均为 1，写全以便扩展）
            v = sink
            min_capacity = float('inf')
            while v != source:
                u = parent[v]
                min_capacity = min(min_capacity, flow_graph[u][v])
                v = u

            # 沿增广路更新正反向边的容量
            v = sink
            while v != source:
                u = parent[v]
                flow_graph[u][v] -= min_capacity
                flow_graph[v][u] += min_capacity
                v = u

            max_flow += min_capacity  # 累加总流量

        return max_flow

    return ford_fulkerson()