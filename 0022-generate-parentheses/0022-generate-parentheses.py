class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def generate(total,arr,i):
            if total == 0 and i == (2*n):
                ans.append(''.join(arr)[::])
                return
            if total < 0 or total > (n) or i == (2*n):
                return
            arr[i] = '('
            total+=1
            generate(total,arr,i+1)
            arr[i] =''
            total-=1
            arr[i] =')'
            total-=1
            generate(total,arr,i+1)
        arr=[''] * (2*n)
        generate(0,arr,0)
        return ans