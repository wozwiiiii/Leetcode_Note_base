#原教程地址：https://algo.itcharge.cn/06_graph/06_04_graph_bfs/


"""

"""



#代码复现

#基于队列实现
import collections

class Solution_1:
    def bfs(self, graph, u):
        visited = set()                     # 使用 visited 标记访问过的节点
        queue = collections.deque([])       # 使用 queue 存放临时节点
        
        visited.add(u)                      # 将起始节点 u 标记为已访问
        queue.append(u)                     # 将起始节点 u 加入队列中
        
        while queue:                        # 队列不为空
            u = queue.popleft()             # 取出队头节点 u
            print(u)                        # 访问节点 u
            for v in graph[u]:              # 遍历节点 u 的所有未访问邻接节点 v
                if v not in visited:        # 节点 v 未被访问
                    visited.add(v)          # 将节点 v 标记为已访问
                    queue.append(v)         # 将节点 v 加入队列中
                

graph = {
    "1": ["2", "3"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3", "5", "6"],
    "5": ["3", "4"],
    "6": ["4", "7"],
    "7": []
}

# 基于队列实现的广度优先搜索
Solution_1().bfs(graph, "1")
