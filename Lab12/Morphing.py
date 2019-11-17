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


def loadTriangles(leftPointFilePath, rightPointFilePath):
    with open(leftPointFilePath, "r") as f:
        contents_left = f.readlines()
    with open(rightPointFilePath, "r") as f:
        contents_right = f.readlines()
    left = []
    right = []
    for index in range(len(contents_left)):
        xl, yl = contents_left[index].split()
        xr, yr = contents_right[index].split()
        left.append([xl, yl])
        right.append([xr, yr])
    l_nparr = np.array(left)
    r_nparr = np.array(right)
    l_tri = Delaunay(l_nparr)
    # r_tri = Delaunay(r_nparr)

    tri_leftlist = []
    tri_rightlist = []

    for index in range(len(l_nparr[l_tri.simplices])):
        l_pair = l_nparr[l_tri.simplices][index]
        r_pair = r_nparr[l_tri.simplices][index]
        new_leftarray = np.array(l_pair, dtype=np.float64)
        new_lefttri = Triangle(new_leftarray)
        tri_leftlist.append(new_lefttri)
        new_rightarray = np.array(r_pair, dtype=np.float64)
        new_righttri = Triangle(new_rightarray)
        tri_rightlist.append(new_righttri)
        print(new_lefttri, new_righttri)

    return tri_leftlist, tri_rightlist



class Triangle:
    def __init__(self, vertices: np.array):
        if vertices.dtype is not np.dtype("float64"):
            # print(vertices.dtype)
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
        # lx = np.round(min(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]), 0)-1
        # ux = np.round(max(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]), 0)+1
        # ly = np.round(min(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]), 0)-1
        # uy = np.round(max(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]), 0)+1
        #
        # for i in range(int(lx), int(ux)+1):
        #     for j in range(int(ly), int(uy)+1):
        #         if path.contains_point([i, j]) is True:
        #             final_list.append([i, j])
        # return np.array(final_list, dtype=np.float64)

        ux = np.ceil(max(self.vertices[0, 0], self.vertices[1, 0], self.vertices[2, 0]))
        uy = np.ceil(max(self.vertices[0, 1], self.vertices[1, 1], self.vertices[2, 1]))
        x, y = np.meshgrid(np.arange(ux+1), np.arange(uy+1))  # make a canvas with coordinates
        x, y = x.flatten(), y.flatten()
        points = np.vstack((x, y)).T

        # not sure whether to include the edge points or not
        grid = path.contains_points(points, radius=0.05)

        for index in range(len(grid)):
            if grid[index] is np.bool_(True):
                final_list.append(points[index])
        return np.array(final_list, dtype=np.float64)




# class Morpher:
#     def __init__(self):





if __name__ == "__main__":
    vertice = np.array([[1, 2], [5, 7], [0, 4]], dtype=np.float64)
    t1 = Triangle(vertice)
    # print(t1.getPoints())
    leftpath = "./points.left.txt"
    rightpath = "./points.right.txt"
    loadTriangles(leftpath, rightpath)



