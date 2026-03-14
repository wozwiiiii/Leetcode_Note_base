#原教程网址：https://algo.itcharge.cn/02_linked_list/02_05_linked_list_insertion_sort/



"""
适用场景：
链表长度较小（通常 < 1000）
链表基本有序的情况
需要稳定排序的场景
作为教学或理解插入排序原理的练习



总结：
链表插入排序通过将未排序节点插入到已排序部分的正确位置完成排序。对近乎有序的链表表现较好，但总体效率不高。

优点：实现简单，稳定排序，空间复杂度低，适合近乎有序数据
缺点：平均/最坏时间复杂度高，不适合大规模数据
"""
#代码实现
class Solution:
    def insertionSort(self, head: ListNode):
        if not head or not head.next:
            return head
        
        # 创建哑节点，简化边界情况处理
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # sorted_tail: 已排序部分的尾节点
        # cur: 当前待插入的节点
        sorted_tail = head
        cur = head.next 
        
        while cur:
            if sorted_tail.val <= cur.val:
                # cur 已经在正确位置，扩展已排序部分
                sorted_tail = sorted_tail.next 
            else:
                # 需要插入 cur 到已排序部分的合适位置
                prev = dummy_head
                # 找到插入位置：第一个大于 cur.val 的节点的前一个位置
                while prev.next.val <= cur.val:
                    prev = prev.next
                
                # 执行插入操作
                sorted_tail.next = cur.next  # 从原位置移除 cur
                cur.next = prev.next         # cur 指向下一个节点
                prev.next = cur              # 前一个节点指向 cur
            
            # 移动到下一个待插入节点
            cur = sorted_tail.next 
        
        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)
    



#练习题
"""
给定链表的头节点 head。

要求：对链表进行插入排序。

说明：
插入排序算法：
 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。

 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

 列表中的节点数在[1,5000] 范围内。

 −5000≤Node.val≤5000。
"""
