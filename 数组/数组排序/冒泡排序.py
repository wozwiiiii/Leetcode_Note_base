#原网址：https://algo.itcharge.cn/01_array/01_03_array_bubble_sort/

"""
适用场景：
数据量较小（n<50）
数据基本有序

总结
冒泡排序是最简单的排序算法之一，通过相邻元素比较交换实现排序。
虽然实现简单，但效率较低。

优点：实现简单，稳定排序，空间复杂度低。
缺点：时间复杂度高，交换次数多
"""

#代码实现
class Solution:
    def bubbleSort(self, nums: [int]) -> [int]:
        """冒泡排序算法实现"""
        n = len(nums)
        # 外层循环控制趟数，每一趟将当前未排序区间的最大值「冒泡」到末尾
        for i in range(n - 1):
            swapped = False  # 记录本趟是否发生过交换
            # 内层循环负责相邻元素两两比较，将较大值后移
            for j in range(n - i - 1):
                # 如果前一个元素大于后一个元素，则交换
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True  # 发生了交换
            # 如果本趟没有发生任何交换，说明数组已经有序，可以提前结束
            if not swapped:
                break
        return nums  # 返回排序后的数组

    def sortArray(self, nums: [int]) -> [int]:
        """排序数组的接口，调用冒泡排序"""
        return self.bubbleSort(nums)
    


"""
练习题
描述：给定一个数组nums。

要求：将所有0移动到末尾，并保持原有的非0数字的相对顺序。

说明：
只能在原数组上进行操作。
1≤nums.length≤10^4
-2^31≤nums[i]≤-2^31 - 1。
"""
