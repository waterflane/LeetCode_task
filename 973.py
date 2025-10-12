from math import sqrt

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    min_dist_list = []
    points_min_dist_list = []
    
    for i in range(len(points)):
        now_dist = sqrt(points[i][0]**2+points[i][1]**2)

        if len(min_dist_list) < k: 
            points_min_dist_list.append(points[i])
            min_dist_list.append(now_dist)
        elif max(min_dist_list)>now_dist: 
            points_min_dist_list.pop(min_dist_list.index(max(min_dist_list)))
            points_min_dist_list.append(points[i])

            min_dist_list.remove(max(min_dist_list))
            min_dist_list.append(now_dist)


    return points_min_dist_list

print(kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
