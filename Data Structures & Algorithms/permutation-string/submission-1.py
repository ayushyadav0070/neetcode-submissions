class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=''.join(sorted(s1))
        n=len(s1)
        for i in range(len(s2)-n+1):
            cur= ''.join(sorted(s2[i:i+n]))
            if cur==s1:
                return True
        return False

