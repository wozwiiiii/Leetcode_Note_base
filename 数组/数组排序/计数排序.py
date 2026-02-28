#源地址：https://algo.itcharge.cn/01_array/01_10_array_counting_sort/

"""
适用场景：
整数排序
数值范围较小（k远小于n）
对稳定性有要求的场景

总结:
计数排序是一种非比较排序算法，通过统计元素频次实现排序。它特别适合数值范围较小的整数排序。

优点：时间复杂度稳定，稳定排序，适合小范围整数排序
缺点：空间复杂度与数值范围相关，不适合大范围数值
"""

#代码实现
class Solution:
    def countingSort(self, nums: [int]) -> [int]:
        # 确定数值范围
        nums_min, nums_max = min(nums), max(nums)
        size = nums_max - nums_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计每个元素出现的次数
        for num in nums:
            counts[num - nums_min] += 1
        
        # 计算累积频次（每个元素出现的次数）
        for i in range(1, size):
            counts[i] += counts[i - 1]

        # 逆序填充结果数组
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 根据累积计数数组，将 num 放在数组对应位置
            res[counts[num - nums_min] - 1] = num
            counts[num - nums_min] -= 1

        return res

    def sortArray(self, nums: [int]) -> [int]:
        return self.countingSort(nums)
    


"""
练习题
描述：
给定两个数组，arr1 和 arr2，其中arr2 中的元素各不相同，arr2中的每个元素都出现在arr1 中。

要求：
对arr1 中的元素进行排序，使arr1 中项的相对顺序和arr2中的相对顺序相同。
未在arr2中出现过的元素需要按照升序放在arr1 的末尾。

说明：
1≤arr1.length,arr2.length≤1000。
0≤arr1[i],arr2[i]≤1000。
"""    