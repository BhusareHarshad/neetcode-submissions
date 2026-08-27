class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        subMap = {}

        for i in range(n):
            sec_num = target - nums[i]
            if sec_num in subMap:
                return [subMap[sec_num], i]
            subMap[nums[i]] = i

        return [-1, -1]