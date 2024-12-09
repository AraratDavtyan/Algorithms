import math
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def graham_scan(points):
    pivot = min(points, key=lambda p: (p[1], p[0]))

    points.sort(key=lambda p: (math.atan2(p[1] - pivot[1], p[0] - pivot[0]), p))

    hull = [pivot, points[0], points[1]]

    for i in range(2, len(points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()  
        hull.append(points[i])  

    return hull

points = [(0, 0), (2, 1), (1, 2), (3, 3), (0, 3), (3, 0), (2, 2)]
convex_hull = graham_scan(points)

print("Convex Hull Points:")
for point in convex_hull:
    print(point)

