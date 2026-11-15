class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        for ch in s:
            if ch in d:
                stack.append(d[ch])
            else:
                if not stack or stack.pop()!=ch:
                    return False
        return not stack
        