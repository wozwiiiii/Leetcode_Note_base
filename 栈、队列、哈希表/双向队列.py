#原教程地址：https://algo.itcharge.cn/03_stack_queue_hash_table/03_05_bidirectional_queue/

"""
双向队列分为两种实现方式：
  顺序存储（可使用数组实现，需处理循环队列问题避免“假溢出”）
    数组结构：使用固定大小的数组存储元素
    头尾指针：维护队头和队尾的位置
    循环处理：通过取模运算实现循环队列

  链式存储（更加高效和灵活）
    节点结构：每个节点包含数据域和两个指针域（prev 和 next）
    头尾指针：维护指向队头节点和队尾节点的指针
    哨兵节点：可以使用哨兵节点简化边界处理
  
总结：  
优点
  操作灵活：支持在队列两端进行插入和删除操作
  效率高：所有基本操作的时间复杂度均为 O(1)
  功能强大：可以模拟栈和队列的行为
  应用广泛：在滑动窗口、单调队列等算法中发挥重要作用

缺点
  实现复杂：相比普通队列，实现逻辑更加复杂
  内存开销：链式实现需要额外的指针空间
  缓存性能：链式实现在缓存性能上不如数组实现

适用场景
  滑动窗口问题：如滑动窗口最大值、最小值等
  单调队列：维护单调递增或递减序列
  双端操作：需要在序列两端频繁操作的场景
  算法优化：某些算法的时间复杂度优化
"""

#代码复现

#链式存储双向队列
class Node:
    """双向链表节点"""
    def __init__(self, value):
        self.value = value     # 节点值
        self.prev = None       # 指向前一个节点的指针
        self.next = None       # 指向后一个节点的指针

class Dequ1:
    """双向队列实现"""
    def __init__(self):
        """初始化空双向队列"""
        # 创建哨兵节点
        self.head = Node(0)    # 头哨兵节点
        self.tail = Node(0)    # 尾哨兵节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0          # 队列大小
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def push_front(self, value):
        """队头入队"""
        new_node = Node(value)
        # 在头哨兵节点后插入新节点
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    
    def push_back(self, value):
        """队尾入队"""
        new_node = Node(value)
        # 在尾哨兵节点前插入新节点
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
    
    def pop_front(self):
        """队头出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 删除头哨兵节点后的第一个节点
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        self.size -= 1
        return node.value
    
    def pop_back(self):
        """队尾出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 删除尾哨兵节点前的第一个节点
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        self.size -= 1
        return node.value
    
    def peek_front(self):
        """查看队头元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.head.next.value
    
    def peek_back(self):
        """查看队尾元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.tail.prev.value


#顺序存储双向队列
class Deque2:
    """顺序存储双向队列实现"""
    def __init__(self, capacity=100):
        """初始化双向队列"""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0        # 队头指针
        self.rear = 0         # 队尾指针
        self.size = 0         # 队列大小
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    
    def is_full(self):
        """判断队列是否已满"""
        return self.size == self.capacity
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def push_front(self, value):
        """队头入队"""
        if self.is_full():
            raise Exception('Deque is full')
        
        # 队头指针向前移动
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
    
    def push_back(self, value):
        """队尾入队"""
        if self.is_full():
            raise Exception('Deque is full')
        
        self.queue[self.rear] = value
        # 队尾指针向后移动
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def pop_front(self):
        """队头出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        value = self.queue[self.front]
        # 队头指针向后移动
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
    
    def pop_back(self):
        """队尾出队"""
        if self.is_empty():
            raise Exception('Deque is empty')
        
        # 队尾指针向前移动
        self.rear = (self.rear - 1) % self.capacity
        value = self.queue[self.rear]
        self.size -= 1
        return value
    
    def peek_front(self):
        """查看队头元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.queue[self.front]
    
    def peek_back(self):
        """查看队尾元素"""
        if self.is_empty():
            raise Exception('Deque is empty')
        return self.queue[(self.rear - 1) % self.capacity]