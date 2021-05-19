
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = []
    target 
    i = 0
    j = 0
    for i in nums:
        while j == int(len(nums)) - i:
            sum = nums[i] + nums [j]
            j += 1
        i += 1
        if sum == target:
            return "[i,j]"
nums = [1,2,3,4,5]
target = 3
print(twoSum(nums, target))
