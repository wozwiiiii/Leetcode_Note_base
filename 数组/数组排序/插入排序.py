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

#测试

#创建Solution类的实例
solution = Solution()

# 定义一个待排序的整数数组
nums = [22, 27, 16, 2, 18, 6]

# 调用sortArray方法进行排序
sorted_nums = solution.sortArray(nums)

# 输出排序后的数组
print(sorted_nums)



"""
题目：
给定一个整数数组nums。
要求：将该数组升序排列。
说明：
1≤nums.length≤5∗10^4 
−5∗10^4≤nums[i]≤5∗10^4
"""
test = []
exper = True

#输入测试元素
while exper:
    a = int(input("输入元素:"))
    test.append(a)
    if len(test) >= 3:
        exper = False

#元素排序（插入排序）    

#外层循环实现遍历无序区间元素     
for i in range(len(test)):
    temp = test[i]
    j = i

    #内层循环遍历有序区间元素并实现大小比较
    while j > 0 and test[j - 1] > temp:
        test[i] = test[j - 1]
        j -= 1
        test[j] = temp

print(test)        



