class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums) - 1):
            if nums[i] != nums[i + 1]:
                i += 1
            else:
                nums.pop(i + 1)
       
        return len(nums), nums

sol = Solution()
sol.removeDuplicates([1,1,2,4,4,5,6,6])