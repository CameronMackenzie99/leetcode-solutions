class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0    
        if target < nums[i]:
            i += 1
        elif target == nums[i]:
            print(i)
            return i
        elif target > nums[i]:
             print(i-1)
             return i - 1
           
            # return i
            #     elif target >= nums[i]:
            #         print(i-1)
            # return i - 1
    
sol = Solution()
sol.searchInsert([1,3,5,6], 5)
