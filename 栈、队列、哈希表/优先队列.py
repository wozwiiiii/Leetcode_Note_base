#原教程地址：https://algo.itcharge.cn/03_stack_queue_hash_table/03_04_priority_queue/


"""
Python 可通过 heapq 模块实现优先队列

有三种实现方式：
  数组（顺序存储）
    入队时直接将元素插入数组末尾，时间复杂度为O(1)；出队时需遍历整个数组以找到优先级最高的元素并删除，时间复杂度为O(n)
  
  链表（链式存储）
    链表内元素按优先级有序排列，入队时需找到合适插入位置，时间复杂度为O(n)；出队时直接移除链表头节点，时间复杂度为O(1)

  二叉堆结构（常用且高效）
    通过二叉堆维护优先级顺序，入队操作（插入新元素）和出队操作（弹出优先级最高元素）均为O(logn)，效率较高



适用场景：
  数据压缩：如赫夫曼编码算法中，频率最低的节点优先合并。
  
  最短路径搜索：如 Dijkstra 算法，优先扩展当前距离最小的节点。
  
  最小生成树构建：如 Prim 算法，优先选择权值最小的边。
  
  任务调度：根据任务优先级动态分配执行顺序。
  
  事件驱动仿真：如排队系统，优先处理最早到达或优先级最高的事件。
  
  Top-K 问题：如查找第 k 大（小）元素、实时维护前 K 个高频元素等
"""


#代码复现


#二叉堆实现优先队列
"""
常用方法：
  heapAdjust：调整堆结构
  heapify：建堆
  heappush：入队
  heappop：出队
  heapSort：堆排序
"""

#原教程中的手写方法
class Heapq:
    # 堆调整方法：将以 index 为根的子树调整为大顶堆
    def heapAdjust(self, nums: list, index: int, end: int):
        """
        nums: 堆数组
        index: 当前需要调整的根节点下标
        end: 堆的最后一个元素下标
        """
        left = index * 2 + 1  # 左子节点下标
        right = left + 1      # 右子节点下标
        while left <= end:
            max_index = index  # 假设当前根节点最大
            # 比较左子节点
            if nums[left] > nums[max_index]:
                max_index = left
            # 比较右子节点（注意要先判断是否越界）
            if right <= end and nums[right] > nums[max_index]:
                max_index = right
            if index == max_index:
                # 如果根节点就是最大值，调整结束
                break
            # 交换根节点与最大子节点
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整被交换下去的子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 建堆：将数组整体调整为大顶堆
    def heapify(self, nums: list):
        size = len(nums)
        # 从最后一个非叶子节点开始，依次向前调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapAdjust(nums, i, size - 1)

    # 入队操作：插入新元素到堆中
    def heappush(self, nums: list, value):
        """
        nums: 堆数组
        value: 待插入的新元素
        """
        nums.append(value)  # 先将新元素加到末尾
        i = len(nums) - 1   # 新元素下标
        # 自下向上调整，恢复堆结构
        while i > 0:
            parent = (i - 1) // 2  # 父节点下标
            if nums[parent] >= value:
                # 父节点比新元素大，插入到当前位置
                break
            # 父节点下移
            nums[i] = nums[parent]
            i = parent
        nums[i] = value  # 插入到最终位置

    # 出队操作：弹出堆顶元素（最大值）
    def heappop(self, nums: list) -> int:
        """
        nums: 堆数组
        return: 堆顶元素
        """
        size = len(nums)
        if size == 0:
            raise IndexError("heappop from empty heap")
        # 交换堆顶和末尾元素
        nums[0], nums[-1] = nums[-1], nums[0]
        top = nums.pop()  # 弹出最大值
        if size > 1:
            # 重新调整堆
            self.heapAdjust(nums, 0, size - 2)
        return top

    # 堆排序：原地将数组升序排序
    def heapSort(self, nums: list):
        """
        nums: 待排序数组
        return: 升序排序后的数组
        """
        self.heapify(nums)  # 先建堆
        size = len(nums)
        # 依次将堆顶元素（最大值）交换到末尾，缩小堆范围
        for i in range(size - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # 堆顶与末尾交换
            self.heapAdjust(nums, 0, i - 1)      # 调整剩余部分为大顶堆
        return nums
    

#使用python中的heapq模块实现
"""
核心操作如下：

heapq.heappush(heap, item)：将元素 item 压入堆 heap 中，保持堆结构。
heapq.heappop(heap)：弹出并返回堆中的最小元素。


注意事项：
heapq 默认是小顶堆，即每次弹出的是最小值。
如果需实现「大顶堆」（每次弹出最大优先级元素），可将优先级取负数存入堆中。
为保证当优先级相同时元素的入队顺序，通常可额外存储一个自增索引

"""
import heapq

class PriorityQueue:
    def __init__(self):
        # 初始化一个空堆和自增索引
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        """
        入队操作，将元素 item 按照优先级 priority 压入堆中。
        为实现大顶堆，优先级取负数；index 保证相同优先级时的稳定性。
        """
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        """
        出队操作，弹出并返回优先级最高的元素（大顶堆）。
        """
        if not self.queue:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.queue)[-1]    