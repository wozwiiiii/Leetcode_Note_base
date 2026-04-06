#原教程地址：https://algo.itcharge.cn/06_graph/06_03_graph_dfs/



"""

"""



#代码复现


#基于递归的深度优先搜索算法
class Solution_1:
    def dfs_recursive(self, graph, u, visited):
        """
        递归实现深度优先搜索（DFS）
        :param graph: 字典表示的邻接表，key为节点，value为邻接节点列表
        :param u: 当前访问的节点
        :param visited: 已访问节点的集合
        """
        print(u)                        # 访问当前节点 u
        visited.add(u)                  # 标记节点 u 已访问

        # 遍历所有邻接节点
        for v in graph[u]:
            if v not in visited:        # 如果邻接节点 v 未被访问
                # 递归访问邻接节点 v
                self.dfs_recursive(graph, v, visited)
        

# 示例图（邻接表形式，节点为字符串，边为无向边）
graph = {
    "1": ["2", "3"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3", "5", "6"],
    "5": ["3", "4"],
    "6": ["4", "7"],
    "7": []
}

# 初始化已访问节点集合
visited = set()
# 从节点 "1" 开始进行深度优先搜索
Solution_1().dfs_recursive(graph, "1", visited)




#基于堆栈实现的深度优先搜素
class Solution_2:
    def dfs_stack(self, graph, u):
        """
        基于显式栈的深度优先搜索（DFS），适用于无向图/有向图的邻接表表示。
        :param graph: dict，邻接表，key为节点，value为邻接节点列表
        :param u: 起始节点
        """
        visited = set()         # 记录已访问节点，防止重复遍历
        stack = []              # 显式栈，模拟递归过程

        stack.append([u, 0])    # 入栈：节点u及其下一个待访问邻接节点的下标 0
        visited.add(u)          # 标记起始节点已访问
        print(u)                # 访问起始节点

        while stack:
            cur, idx = stack.pop()  # 取出当前节点及其下一个邻接节点下标
            neighbors = graph[cur]  # 当前节点的所有邻接节点

            # 如果还有未遍历的邻接节点
            if idx < len(neighbors):
                v = neighbors[idx]      # 取出下一个邻接节点
                stack.append([cur, idx + 1])  # 当前节点下标 + 1，回溯时继续遍历下一个邻接点

                if v not in visited:
                    print(v)           # 访问新节点
                    visited.add(v)     # 标记为已访问
                    stack.append([v, 0])   # 新节点入栈，准备遍历其邻接节点

        # 也可以返回 visited 集合，便于后续处理
        # return visited

# 示例图（邻接表形式，节点为字符串，边为无向边）
graph = {
    "1": ["2", "3"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3", "5", "6"],
    "5": ["3", "4"],
    "6": ["4", "7"],
    "7": []
}

# 从节点 "1" 开始进行深度优先搜索
Solution_2().dfs_stack(graph, "1")