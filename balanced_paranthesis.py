class ValidParanthesis:
    
    def __init__(self,s,n):
        self.s = s
        self.n = n
        
    def is_valid(self):
        l = []
        for i in range(self.n):
            if self.s[i]=='{' or s[i]=='[' or s[i]=='(':
                l.append(self.s[i])
            elif self.s[i]=='}' and l and l[-1]=='{':
                l.pop()
            elif self.s[i]==')' and l and l[-1]=='(':
                l.pop()
            elif self.s[i]==']' and l and l[-1]=='[':
                l.pop()
            else:
                return False
        if not l:
            return True
        return False
        
s = input()
cls = ValidParanthesis(s,len(s))
print("Balanced" if cls.is_valid() else "Not Balanced")