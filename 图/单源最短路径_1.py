#https://algo.itcharge.cn/06_graph/06_07_graph_shortest_path_01/


#代码复现

#Dijkstra算法
class Solution_1:
    def dijkstra(self, graph, n, source):
        """
        Dijkstra 算法求解单源最短路径
        :param graph: 邻接表表示的有向图，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist 数组，dist[i] 表示源点到 i 的最短距离
        """
        # 距离数组，初始化为无穷大
        dist = [float('inf')] * (n + 1)
        dist[source] = 0  # 源点到自身距离为 0

        visited = set()  # 已确定最短路的节点集合

        while len(visited) < n:
            # 在所有未访问的节点中，选择距离源点最近的节点
            current_node = -1
            min_distance = float('inf')
            for i in range(1, n + 1):
                if i not in visited and dist[i] < min_distance:
                    min_distance = dist[i]
                    current_node = i

            # 如果没有可处理的节点（说明剩下的节点不可达），提前结束
            if current_node == -1:
                break

            visited.add(current_node)  # 标记当前节点为已访问

            # 遍历当前节点的所有邻居，尝试更新最短距离
            for neighbor, weight in graph.get(current_node, {}).items():
                if neighbor not in visited:
                    if dist[current_node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[current_node] + weight

        return dist

# 使用示例
# 构建一个有向图，邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 节点数量
source = 1  # 源点

dist = Solution_1().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")




#堆优化Dijkstra算法
import heapq

class Solution_2:
    def dijkstra(self, graph, n, source):
        """
        堆优化 Dijkstra 算法，计算单源最短路径
        :param graph: 邻接表，graph[u] = {v: w, ...}
        :param n: 节点总数（节点编号从 1 到 n）
        :param source: 源点编号
        :return: dist[i] 表示源点到 i 的最短距离
        """
        # 距离数组，初始化为无穷大
        dist = [float('inf')] * (n + 1)
        dist[source] = 0  # 源点到自身距离为 0

        # 小根堆，存储 (距离, 节点) 元组
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            # 如果弹出的节点距离不是最短的，说明已被更新，跳过
            if current_distance > dist[current_node]:
                continue

            # 遍历当前节点的所有邻居
            for neighbor, weight in graph.get(current_node, {}).items():
                new_distance = current_distance + weight
                # 如果找到更短路径，则更新并入堆
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return dist

# 使用示例
# 构建一个有向图，邻接表表示
graph = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {4: 3},
    4: {}
}
n = 4  # 节点数量
source = 1  # 源点编号

dist = Solution_2().dijkstra(graph, n, source)
print("从节点", source, "到其他节点的最短距离：")
for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(f"到节点 {i} 的距离：不可达")
    else:
        print(f"到节点 {i} 的距离：{dist[i]}")