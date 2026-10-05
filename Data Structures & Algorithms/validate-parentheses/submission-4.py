class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','{','[']
        close_brackets = [')','}',']']

        stack = []
        if len(s)%2 !=0:
            return False
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in close_brackets and len(stack)!=0 :
                last_one=stack.pop()
                if open_brackets.index(last_one)!=close_brackets.index(char):
                    return False
            else:
                return False
        if len(stack)>0:
            return False
        return True
                
        