#源地址：https://algo.itcharge.cn/02_linked_list/02_11_linked_list_two_pointers/

"""
快慢指针适用场景：

起点不一致的快慢指针
  找到链表中倒数第 k 个节点
  删除链表倒数第 N 个节点
  其他需要定位倒数位置的问题

步长不一致的快慢指针：
  寻找链表的中点
  检测链表是否有环
  找到两个链表的交点
  其他需要定位中间位置的问题


分离双指针适用场景：
  合并两个有序链表
  比较两个链表
  找到两个链表的交点
  其他需要同时处理两个链表的问题
"""


#快慢指针代码模板

#起点不一致
def findNthFromEnd(head, n):
    slow = fast = head
    
    # 快指针先走 n 步
    for _ in range(n):
        fast = fast.next
    
    # 两个指针同时移动
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # 慢指针指向倒数第 n 个节点

#步长不一致
def fastSlowPointer(head):
    slow = fast = head
    
    # 快指针每次走 2 步，慢指针每次走 1 步
    while fast and fast.next:
        slow = slow.next      # 慢指针移动 1 步
        fast = fast.next.next # 快指针移动 2 步
    
    return slow  # 慢指针指向中点或环的入口



#分离指针代码模板
def separateTwoPointers(list1, list2):
    p1, p2 = list1, list2
    
    while p1 and p2:
        if condition1:
            # 两个指针同时移动
            p1 = p1.next
            p2 = p2.next
        elif condition2:
            # 只移动第一个指针
            p1 = p1.next
        else:
            # 只移动第二个指针
            p2 = p2.next
    
    return result