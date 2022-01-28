class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 0
        ans = []
        for i in nums:
            k = 0
            for j in nums:
                if i > j:
                    k += 1
            ans.insert(len(ans),k)
        print(ans)

sol = Solution()
sol.smallerNumbersThanCurrent([8,1,2,2,3])