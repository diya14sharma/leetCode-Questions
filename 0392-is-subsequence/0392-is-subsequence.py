class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=0
        for i in t:
            if m<len(s) and s[m]==i:
                m+=1
        return m==len(s)          
        