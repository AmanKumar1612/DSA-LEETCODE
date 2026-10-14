class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def cycle(arr,vis,i):
            if vis[i] == 1:
                return True
            if vis[i] == 2:
                return False
            vis[i]=1
            for j in arr[i]:
                if cycle(arr,vis,j):
                    return True
            vis[i]=2
            return False
        vis=[0] * numCourses
        arr=[ [] for _ in range(numCourses)]
        for i,j in prerequisites:
            arr[j].append(i)
        for i in range(numCourses):
            if vis[i]==0:
                if cycle(arr,vis,i):
                    return False
        return True
