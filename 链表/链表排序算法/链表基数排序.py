#源地址：https://algo.itcharge.cn/02_linked_list/02_10_linked_list_radix_sort/

"""
适用场景：
链表基数排序的适用场景主要是在位数较小且整数键的情况下
77

总结
链表基数排序按位进行「分桶 + 收集」，在位数较小、整数键的场景下效率稳定。

优点：时间复杂度与数据有序度无关，稳定排序，适合固定位数整数
缺点：空间开销较高，仅适用于整数或可映射到位的键
"""


#代码实现
class Solution:
    def radixSort(self, head: ListNode):       
        # 1. 计算最大数字的位数
        size = 0
        cur = head
        while cur:
            val_len = len(str(cur.val))
            size = max(size, val_len)
            cur = cur.next
        
        # 2. 从个位到最高位依次排序
        for i in range(size):
            # 创建 10 个桶（对应数字 0-9）
            buckets = [[] for _ in range(10)]
            cur = head
            
            # 3. 按当前位数字分配到对应桶
            while cur:
                # 获取第 i 位数字：先除以 10^i，再对 10 取余
                digit = (cur.val // (10 ** i)) % 10
                buckets[digit].append(cur.val)
                cur = cur.next
            
            # 4. 按桶的顺序重新构建链表
            dummy_head = ListNode(-1)
            cur = dummy_head
            for bucket in buckets:
                for num in bucket:
                    cur.next = ListNode(num)
                    cur = cur.next
            head = dummy_head.next
            
        return head
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.radixSort(head)
    

    