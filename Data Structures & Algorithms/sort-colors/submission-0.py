class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(one,two):
            temp = nums[one]
            nums[one] = nums[two]
            nums[two] = temp
        left = 0
        right = len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(i,left)
                left = left + 1
            elif nums[i] == 2:
                swap(i,right)
                right = right - 1
                i = i - 1
            i = i + 1
            


"""
Bucket Sort 

Quick Sort 

Partition



"""