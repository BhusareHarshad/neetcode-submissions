class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #freq calc
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        so_hp = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)[:k]

        return [k for k, _ in so_hp]
            