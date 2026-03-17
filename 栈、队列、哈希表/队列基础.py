#原教程：https://algo.itcharge.cn/03_stack_queue_hash_table/03_03_queue_basic/

"""
队列的应用：
1、缓解主机与外部设备之间的速度差异

2、解决多用户环境下的系统资源竞争

队列分为两类：

顺序储存队列：
  顺序存储队列（非循环）：队列满时无法插入新元素


  解决队满时无法插入新元素的问题:

    每次出队后整体前移元素：时间复杂度为O(n)，不推荐

    循环移动：基本操作时间复杂度均为O(1)
      顺序存储循环队列：



链式存储队列：


"""


#代码复现


#顺序存储队列（python中，可直接使用列表（list）实现）
class Queue:
    """
    顺序存储队列实现（非循环队列）
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """
    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量
        """
        self.size = size
        self.queue = [None for _ in range(size)]  # 存储队列元素的数组
        self.front = -1  # 队头指针，指向队头元素的前一个位置
        self.rear = -1   # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: 如果队列已满返回 True，否则返回 False
        """
        return self.rear + 1 == self.size

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 待插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception('Queue is full')
        self.rear += 1
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        self.front += 1
        return self.queue[self.front]

    def front_value(self):
        """
        获取队头元素（不删除）
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.front + 1]

    def rear_value(self):
        """
        获取队尾元素（不删除）
        :return: 队尾元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.rear]


#顺序存储循环队列
class Queue_2:
    """
    顺序存储循环队列实现
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """
    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量（实际可用容量为 size）
        """
        self.size = size + 1  # 实际分配空间多一个，用于区分队满和队空
        self.queue = [None for _ in range(self.size)]  # 存储队列元素
        self.front = 0  # 队头指针，指向队头元素的前一个位置
        self.rear = 0   # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: True 表示队列为空，False 表示非空
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: True 表示队列已满，False 表示未满
        """
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 要插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception('Queue is full')
        # rear 指针循环前进一位
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        # front 指针循环前进一位
        self.front = (self.front + 1) % self.size
        value = self.queue[self.front]
        self.queue[self.front] = None  # 可选：清除引用，便于垃圾回收
        return value

    def front_value(self):
        """
        获取队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[(self.front + 1) % self.size]

    def rear_value(self):
        """
        获取队尾元素
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue[self.rear]
    


#链式存储队列
class Node:
    """
    链表节点类
    """
    def __init__(self, value):
        self.value = value  # 节点存储的值
        self.next = None    # 指向下一个节点的指针

class Queue_3:
    """
    链式队列实现
    """
    def __init__(self):
        """
        初始化空队列，创建一个头结点（哨兵节点），front和rear都指向头结点
        """
        head = Node(0)  # 哨兵节点，不存储有效数据
        self.front = head  # front指向队头元素的前一个节点
        self.rear = head   # rear指向队尾节点

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def enqueue(self, value):
        """
        入队操作，在队尾插入新节点
        :param value: 要插入的元素值
        """
        node = Node(value)         # 创建新节点
        self.rear.next = node      # 当前队尾节点的next指向新节点
        self.rear = node           # rear指针后移，指向新节点

    def dequeue(self):
        """
        出队操作，删除队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        node = self.front.next         # 队头节点（第一个有效节点）
        self.front.next = node.next    # front的next指向下一个节点
        if self.rear == node:          # 如果出队后队列为空，rear回退到front
            self.rear = self.front
        value = node.value             # 取出队头元素的值
        del node                       # 释放节点（可省略，Python自动垃圾回收）
        return value

    def front_value(self):
        """
        获取队头元素的值
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        return self.front.next.value   # front.next为队头节点

    def rear_value(self):
        """
        获取队尾元素的值
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception('Queue is empty')
            
        return self.rear.value         # rear为队尾节点    
    


"""
练习题

要求：仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的四种操作：push、top、pop 和 empty。

要求实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 True；否则，返回 False。

说明：
只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
"""    
