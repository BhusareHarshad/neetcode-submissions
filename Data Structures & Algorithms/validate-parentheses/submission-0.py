class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map_ = {")": "(", "]": "[", "}": "{"}

        for paren in s:
            if paren in hash_map_:
                if stack and stack[-1] == hash_map_[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)

        return True if not stack else False
        