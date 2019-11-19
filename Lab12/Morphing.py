#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <11/13/2019>
#######################################################

import numpy as np
import scipy
import imageio
import matplotlib
from matplotlib.path import Path
from scipy.spatial import Delaunay
from scipy import interpolate


def loadTriangles(leftPointFilePath, rightPointFilePath):
    with open(leftPointFilePath, "r") as f:
        contents_left = f.readlines()
    with open(rightPointFilePath, "r") as f:
        contents_right = f.readlines()
    left = []
    right = []
    # get left and right point list
    for index in range(len(contents_left)):
        xl, yl = contents_left[index].split()
        xr, yr = contents_right[index].split()
        left.append([xl, yl])
        right.append([xr, yr])
    l_nparr = np.array(left)
    r_nparr = np.array(right)
    # get the delaunay triangle pairs on left image
    l_tri = Delaunay(l_nparr)

    tri_leftlist = []
    tri_rightlist = []
    # get all left and right triangles
    for index in range(len(l_nparr[l_tri.simplices])):
        l_pair = l_nparr[l_tri.simplices][index]
        r_pair = r_nparr[l_tri.simplices][index]
        new_leftarray = np.array(l_pair, dtype=np.float64)
        new_lefttri = Triangle(new_leftarray)
        tri_leftlist.append(new_lefttri)
        new_rightarray = np.array(r_pair, dtype=np.float64)
        new_righttri = Triangle(new_rightarray)
        tri_rightlist.append(new_righttri)
        # print(new_lefttri)

    return tri_leftlist, tri_rightlist


class Triangle:
    def __init__(self, vertices: np.array):
        if vertices.dtype is not np.dtype("float64"):
            raise ValueError("The arguments should be an array of float numbers.")
        if vertices.shape != (3, 2):
            raise ValueError("The argument should be a 3x2 array.")
        self.vertices = vertices

    def __str__(self):
        return str(self.vertices[0]) + str(self.vertices[1]) + str(self.vertices[2])

    def getPoints(self):
        # using matplotlib caontains_points function, slow, might need update
        path = Path(self.vertices)
        final_list = []

        # this way is about 10s faster than the previous one
        ux = np.ceil(max(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]))
        uy = np.ceil(max(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]))
        lx = np.round(min(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]), 0) - 1
        ly = np.round(min(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]), 0) - 1
        x, y = np.meshgrid(np.arange(lx, ux+1), np.arange(ly, uy+1))  # make a canvas with coordinates
        x, y = x.flatten(), y.flatten()
        points = np.vstack((x, y)).T

        # not sure whether to include the edge points or not
        grid = path.contains_points(points, radius=0.05)

        for index in range(len(grid)):
            if grid[index] is np.bool_(True):
                final_list.append(points[index])
        return np.array(final_list, dtype=np.float64)


def getInterpolation(origin, target):
    A1 = [origin.vertices[0][0], origin.vertices[0][1], 1, 0, 0, 0,
          0, 0, 0, origin.vertices[0][0], origin.vertices[0][1], 1]
    A2 = [origin.vertices[1][0], origin.vertices[1][1], 1, 0, 0, 0,
          0, 0, 0, origin.vertices[1][0], origin.vertices[1][1], 1]
    A3 = [origin.vertices[2][0], origin.vertices[2][1], 1, 0, 0, 0,
          0, 0, 0, origin.vertices[2][0], origin.vertices[2][1], 1]
    A = np.reshape([A1, A2, A3], (6, 6))
    # print(A)
    # print()
    b = [target.vertices[0][0], target.vertices[0][1], target.vertices[1][0], target.vertices[1][1],
         target.vertices[2][0], target.vertices[2][1]]
    B = np.reshape(b, (6, 1))
    # print(B)
    # print()
    h = np.linalg.solve(A, B)
    H = np.reshape([h[0][0], h[1][0], h[2][0], h[3][0], h[4][0], h[5][0], 0, 0, 1], (3, 3))
    return H


class Morpher:
    def __init__(self, leftImage: np.array, leftTriangles, rightImage: np.array, rightTriangles):
        if leftImage.dtype is not np.dtype("uint8"):
            raise TypeError("LeftImage shoule be a numpy array of uniy8 type.")
        for triangle in leftTriangles:
            if not isinstance(triangle, Triangle):
                raise TypeError("LeftTriangles should be a list of Triangle instances.")
        if rightImage.dtype is not np.dtype("uint8"):
            raise TypeError("RightImage shoule be a numpy array of uniy8 type.")
        for triangle in rightTriangles:
            if not isinstance(triangle, Triangle):
                raise TypeError("RightTriangles should be a list of Triangle instances.")
        self.leftImage = leftImage
        self.leftTriangles = leftTriangles
        self.rightImage = rightImage
        self.rightTriangles = rightTriangles

    def getImageAtAlpha(self, alpha: float):
        if alpha == 0:
            return self.leftImage
        elif alpha == 1:
            return self.rightImage
        else:
            m, n = self.leftImage.shape
            # m: 1080 n: 1440 m is the row and n is the col
            # x is col and y is row
            x = np.arange(n)
            y = np.arange(m)
            # f_left = interpolate.interp2d(x, y, self.leftImage)
            # f_right = interpolate.interp2d(x, y, self.rightImage)
            f_left = interpolate.RectBivariateSpline(y, x, self.leftImage)
            f_right = interpolate.RectBivariateSpline(y, x, self.rightImage)
            result = np.empty([m, n], dtype=np.uint8)
            for index in range(len(self.leftTriangles)):
                left = self.leftTriangles[index]
                right = self.rightTriangles[index]
                # get the target triangle
                tar_vertice = left.vertices*(1-alpha)+right.vertices*alpha
                tar_tri = Triangle(tar_vertice)

                # get interpolation matrix on left and right images
                H_left = getInterpolation(left, tar_tri)
                H_right = getInterpolation(right, tar_tri)
                H_left_inv = np.linalg.inv(H_left)
                H_right_inv = np.linalg.inv(H_right)

                # get points of target triangle
                points = tar_tri.getPoints()
                for point in points:
                    a = np.reshape([point[0], point[1], 1], (3, 1))
                    b_left = np.matmul(H_left_inv, a)
                    b_right = np.matmul(H_right_inv, a)

                    # left_value = np.float64(f_left(b_left[0][0], b_left[1][0]))
                    # right_value = np.float64(f_right(b_right[0][0], b_right[1][0]))
                    left_value = np.float64(f_left(b_left[1][0], b_left[0][0]))
                    right_value = np.float64(f_right(b_right[1][0], b_right[0][0]))
                    result_value = np.uint8(np.round(left_value*(1-alpha) + right_value*alpha))
                    result[int(point[1])][int(point[0])] = result_value
            return result


if __name__ == "__main__":
    # vertice = np.array([[1, 2], [5, 7], [0, 4]], dtype=np.float64)
    # t1 = Triangle(vertice)
    # print(t1.getPoints())
    leftpath = "./points.left.txt"
    rightpath = "./points.right.txt"
    leftTri, rightTri = loadTriangles(leftpath, rightpath)
    test = np.array([[1, 2], [5, 7], [0, 4]], dtype=np.uint8)
    left_image = imageio.imread('./LeftGray.png')
    right_image = imageio.imread('./RightGray.png')
    m1 = Morpher(left_image, leftTri, right_image, rightTri)
    result = m1.getImageAtAlpha(0.5)
    imageio.imwrite('./result.png', result)
    print("finish")



