#原教程地址：https://algo.itcharge.cn/03_stack_queue_hash_table/03_02_monotone_stack/

"""
适用场景：
 单调栈常用于O(n) 时间复杂度内高效解决「最近更大/更小元素」类问题，主要包括以下四种典型场景：
    查找左侧第一个比当前元素更大 / 更小的元素。
    查找右侧第一个比当前元素更大 / 更小的元素。

单调栈分为两类：

单调递增栈：
每次新元素进栈时，如果它比栈顶元素小，直接入栈；如果比栈顶元素大或相等，就把栈顶及以上所有小于等于它的元素依次弹出，直到栈顶比它大或栈空，再将新元素入栈

单调递减栈：
每次新元素进栈时，只有当它比栈顶元素大时才能直接入栈；如果小于或等于栈顶元素，则需要先将栈中所有大于等于当前元素的元素依次弹出，直到栈顶元素小于当前元素或栈为空，再将新元素入栈。
"""


#代码复现

#单调递增栈
def monotoneIncreasingStack(nums):
    stack = []
    left
    for i, num in enumerate(nums):
        while stack and num >= stack[-1]:
            stack.pop()
        if stack:
        
        stack.append(num)


#单调递减栈
def monotoneDecreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num <= stack[-1]:
            stack.pop()
        stack.append(num)