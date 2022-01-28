class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        List = []
        runningSum = 0
        for i in nums:
            runningSum += i
            List.insert(len(List), runningSum)
        print(List)
        return List

solution = Solution()
solution.runningSum([1,2,3,4])