#源网址：https://algo.itcharge.cn/01_array/01_07_array_merge_sort/

"""
适用场景：
大规模数据排序（n>1000）
对稳定性有要求的场景
外部排序（数据无法全部加载到内存）
链表排序

总结
归并排序是一种高效稳定的排序算法，
采用分治策略将数组递归分解后合并排序。

优点：
时间复杂度稳定，始终为 O(nlogn)
稳定排序，相等元素相对位置不变
适合大规模数据排序
可用于外部排序和链表排序
缺点：
空间复杂度较高，需要 O(n) 额外空间
对于小规模数据，常数因子较大
不是原地排序算法
"""

class Solution:
    # 合并过程
    def merge(self, left_nums: [int], right_nums: [int]):
        nums = []
        left_i, right_i = 0, 0
        
        # 合并两个有序子数组
        while left_i < len(left_nums) and right_i < len(right_nums):
            if left_nums[left_i] <= right_nums[right_i]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_i])
                right_i += 1
        
        # 如果左子数组有剩余元素，则将其插入到结果数组中
        while left_i < len(left_nums):
            nums.append(left_nums[left_i])
            left_i += 1
        
        # 如果右子数组有剩余元素，则将其插入到结果数组中
        while right_i < len(right_nums):
            nums.append(right_nums[right_i])
            right_i += 1
        
        # 返回合并后的结果数组
        return nums

    # 分解过程
    def mergeSort(self, nums: [int]) -> [int]:
        # 数组元素个数小于等于 1 时，直接返回原数组
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2                        # 将数组从中间位置分为左右两个数组
        left_nums = self.mergeSort(nums[0: mid])    # 递归将左子数组进行分解和排序
        right_nums =  self.mergeSort(nums[mid:])    # 递归将右子数组进行分解和排序
        return self.merge(left_nums, right_nums)    # 把当前数组组中有序子数组逐层向上，进行两两合并

    def sortArray(self, nums: [int]) -> [int]:
        return self.mergeSort(nums)


"""
练习题
描述：给定两个有序数组nums1、nums2。

要求：将nums2合并到nums1中，使nums1成为一个有序数组。

说明：
1、给定数组nums1 空间大小为$ m + n$ 个，其中前m个为nums1 的元素。
nums2 空间大小为n。这样可以用 nums1 的空间来存储最终的有序数组。
2、nums1.length==m+n。
3、nums2.length==n。
4、0≤m,n≤200。
5、1≤m+n≤200。
6、−10^9≤nums1[i],nums2[j]≤10^9
"""    
