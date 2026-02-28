#源地址：https://algo.itcharge.cn/01_array/01_04_array_selection_sort/

"""
数据量较小（n<50）
对空间复杂度要求严格的场景

总结
选择排序是一种简单直观的排序算法，通过不断选择未排序区间的最小元素来构建有序序列。

优点：实现简单，空间复杂度低，交换次数少
缺点：时间复杂度高，不适合大规模数据
"""


#代码实现
class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        n = len(nums)
        for i in range(n - 1):
            # 找到未排序区间中最小元素的位置
            min_i = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 交换元素
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.selectionSort(nums)
    

"""
练习题

题目：
给定一个整数数组nums。
要求：将该数组升序排列。

说明：
1≤nums.length≤5∗10^4 
−5∗10^4≤nums[i]≤5∗10^4
"""

