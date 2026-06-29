class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lv=height[l]
        rv=height[r]
        area=0
        while l<r:
            if lv<rv:
                l+=1
                lv=max(lv,height[l])
                area+=lv-height[l]
            else:
                r-=1
                rv=max(rv,height[r])
                area+=rv-height[r]
        return area