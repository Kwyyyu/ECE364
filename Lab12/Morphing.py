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
import os
import shutil


def loadTriangles(leftPointFilePath, rightPointFilePath):
    with open(leftPointFilePath, "r") as f:
        contents_left = f.readlines()
    with open(rightPointFilePath, "r") as f:
        contents_right = f.readlines()
    left = []
    right = []
    # get left and right point list
    for index in range(len(contents_left)):
        if contents_left[index] != "\n" and contents_right[index] != "\n":
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
        if not isinstance(vertices, np.ndarray):
            raise ValueError("The argument should be a numpy array.")
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
        lx = np.ceil(min(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]))
        ly = np.ceil(min(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]))
        x, y = np.meshgrid(np.arange(lx, ux+1), np.arange(ly, uy+1))  # make a canvas with coordinates
        x, y = x.flatten(), y.flatten()
        points = np.vstack((x, y)).T

        # not sure whether to include the edge points or not
        grid = path.contains_points(points, radius=0.05)

        # for index in range(len(grid)):
        #     if grid[index] is np.bool_(True):
        #         final_list.append(points[index])
        index_list = list(filter(lambda i: grid[i] is np.bool_(True), range(len(grid))))
        final_list = points[index_list]
        return np.array(final_list, dtype=np.float64)


def getInterpolation(origin, target):
    # A1 = [origin.vertices[0][0], origin.vertices[0][1], 1, 0, 0, 0,
    #       0, 0, 0, origin.vertices[0][0], origin.vertices[0][1], 1]
    # A2 = [origin.vertices[1][0], origin.vertices[1][1], 1, 0, 0, 0,
    #       0, 0, 0, origin.vertices[1][0], origin.vertices[1][1], 1]
    # A3 = [origin.vertices[2][0], origin.vertices[2][1], 1, 0, 0, 0,
    #       0, 0, 0, origin.vertices[2][0], origin.vertices[2][1], 1]
    A = [[origin.vertices[0][0], origin.vertices[0][1], 1, 0, 0, 0],
                  [0, 0, 0, origin.vertices[0][0], origin.vertices[0][1], 1],
                  [origin.vertices[1][0], origin.vertices[1][1], 1, 0, 0, 0],
                  [0, 0, 0, origin.vertices[1][0], origin.vertices[1][1], 1],
                  [origin.vertices[2][0], origin.vertices[2][1], 1, 0, 0, 0],
                  [0, 0, 0, origin.vertices[2][0], origin.vertices[2][1], 1]]

    B = [[target.vertices[0][0]],
         [target.vertices[0][1]],
         [target.vertices[1][0]],
         [target.vertices[1][1]],
         [target.vertices[2][0]],
         [target.vertices[2][1]]]

    h = np.linalg.solve(A, B)
    H = [[h[0][0], h[1][0], h[2][0]],
         [h[3][0], h[4][0], h[5][0]],
         [0, 0, 1]]
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
        elif alpha > 1 or alpha < 0:
            raise ValueError("Alpha should be in range of 0 and 1.")
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
            for left, right in zip(self.leftTriangles, self.rightTriangles):
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
                extra = np.ones((points.shape[0], 1))
                a = np.hstack((points, extra)).transpose()

                b_left = np.matmul(H_left_inv, a)
                b_right = np.matmul(H_right_inv, a)

                left_value = f_left(b_left[1], b_left[0], grid=False)
                right_value = f_right(b_right[1], b_right[0], grid=False)
                result_value = np.uint8(left_value * (1 - alpha) + right_value * alpha)

                for index in range(len(points)):
                    result[int(points[index][1]), int(points[index][0])] = result_value[index]
            return result

    def saveVideo(self, targetFilePath: str, frameCount: int, frameRate: int, includeReversed=True):
        if targetFilePath[len(targetFilePath)-4:len(targetFilePath)] != ".mp4":
            raise ValueError('Wrong file path! Should have an extension of ".mp4".')
        if (not isinstance(frameCount, int)) or frameCount < 10:
            raise ValueError("FrameCount should be an integer larger than or equal to 10.")
        if (not isinstance(frameRate, int)) or frameCount < 5:
            raise ValueError("FrameRate should be an integer larger than or equal to 5.")
        if not isinstance(includeReversed, bool):
            raise TypeError("IncludeReverse should be a boolean variable.")

        alpha_list = np.arange(0, 1, 1.0/(frameCount-1))
        alpha_list = np.append(alpha_list, [1.0])
        index = 1
        if os.path.isdir("./temp/"):
            shutil.rmtree("./temp")
        os.mkdir("./temp")
        result_list = []
        for alpha in alpha_list:
            result = self.getImageAtAlpha(alpha)
            result_list.append(result)
            index_new = "%03d" % index
            path = "./temp/result_" + index_new + ".png"
            imageio.imwrite(path, result)
            index += 1
        if includeReversed:
            result_list.reverse()
            for result in result_list:
                index_new = "%03d" % index
                path = "./temp/result_" + index_new + ".png"
                imageio.imwrite(path, result)
                index += 1

        command = "ffmpeg -framerate " + str(frameRate) + " -i ./temp/result_%03d.png " + targetFilePath
        os.system(command)
        shutil.rmtree("./temp")


if __name__ == "__main__":

    leftpath = "./points.left.txt"
    rightpath = "./points.right.txt"
    leftTri, rightTri = loadTriangles(leftpath, rightpath)

    left_image = imageio.imread('./LeftGray.png')
    right_image = imageio.imread('./RightGray.png')
    m1 = Morpher(left_image, leftTri, right_image, rightTri)
    # result = m1.getImageAtAlpha(0.75)
    # imageio.imwrite('./result.png', result)

    m1.saveVideo("./rv.mp4", 11, 5, True)


    print("finish")



