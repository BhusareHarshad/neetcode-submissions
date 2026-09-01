class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def calc_freq(str_):
            hashMap = {}
            for let in str_:
                if let not in hashMap:
                    hashMap[let] = 1
                else:
                    hashMap[let] += 1

            return hashMap

        return calc_freq(s) == calc_freq(t)
        