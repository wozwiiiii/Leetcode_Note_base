#源地址：https://algo.itcharge.cn/02_linked_list/02_09_linked_list_bucket_sort/

""" 
适用场景：
已知值域且分布均匀： 
  场景描述：当链表中的元素值在一个已知的范围内，并且这些值的分布相对均匀时，桶排序非常有效。
  优点：在这种情况下，桶排序可以接近线性时间复杂度 O(n + k)，其中 n 是链表的长度，k 是桶的数量

大规模数据排序 
  场景描述：需要对大规模数据进行排序，并且值域范围已知且分布均匀。
  优点：桶排序在处理大规模数据时，如果值域分布均匀，可以显著提高排序效率，避免快速排序和归并排序在最坏情况下的性能退化。

稳定排序需求： 
  场景描述：需要对链表进行排序，并且要求排序是稳定的（即相同元素的相对顺序保持不变）。
  优点：桶排序可以使用稳定排序算法（如归并排序）对每个桶内的元素进行排序，从而保证整体排序的稳定性。

内存受限： 
  场景描述：在内存有限的情况下进行链表排序。
  优点：桶排序不需要额外的空间来存储元素本身，只需存储桶的指针，因此在内存受限的环境中仍然适用。

并行处理： 
  场景描述：需要对链表进行并行排序。
  优点：由于桶排序可以独立对每个桶进行排序，因此适合并行处理，可以提高排序的效率。

总结：
表桶排序将元素按值域分配到多个桶中，分别排序后再合并。适合值域已知且分布较均匀的场景。

优点：分布均匀且桶参数合理时可接近线性；可用稳定桶内排序；并行友好
缺点：对分布与桶大小/数量敏感；额外空间 O(n+k)；最坏情况可能退化
"""

#代码复现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertion(self, buckets, index, val):
        """
        将元素插入到指定桶中（头插法）
        
        Args:
            buckets: 桶数组
            index: 桶的索引
            val: 要插入的值
        """
        if not buckets[index]:
            # 如果桶为空，直接创建新节点
            buckets[index] = ListNode(val)
            return
        
        # 头插法：新节点插入到桶的头部
        node = ListNode(val)
        node.next = buckets[index]
        buckets[index] = node
        
    def merge(self, left, right):
        """
        归并两个有序链表
        
        Args:
            left: 左链表头节点
            right: 右链表头节点
            
        Returns:
            合并后的有序链表头节点
        """
        dummy_head = ListNode(-1)  # 虚拟头节点
        cur = dummy_head
        
        # 比较两个链表的节点值，选择较小的加入结果链表
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            
        # 处理剩余节点
        if left:
            cur.next = left
        elif right:
            cur.next = right
            
        return dummy_head.next
    
    def mergeSort(self, head):
        """
        对链表进行归并排序
        
        Args:
            head: 链表头节点
            
        Returns:
            排序后的链表头节点
        """
        # 递归终止条件：空链表或单节点
        if not head or not head.next:
            return head
        
        # 快慢指针找到链表中间位置
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
        # 分割链表为左右两部分
        left_head, right_head = head, slow.next 
        slow.next = None
        
        # 递归排序左右两部分，然后归并
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))        
    
    def bucketSort(self, head, bucket_size=5):
        """
        链表桶排序主函数
        
        Args:
            head: 待排序的链表头节点
            bucket_size: 每个桶的大小，默认5
            
        Returns:
            排序后的链表头节点
        """
        if not head:
            return head
        
        # 第一步：找出链表中的最大值和最小值
        list_min, list_max = float('inf'), float('-inf')
        cur = head
        while cur:
            list_min = min(list_min, cur.val)
            list_max = max(list_max, cur.val)
            cur = cur.next
            
        # 第二步：计算桶的数量并初始化桶数组
        bucket_count = (list_max - list_min) // bucket_size + 1
        buckets = [None for _ in range(bucket_count)]
        
        # 第三步：将链表元素分配到对应的桶中
        cur = head
        while cur:
            # 计算元素应该放入哪个桶
            index = (cur.val - list_min) // bucket_size
            self.insertion(buckets, index, cur.val)
            cur = cur.next
            
        # 第四步：对每个桶内的元素排序，然后合并
        dummy_head = ListNode(-1)
        cur = dummy_head
        
        for bucket_head in buckets:
            if bucket_head:
                # 对桶内元素进行归并排序
                sorted_bucket = self.mergeSort(bucket_head)
                # 将排序后的桶内元素添加到结果链表
                while sorted_bucket:
                    cur.next = sorted_bucket
                    cur = cur.next
                    sorted_bucket = sorted_bucket.next
                
        return dummy_head.next
    
    def sortList(self, head):
        """
        排序链表接口函数
        
        Args:
            head: 待排序的链表头节点
            
        Returns:
            排序后的链表头节点
        """
        return self.bucketSort(head)
    

"""
练习题
描述：给定链表的头节点 head。

要求：按照升序排列并返回排序后的链表。

说明：
链表中节点的数目在范围[0,5∗10^4] 内。
−10^5≤Node.val≤10^5。
"""    