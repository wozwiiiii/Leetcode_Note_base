#源地址：https://algo.itcharge.cn/01_array/01_13_array_binary_search_01/


"""
核心要点：
二分查找是一种在有序数组中高效查找目标元素的算法，
其核心思想是每次将查找区间缩小一半，从而快速定位目标位置。

算法特点:
时间复杂度：O(logn)，比线性查找O(n) 更高效。
空间复杂度：O(1)，只需要常数级别的额外空间。
适用条件：数据必须是有序的（升序或降序）。
核心思想：减而治之，每次排除一半不可能的区域。

实现要点
区间定义：使用左闭右闭区间 [left, right]。
中间计算：mid = (left + right) // 2 或 mid = left + (right - left) // 2（防溢出）。
边界更新：
目标在右半区间：left = mid + 1
目标在左半区间：right = mid - 1
终止条件：left > right 时查找失败。

应用场景:
在有序数组中查找特定元素
查找插入位置
寻找边界值
数值范围查询
"""


#代码实现
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 循环查找区间为 [left, right]，直到区间为空
        while left <= right:
            # 计算中间位置，防止溢出可写为 left + (right - left) // 2
            mid = (left + right) // 2
            # 命中目标，直接返回下标
            if nums[mid] == target:
                return mid
            # 目标在右半区间，收缩左边界
            elif nums[mid] < target:
                left = mid + 1
            # 目标在左半区间，收缩右边界
            else:
                right = mid - 1
        # 查找失败，返回 -1
        return -1



"""
练习题目：
描述：给定一个排好序的数组nums，以及一个目标值target。

要求：在数组中找到目标值，并返回下标。如果找不到，则返回目标值按顺序插入数组的位置。

说明：
1≤nums.length≤10^4
−10^4≤nums[i]≤10^4
nums 为无重复元素的升序排列数组。
−10^4≤target≤10^4
 。"""