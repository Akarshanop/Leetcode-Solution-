class Solution:
    def twoSum(self, nums, target):
        mpp={}
        for i in range(len(nums)):
            element=target-nums[i]
            if element in mpp:
                return [i,mpp[element]]
            mpp[nums[i]]=i
        
solution = Solution()
print(solution.twoSum([1,2,3,4,5,6],10))