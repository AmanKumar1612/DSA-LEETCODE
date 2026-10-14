class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        def check(arr,vis,n):
            if vis[n]==1:
                return True
            if vis[n]==2:
                return False
            vis[n]=1
            for i in arr[n]:
                if check(arr,vis,i):
                    return True
            vis[n]=2
            return False
        def order(arr,n,x,vis):
            vis[n]=1
            for i in arr[n]:
                if vis[i]== 0:
                    order(arr,i,x,vis)
            x.append(n)
            
        vis=[0]*numCourses
        arr=[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            arr[j].append(i)
        for i in range(numCourses):
            if vis[i] == 0:
                if check(arr,vis,i):
                    return []
        x=[]
        vis=[0]*numCourses
        for i in range(numCourses):
            if vis[i] == 0:
                order(arr,i,x,vis)
        return x[::-1]
