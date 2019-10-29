#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/16/2019>
#######################################################

class Rectangle:
    def __init__(self, llPoint: tuple, urPoint: tuple):
        xll, yll = llPoint
        xur, yur = urPoint
        if xll >= xur or yll >= yur:
            raise ValueError("Coordinates value not correct! Lower left value should be smaller than upper right value.")
        self.lowerLeft = llPoint
        self.upperRight = urPoint

    def __str__(self):
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        return f"A rectangle with upper right point ({'%.2f' % xur},{'%.2f' % yur}) and lower left point ({'%.2f' % xll},{'%.2f' % yll})"

    def isSquare(self):
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        if xur - xll == yur - yll:
            return True
        else:
            return False

    def intersectsWith(self, rect):
        if isinstance(rect, Rectangle):
            xll, yll = self.lowerLeft
            xur, yur = self.upperRight
            new_xll, new_yll = rect.lowerLeft
            new_xur, new_yur = rect.upperRight
            if xll < new_xll < xur or xll < new_xur < xur:
                if yll < new_yll < yur or yll < new_yur < yur:
                    return True
            else:
                return False
        else:
            raise TypeError("Rect variable should be an instance of Rectangle class.")

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Second variable should be an instance of Rectangle class.")
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        area = (xur - xll) * (yur - yll)
        new_xll, new_yll = other.lowerLeft
        new_xur, new_yur = other.upperRight
        newarea = (new_xur - new_xll) * (new_yur - new_yll)
        if area == newarea:
            return True
        else:
            return False


class Circle:
    def __init__(self, center: tuple, radius: float):
        if radius <= 0:
            raise ValueError("The radius of a circle must be greater than 0.")
        self.center = center
        self.radius = radius

    def __str__(self):
        x1, y1 = self.center
        return f"A circle with a center point ({'%.2f' % x1},{'%.2f' % y1}) and a radius {'%.2f' % self.radius}."

    def intersectsWith(self, other):
        if isinstance(other, Circle):
            x1, y1 = self.center
            r1 = self.radius
            x2, y2 = other.center
            r2 = other.radius
            if ((x1-x2)*(x1-x2) + (y1-y2)*(y1 - y2)) < (r1+r2)*(r1+r2):
                return True
            else:
                return False
        elif isinstance(other, Rectangle):
            x1, y1 = self.center
            r1 = self.radius
            xll, yll = other.lowerLeft
            xur, yur = other.upperRight
            if x1 < xll:
                if y1 < yll:
                    if (x1-xll)*(x1-xll) + (y1-yll)*(y1-yll) < r1*r1:
                        return True
                elif y1 > yur:
                    if (x1-xll)*(x1-xll) + (y1-yur)*(y1-yur) < r1*r1:
                        return True
                else:
                    if xll - x1 < r1:
                        return True
                return False
            elif x1 > xur:
                if y1 < yll:
                    if (x1-xur)*(x1-xur) + (y1-yll)*(y1-yll) < r1*r1:
                        return True
                elif y1 > yur:
                    if (x1 - xur) * (x1 - xur) + (y1 - yur) * (y1 - yur) < r1 * r1:
                        return True
                else:
                    if x1-xur < r1:
                        return True
                return False
            else:
                if y1 > yur:
                    if y1 - yur < r1:
                        return True
                elif y1 < yll:
                    if yll - y1 < r1:
                        return True
                else:
                    return True
                return False
        else:
            raise TypeError("The second variable should either be a Circle or a Rectangle.")


if __name__ == "__main__":
    rect = Rectangle((1.5, 2.0), (3.0, 4.5))
    # rect2 = Rectangle((1.5, 2.0), (1.0, 4.5))
    rect2 = Rectangle((1.5, 2.0), (4.0, 4.5))
    print(rect)
    print(rect2)
    print(rect.isSquare())
    print(rect2.isSquare())
    print(rect == rect2)
    print(rect.intersectsWith(rect2))
    # print(rect == ((1.5, 2.0), (3.0, 4.5)))
    circle = Circle((2.5, 3.0), 1.5)
    circle2 = Circle((3.0, 4.0), 2.5)
    print(circle)
    print(circle2)
    print(circle.intersectsWith(circle2))
    print(circle.intersectsWith(rect))
    # print(circle.intersectsWith(((2.5, 3.0), 1.5)))
