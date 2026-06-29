class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=[float('-inf')]
        l=len(height)
        for i in range(1,l):
            l_max.append(max(l_max[i-1],height[i-1]))
        r_max=[float('-inf')]*(l)
        
        for i in range(l-2,-1,-1):
            r_max[i]=max(r_max[i+1],height[i+1])
        area=0
        for i in range(l):
            m=min(l_max[i],r_max[i])
            m=m-height[i]
            if m<=0:
                m=0
            area+=m
        return area
        