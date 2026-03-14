#源地址：https://algo.itcharge.cn/02_linked_list/02_08_linked_list_counting_sort/

"""
适用场景：

值域小且为整数： 
  计数排序特别适用于链表中节点的值在一个较小的范围内，并且这些值是整数。
  例如，如果链表中的节点值范围在 0 到 100 之间，计数排序会非常高效。

数据分布均匀： 
  当链表中的数字分布较为均匀时，计数排序能够更好地发挥其优势。
  如果链表中的数字分布非常稀疏，计数排序的空间开销会变得很大，效率也会降低。

需要稳定排序： 
  计数排序是一种稳定排序算法，这意味着在排序过程中，相同值的节点的相对顺序不会改变。
  如果需要保持原始链表中相同值节点的顺序，计数排序是一个不错的选择。

总结
链表计数排序通过「统计次数 + 重构链表」完成排序，在值域小且为整数的场景下接近线性时间。

优点：时间近线性（当 k 较小）、实现简单、稳定排序
缺点：额外空间O(k)，对值域敏感，不适合大值域或稀疏分布
"""

#代码实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countingSort(self, head: ListNode) -> ListNode:
        # 边界条件检查
        if not head or not head.next:
            return head
        
        # 步骤1: 找出链表中最大值和最小值
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next
        
        # 计算数值范围
        size = list_max - list_min + 1
        
        # 步骤2: 创建计数数组并统计每个数值的出现次数
        counts = [0 for _ in range(size)]
        cur = head
        while cur:
            # 将数值映射到计数数组的索引
            index = cur.val - list_min
            counts[index] += 1
            cur = cur.next
        
        # 步骤3: 重构有序链表
        dummy_head = ListNode(-1)  # 哑节点，简化头节点操作
        cur = dummy_head
        
        # 遍历计数数组，按顺序重构链表
        for i in range(size):
            # 对于每个非零计数，创建相应数量的节点
            while counts[i] > 0:
                # 创建新节点，值为 i + list_min
                new_node = ListNode(i + list_min)
                cur.next = new_node
                cur = cur.next
                counts[i] -= 1
        
        return dummy_head.next

    def sortList(self, head: ListNode) -> ListNode:
        """
        排序链表的主函数
        
        Args:
            head: 待排序链表的头节点
            
        Returns:
            排序后的链表头节点
        """
        return self.countingSort(head)



"""
题目:排序链表
描述：给定链表的头节点 head。

要求：按照升序排列并返回排序后的链表。

说明：
链表中节点的数目在范围[0,5∗10^4] 内。
−10^5≤Node.val≤10^5
"""

