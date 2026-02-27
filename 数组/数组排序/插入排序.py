#插入排序详细解析：https://algo.itcharge.cn/01_array/01_05_array_insertion_sort/
"""
使用场景：
  数据量较小（n<50）
  数据基本有序
  在线排序（数据逐个到达）

总结：  
  插入排序是一种简单直观的排序算法，通过逐步构建有序序列实现排序。
  优点：实现简单，稳定排序，空间复杂度低，对基本有序数据效率高
  缺点：时间复杂度高，不适合大规模数据
"""

#插入排序代码实现
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        #遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            #从右到左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                #将大于temp的元素右移
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp
        return nums    
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.insertionSort(nums) 
           


