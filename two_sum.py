class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp={}
        for i in range(len(nums)):
            element=target-nums[i]
            if element in mpp:
                return [i,mpp[element]]
            mpp[nums[i]]=i
