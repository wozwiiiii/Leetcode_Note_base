#源代码地址：https://algo.itcharge.cn/02_linked_list/02_07_linked_list_quick_sort/

"""
适用场景：

链表数据结构： 
  动态大小：当链表的大小不确定，且需要频繁插入和删除操作时，快速排序可以有效利用链表的动态特性。
  内存限制：链表快速排序不需要额外的空间来存储元素，适合在内存受限的环境中使用。

排序需求： 
  平均效率要求高：快速排序的平均时间复杂度为 O(nlogn)，如果对排序的时间效率有较高要求，且不介意最坏情况下的性能退化，链表快速排序是一个不错的选择。
  就地排序：如果希望避免额外的空间开销，链表快速排序是一个就地排序算法，适合在需要节省内存的情况下使用。

数据特点： 
  随机分布的数据：快速排序在数据随机分布的情况下表现良好，平均时间复杂度为 O(nlogn)。
  不关心稳定性：如果排序结果的稳定性（相同元素的相对顺序不变）不是必须的，链表快速排序可以满足需求。

总结
链表快速排序通过分治与就地分区实现排序，平均效率高，但极端情况下退化明显，且不稳定。

优点：平均时间复杂度O(nlogn)，就地分区、空间开销小
缺点：最坏时间复杂度O(n^2)，不稳定，对枢轴选择敏感
"""


#代码复现
class Solution:
    def partition(self, left: ListNode, right: ListNode):
        """
        分割函数：将链表分割为两部分
        left: 左边界节点（包含）
        right: 右边界节点（不包含）
        返回：基准值节点的最终位置
        """
        # 边界条件：区间没有元素或者只有一个元素，直接返回第一个节点
        if left == right or left.next == right:
            return left
        
        # 选择头节点为基准节点
        pivot = left.val
        
        # 使用快慢指针进行分割
        # node_i: 指向小于基准值的最后一个节点
        # node_j: 遍历指针，寻找小于基准值的节点
        node_i, node_j = left, left.next
        
        while node_j != right:
            # 发现一个小于基准值的元素
            if node_j.val < pivot:
                # 将 node_i 向右移动一位
                node_i = node_i.next
                # 交换 node_i 和 node_j 的值，保证 node_i 之前的节点都小于基准值
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next
        
        # 将基准节点放到正确位置上（node_i 位置）
        node_i.val, left.val = left.val, node_i.val
        return node_i
        
    def quickSort(self, left: ListNode, right: ListNode):
        """
        快速排序主函数
        left: 左边界节点（包含）
        right: 右边界节点（不包含）
        """
        # 递归终止条件：区间长度小于等于 1
        if left == right or left.next == right:
            return left
        
        # 分割链表，获取基准值位置
        pi = self.partition(left, right)
        
        # 递归排序左半部分
        self.quickSort(left, pi)
        # 递归排序右半部分
        self.quickSort(pi.next, right)
        
        return left

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        链表排序入口函数
        """
        # 边界条件检查
        if not head or not head.next:
            return head
        
        # 调用快速排序
        return self.quickSort(head, None)