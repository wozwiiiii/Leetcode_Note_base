#讲解源地址：https://algo.itcharge.cn/01_array/01_09_array_heap_sort/

"""
使用场景：
大规模数据排序
内存受限的环境
需要稳定时间复杂度的场景
需要保证最坏情况下性能的场景

总结：
排序是一种基于堆数据结构的排序算法，利用堆的特性实现高效排序。
核心思想：
将数组构建成大顶堆，堆顶元素始终是最大值
重复取出堆顶元素并调整堆结构，最终得到有序数组

算法步骤：
构建初始堆：将数组转换为大顶堆
重复提取：交换堆顶与末尾元素，调整堆结构，逐步得到有序数组

优点：
时间复杂度稳定，始终为O(nlogn)
空间复杂度低，为 O(1)
适合处理大规模数据
原地排序，不需要额外空间
缺点：
不稳定排序
常数因子较大，实际应用中可能比快速排序稍慢
对缓存不友好，访问模式不够局部化
堆排序是一种同时具备O(nlogn)时间复杂度和O(1)空间复杂度的比较排序算法，
在内存受限或需要稳定时间复杂度的场景下具有重要价值
"""


#1、堆的基本结构和基础操作
#通常创建一个类来封装堆的各种操作
class MaxHeap_Base:
    def __init__(self):
        #创建空的大顶堆
        self.max_heap = []

    #访问堆顶元素
    def peek(self) -> int:
        #检查堆是否为空
        if not self.max_heap:
            return None
        #返回堆顶元素（数组第一个元素）
        return self.max_heap[0]

    #向堆中插入元素
    def push(self, val: int):
        #将新元素添加到堆的末尾
        self.max_heap.append(val)
        #从新元素开始进行上移调整
        self.__shift_up(len(self.max_heap) - 1)

    def __shift_up(self, i: int):
        #上移调整：将节点与其父节点比较并交换
        while (i - 1) // 2 >= 0 and self.max_heap[i] > self.max_heap[(i-1) // 2]:
            #交换当前节点与父节点
            self.max_heap[i], self.max_heap[(i - 1) // 2] = self.max_heap[(i - 1) // 2], self.max_heap[i]
            #继续向上调整
            i = (i - 1) // 2

    #删除堆顶元素
    def pop(self) -> int:
    # 检查堆是否为空
        if not self.max_heap:
            raise IndexError("堆为空")
    
        # 交换堆顶元素与末尾元素
        size = len(self.max_heap)
        self.max_heap[0], self.max_heap[size - 1] = self.max_heap[size - 1], self.max_heap[0]
    
        # 删除末尾元素（原堆顶元素）
        val = self.max_heap.pop()
    
        # 如果堆不为空，进行下移调整
        if self.max_heap:
            self.__shift_down(0, len(self.max_heap))
    
        # 返回被删除的堆顶元素
        return val

    def __shift_down(self, i: int, n: int):
        # 下移调整：将节点与其较大的子节点比较并交换
        while 2 * i + 1 < n:
            # 计算左右子节点索引
            left, right = 2 * i + 1, 2 * i + 2
        
            # 找出较大的子节点
            larger = left
            if right < n and self.max_heap[right] > self.max_heap[left]:
                larger = right
        
            # 如果当前节点小于较大子节点，则交换
            if self.max_heap[i] < self.max_heap[larger]:
                self.max_heap[i], self.max_heap[larger] = self.max_heap[larger], self.max_heap[i]
                i = larger
            else:
                break 



#2、堆排序代码实现
class MaxHeap:
    def __init__(self):
        self.max_heap = []
    
    def __buildMaxHeap(self, nums: [int]):
        # 将数组元素复制到堆中
        self.max_heap = nums.copy()
        size = len(nums)
        
        # 从最后一个非叶子节点开始，自底向上构建堆
        for i in range((size - 2) // 2, -1, -1):
            self.__shift_down(i, size)

    def maxHeapSort(self, nums: [int]) -> [int]:
        # 第一阶段：构建初始大顶堆
        self.__buildMaxHeap(nums)
        
        size = len(self.max_heap)
        # 第二阶段：重复提取最大值
        for i in range(size - 1, -1, -1):
            # 交换堆顶元素与当前末尾元素
            self.max_heap[0], self.max_heap[i] = self.max_heap[i], self.max_heap[0]
            # 对新的堆顶元素进行下移调整，堆的大小为 i
            self.__shift_down(0, i)
        
        # 返回排序后的数组
        return self.max_heap
    
    def __shift_down(self, i: int, n: int):
        # 下移调整：将节点与其较大的子节点比较并交换
        while 2 * i + 1 < n:
            left, right = 2 * i + 1, 2 * i + 2
            
            # 找出较大的子节点
            larger = left
            if right < n and self.max_heap[right] > self.max_heap[left]:
                larger = right
            
            # 如果当前节点小于较大子节点，则交换
            if self.max_heap[i] < self.max_heap[larger]:
                self.max_heap[i], self.max_heap[larger] = self.max_heap[larger], self.max_heap[i]
                i = larger
            else:
                break

class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        return MaxHeap().maxHeapSort(nums)


#练习题
"""
描述：给定一个未排序的整数数组nums和一个整数k。
要求：返回数组中第k个最大的元素。
说明：
  1、要求使用时间复杂度为 O(n)的算法解决此问题。
  2、1< k < nums.length <= 10^5
  3、-10^4 < nums[i] <= 10^4
"""
