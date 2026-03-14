#原教程地址：https://algo.itcharge.cn/02_linked_list/02_03_linked_list_bubble_sort/

"""
适用场景：
小规模数据：节点数量 < 100
教学演示：理解排序算法原理
特殊要求：需要稳定排序且空间受限

总结
链表中的冒泡排序是最简单的链表排序之一，通过相邻节点比较交换实现排序。虽然实现简单，但效率较低。

优点：实现简单，稳定排序，空间复杂度低
缺点：时间复杂度高，交换次数多
"""

#代码复现
class Solution:
    def bubbleSort(self, head: ListNode):
        if not head or not head.next:
            return head
            
        # 外层循环：控制排序轮数
        node_i = head
        tail = None  # 尾指针，右侧为已排序部分
        
        while node_i:
            node_j = head  # 内层循环指针
            
            # 内层循环：比较相邻节点
            while node_j and node_j.next != tail:
                if node_j.val > node_j.next.val:
                    # 交换相邻节点的值
                    node_j.val, node_j.next.val = node_j.next.val, node_j.val
                node_j = node_j.next
            
            # 更新尾指针，右侧已排好序
            tail = node_j
            node_i = node_i.next
            
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSort(head)