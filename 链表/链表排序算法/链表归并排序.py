#原教程地址：https://algo.itcharge.cn/02_linked_list/02_06_linked_list_merge_sort/


"""
使用场景:
1. 大规模链表排序：
链表归并排序的时间复杂度为 O(nlogn)，这使得它在处理大规模链表时表现良好。与数组的插入排序或选择排序相比，归并排序的时间复杂度更低，更适合处理较长的序列。 

2. 链表结构：
链表归并排序不需要随机访问（即不需要通过索引来访问任意节点），这使得它天然适合链表这种结构。链表只能通过指针顺序访问节点，归并排序的分治和归并过程可以通过指针操作来高效实现。 

3. 稳定排序：
链表归并排序是一种稳定的排序算法。稳定排序是指在排序过程中，如果有多个相同的元素，它们在排序后的相对顺序与排序前相同。这对于某些应用来说非常重要，特别是在需要保持原有顺序的情况下对数据进行排序。 

4. 链表基本有序的情况：
虽然链表归并排序在链表基本有序的情况下仍然能够保持高效，但不如插入排序在近乎有序链表上表现得更好。然而，对于基本有序的链表，归并排序仍然可以提供良好的性能和稳定性。 

5. 作为教学或理解归并排序原理的练习：
链表归并排序是一个经典的排序算法，通过实现链表归并排序，可以帮助学习者更好地理解分治策略和递归的概念。它也提供了一个不同于数组归并排序的视角，有助于加深对链表操作的理解。


总结
链表归并排序采用分治策略，将链表递归拆分后再两两归并得到有序链表，整体效率高且稳定。

优点：时间复杂度O(nlogn)，稳定排序，适合大规模链表；无需随机访问，天然适配链表结构
缺点：递归实现需要O(logn) 栈空间，实现相对复杂，常数因子较高
"""



#代码实现
class Solution:
    def merge(self, left, right):
        # 归并阶段
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        if left:
            cur.next = left
        elif right:
            cur.next = right
            
        return dummy_head.next
        
    def mergeSort(self, head: ListNode):
        # 分割阶段
        if not head or not head.next:
            return head
        
        # 快慢指针找到中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # 断开左右子链表
        left_head, right_head = head, slow.next 
        slow.next = None
        
        # 归并操作
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
    


"""
练习题：合并两个有序链表
题目大意
描述：给定两个升序链表的头节点 list1 和 list2。

要求：将其合并为一个升序链表。

说明：
两个链表的节点数目范围是[0,50]。
−100≤Node.val≤100。
list1 和 list2 均按 非递减顺序 排列
"""