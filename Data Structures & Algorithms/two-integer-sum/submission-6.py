class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashMap = {}
        for i in range(n):
            second_num = target - nums[i]
            if second_num in hashMap:
                return [hashMap[second_num], i]
            hashMap[nums[i]] = i
        return [-1, -1]