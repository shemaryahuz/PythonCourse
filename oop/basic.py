class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x()

    def get_y(self):
        return self.y

point1 = Point(2,3)
point2 = Point(4,4)
point3 = Point(1,7)

points = [point1,point2,point3]

is_min = points[0].x
for i in range(1,len(points)):
    if points[i].x < is_min:
        is_min = points[i].x
print(is_min)

sum_all = 0
for point in points:
    sum_all += point.x + point.y
print(sum_all)

