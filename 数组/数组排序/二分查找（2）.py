#源地址：https://algo.itcharge.cn/01_array/01_14_array_binary_search_02/


"""
两种思路适用范围:

1、直接法：因为判断语句是 left <= right，有时候要考虑返回是 left 还是right。
循环体内有 3 个分支，并且一定有一个分支用于退出循环或者直接返回。
这种思路适合解决简单题目。即要查找的元素性质简单，数组中都是非重复元素，且 ==、>、< 的情况非常好写的时候。

2、排除法：更加符合二分查找算法的减治思想。每次排除目标元素一定不存在的区间，达到减少问题规模的效果。
然后在可能存在的区间内继续查找目标元素。这种思路适合解决复杂题目。比如查找一个数组里可能不存在的元素，找边界问题，可以使用这种思路。


总结：
二分查找的细节问题包括区间开闭、mid取值、循环条件和搜索范围的选择。

区间开闭：建议使用左闭右闭区间，这样逻辑更简单，减少出错可能。

mid取值：通常使用 mid = left + (right - left) // 2，防止整型溢出。
在某些情况下，如 left = mid 时，需向上取整，避免死循环。

循环条件：
left <= right：适用于直接法，循环结束时如果未找到目标，直接返回−1。
left < right：适用于排除法，循环结束时需额外判断 nums[left] 是否为目标值。

搜索范围选择：
直接法：left = mid + 1 或 right = mid - 1，明确缩小范围。
排除法：根据情况选择 left = mid + 1 或 right = mid，以及 right = mid - 1 或 left = mid，确保每次排除无效区间。

两种思路：
直接法：简单直接，适合查找明确存在的元素。
排除法：更通用，适合复杂问题，如边界查找或不确定元素是否存在的情况。
掌握这些细节能更灵活地应用二分查找，避免常见错误
"""


#代码实现
#直接法
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
    

#排除法：两种形式

class Solution_1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 在闭区间 [left, right] 内查找 target
        while left < right:
            # 计算中间位置，向下取整
            mid = left + (right - left) // 2
            # 如果 nums[mid] 小于目标值，排除 [left, mid] 区间，继续在 [mid + 1, right] 查找
            if nums[mid] < target:
                left = mid + 1
            # 否则目标值可能在 [left, mid] 区间，收缩右边界
            else:
                right = mid
        # 循环结束后，left == right，判断该位置是否为目标值
        return left if nums[left] == target else -1



"""
方式二注意：只要出现 left = mid，就要让 mid 向上取整，具体配对如下：
left = mid + 1、right = mid 搭配 mid = left + (right - left) // 2。
right = mid - 1、left = mid 搭配 mid = left + (right - left + 1) // 2
"""
class Solution_2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 在闭区间 [left, right] 内查找 target
        while left < right:
            # 计算中间位置，向上取整，防止死循环
            mid = left + (right - left + 1) // 2
            # 如果 nums[mid] > target，说明目标只可能在 [left, mid - 1] 区间
            if nums[mid] > target:
                right = mid - 1
            # 否则，目标在 [mid, right] 区间（包括 mid）
            else:
                left = mid
        # 循环结束后，left == right，判断该位置是否为目标值
        return left if nums[left] == target else -1    




"""
描述：给你一个整数n，代表已经发布的版本号。还有一个用于检测版本是否出错的接口 isBadVersion(version): 。

要求：找出第一次出错的版本号bad。

说明：
要求尽可能减少对 isBadVersion(version): 接口的调用。
1≤bad≤n≤2^31 - 1
"""