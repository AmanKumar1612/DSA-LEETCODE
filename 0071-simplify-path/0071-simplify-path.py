class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        s=path.split('/')
        for i in s:
            if i=='..':
                if stack:
                    stack.pop()
            elif i=='' or i=='.':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)