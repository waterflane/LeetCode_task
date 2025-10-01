def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height)-1

    max_volume = 0
    while True:
        if r == l: return max_volume

        now_volume = min(height[l], height[r])*(r-l)
        max_volume = now_volume if max_volume < now_volume else max_volume

        if height[l] < height[r]: l+=1
        else: r -=1 
        
print(maxArea([1,8,6,2,5,4,8,3,7]))
