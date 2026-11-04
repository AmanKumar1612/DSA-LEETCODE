class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def check(no,flag,arr):
            if no == n:
                ans.append(''.join(arr))
                return
            arr[no] = '1'
            
            check(no+1,True,arr)
            if flag:
                arr[no]='0'
                check(no+1,False,arr)
                arr[no]='1'
            
            
        arr=['0' for _ in range(n)]
        check(0,True,arr)
        return ans