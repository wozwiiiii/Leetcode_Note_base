#原教程地址：https://algo.itcharge.cn/01_array/01_12_array_radix_sort/

"""
适用场景：
整数排序，位数不多（k较小）
数据范围大但位数固定
电话号码、身份证号等固定位数数据

总结:
基数排序是一种非比较排序算法，通过按位分配和收集实现排序。

优点：时间复杂度与数据范围无关，稳定排序，适合固定位数数据
缺点：空间复杂度较高，只适用于整数排序
练习题目
"""

#代码实现
class Solution:
    def radixSort(self, nums: [int]) -> [int]:
        # 获取最大位数
        size = len(str(max(nums)))
        
        # 从个位开始逐位排序
        for i in range(size):
            # 创建 10 个桶，每个桶分别代表 0 ~ 9 中的 1 个数字
            buckets = [[] for _ in range(10)]
            
            # 按当前位数字分桶
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            
            # 重新收集
            nums.clear()
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)
                    
        # 完成排序，返回结果数组
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.radixSort(nums)




"""
练习题
给定一个无序数组nums。

要求：
找出数组在排序之后，相邻元素之间最大的差值。如果数组元素个数小于2，则返回0。

说明：
所有元素都是非负整数，且数值在32位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
"""
