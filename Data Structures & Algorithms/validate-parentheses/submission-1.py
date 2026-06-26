class Solution:
    def isValid(self, st: str) -> bool:
        s=[]
        for ch in st:
            if ch=='(':
                s.append(ch)
            elif ch=='[':
                s.append(ch)
            elif ch=='{':
                s.append(ch)
            else:
                if (len(s)==0) or (ch==')' and s[-1]!='(') or (ch=='}' and s[-1]!='{') or (ch==']' and s[-1]!='['):
                    return False
                else:
                    s.pop()
        return len(s)==0