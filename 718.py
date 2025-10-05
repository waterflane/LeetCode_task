def findLength(nums1: list[int], nums2: list[int]) -> int:
    l1 = len(nums1)
    l2 = len(nums2)
    matrix = [[0 for x in range(l2)] for y in range(l1)]
    
    res = 0
    for y in range(l1):
        for x in range(l2):
            if nums2[x] == nums1[y]:
                if (x != 0 and x != len(nums2) and y != 0) and matrix[y-1][x-1] != 0:
                    res = max(matrix[y-1][x-1]+1, res)
                    matrix[y][x] = matrix[y-1][x-1]+1
                else:
                    res = max(1, res)
                    matrix[y][x] = 1

    return res

print(findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(findLength(nums1 = [0,0,0,0,1], nums2 = [1,0,0,0,0]))
print(findLength(nums1 = [1,1,0,0,1], nums2 = [1,1,0,0,0]))
print(findLength(nums1 = [1,1,0,0,1,0], nums2 = [0,0]))
