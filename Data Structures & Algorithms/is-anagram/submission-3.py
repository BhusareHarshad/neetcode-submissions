class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def calc_freq_(str_):
            hashMap = {}
            for w in str_:
                if w not in hashMap:
                    hashMap[w] = 1
                else:
                    hashMap[w] += 1

            return hashMap

        return calc_freq_(s) == calc_freq_(t)