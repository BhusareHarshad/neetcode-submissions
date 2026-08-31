class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_Map = {}
        for i in range(n):
            incom = target - nums[i]
            if incom in hash_Map:
                return [hash_Map[incom], i]
            hash_Map[nums[i]] = i

        return [-1, -1]
