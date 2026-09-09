class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub_s = s.replace(" ", "")
        sub_s = "".join(ch for ch in sub_s if ch.isalnum())

        a = 0
        b = len(sub_s)-1

        # print(sub_s)
        
        for i in range(int(len(sub_s)/2)):
            # print(sub_s[a].lower())
            # print(sub_s[b].lower())
            
            if sub_s[a].lower() != sub_s[b].lower():
                return False
            a += 1
            b -= 1

        return True


        