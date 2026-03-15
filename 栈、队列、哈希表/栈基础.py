#原教程地址：https://algo.itcharge.cn/03_stack_queue_hash_table/03_01_stack_basic/

"""
栈分为两类：

顺序栈（通常数组实现，python中直接使用list（列表）实现）
空间利用率：固定大小，可能浪费
扩容操作：需要重新分配空间
内存碎片：较少
实现复杂度：简单


链式栈（链表实现）
空间利用率：按需分配，无浪费
扩容操作：无需扩容
内存碎片：可能产生碎片
实现复杂度：相对复杂
"""


#代码复现

#顺序栈
class Stack:
    # 初始化空栈
    def __init__(self, size=100):
        self.stack = []        # 存储元素的数组
        self.size = size       # 栈的最大容量
        self.top = -1          # 栈顶指针，-1表示空栈
    
    def is_empty(self):
        """判断栈是否为空"""
        return self.top == -1
    
    def is_full(self):
        """判断栈是否已满"""
        return self.top + 1 == self.size
    
    def push(self, value):
        """入栈操作"""
        if self.is_full():
            raise Exception('栈已满')
        self.stack.append(value)
        self.top += 1
    
    def pop(self):
        """出栈操作"""
        if self.is_empty():
            raise Exception('栈为空')
        value = self.stack.pop()
        self.top -= 1
        return value
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise Exception('栈为空')
        return self.stack[self.top]
    

#链式栈
class Node:
    """链表节点"""
    def __init__(self, value):
        self.value = value     # 节点值
        self.next = None       # 指向下一个节点的指针
        
class Stack:
    def __init__(self):
        """初始化空栈"""
        self.top = None        # 栈顶指针，指向链表头节点
    
    def is_empty(self):
        """判断栈是否为空"""
        return self.top is None
    
    def push(self, value):
        """入栈操作 - 在链表头部插入新节点"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        """出栈操作 - 删除链表头节点"""
        if self.is_empty():
            raise Exception('栈为空')
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise Exception('栈为空')
        return self.top.value



"""
描述：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串s。

要求：判断字符串s是否有效（即括号是否匹配）。

说明：
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""
