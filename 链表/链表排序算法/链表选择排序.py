#源地址：https://algo.itcharge.cn/02_linked_list/02_04_linked_list_selection_sort/

"""
适用场景：
  小规模数据：节点数量较少的场景（如 < 100）
  对空间复杂度严格：仅使用常数额外空间的需求
  交换代价高的场景：选择排序交换次数少（最多 (n-1) 次）

总结
链表中的选择排序是一种简单直观的链表排序算法，通过在未排序部分中选择最小节点并将其放到已排序部分的末尾来完成排序。虽然实现简单，但效率较低。

优点：实现简单，空间复杂度低，交换次数少
缺点：时间复杂度高，不稳定，不适合大规模数据
"""

#代码复现
class Solution:
    def selectionSort(self, head: ListNode):
        node_i = head
        
        # 外层循环：遍历每个节点
        while node_i and node_i.next:
            # 假设当前节点为最小值节点
            min_node = node_i
            node_j = node_i.next
            
            # 内层循环：在未排序部分寻找最小值
            while node_j:
                if node_j.val < min_node.val:
                    min_node = node_j
                node_j = node_j.next
            
            # 如果找到更小的值，则交换（个人认为这里应该的注释为两者不相等则交换）
            if node_i != min_node:
                node_i.val, min_node.val = min_node.val, node_i.val
            
            # 移动到下一个节点
            node_i = node_i.next
        
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.selectionSort(head)