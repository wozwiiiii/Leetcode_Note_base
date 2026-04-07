#https://algo.itcharge.cn/06_graph/06_11_graph_bipartite_basic/


#代码复现
#二分图判定
def is_bipartite(graph):
    """
    判断无向图是否为二分图（染色法）
    :param graph: List[List[int]]，邻接表表示的无向图
    :return: bool，是否为二分图
    """
    n = len(graph)
    colors = [0] * n  # 0 表示未染色，1 和 -1 表示两种颜色

    def dfs(node, color):
        """
        对节点 node 进行染色，并递归染色其所有邻居
        :param node: 当前节点编号
        :param color: 当前节点应染的颜色（1 或 -1）
        :return: bool，如果染色无冲突返回 True，否则 False
        """
        colors[node] = color  # 给当前节点染色
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                # 邻居和当前节点颜色相同，冲突，非二分图
                return False
            if colors[neighbor] == 0:
                # 邻居未染色，递归染成相反颜色
                if not dfs(neighbor, -color):
                    return False
        return True

    for i in range(n):
        if colors[i] == 0:
            # 只对未染色的节点（新连通分量）进行 DFS 染色
            if not dfs(i, 1):
                return False  # 染色过程中发现冲突，非二分图
    return True  # 所有节点染色无冲突，是二分图