#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/31/2019>
#######################################################

import math
import copy
import collections
import enum
import numpy


class Datum:

    def __init__(self, *args):
        self._storage = ()
        for elem in args:
            if isinstance(elem, float) | isinstance(elem, int):
                self._storage += (elem, )
            else:
                raise TypeError("Input is not a float!")

    def __str__(self):
        output = "("
        output += ('%.2f' % self._storage[0])
        for elem in self._storage[1:]:
            output += ", " + ('%.2f' % elem)
        output += ")"
        return output

    def __repr__(self):
        output = "("
        output += ('%.2f' % self._storage[0])
        for elem in self._storage[1:]:
            output += ", " + ('%.2f' % elem)
        output += ")"
        return output

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, d):
        if not isinstance(d, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        else:
            length = min(len(self._storage), len(d._storage))
            sum1 = 0
            for i in range(length):
                sum1 += pow(self._storage[i]-d._storage[i], 2)
            if len(self._storage) > length:
                for i in range(len(self._storage)-length):
                    sum1 += pow(self._storage[i+length], 2)
            else:
                for i in range(len(d._storage)-length):
                    sum1 += pow(d._storage[i+length], 2)
            dis = math.sqrt(sum1)
            return dis

    def clone(self):
        return copy.deepcopy(self)

    def __contains__(self, item):
        if isinstance(item, float) | isinstance(item, int):
            if item in self._storage:
                return True
            else:
                return False
        else:
            raise TypeError("Input is not a float!")

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        self.new = 0
        return self

    def __next__(self):
        val = self.new
        if val == len(self._storage):
            raise StopIteration
        self.new += 1
        return self._storage[val]

    def __neg__(self):
        item = Datum()
        new_tuple = ()
        for val in self._storage:
            new_tuple += (-val, )
        item._storage = new_tuple
        return item

    def __getitem__(self, item):
        return self._storage[item]

    def __add__(self, other):
        final = self.clone()
        final_tuple = ()
        if isinstance(other, Datum):
            length = min(len(self._storage), len(other._storage))
            for i in range(length):
                final_tuple += (self._storage[i]+other._storage[i],)
            if len(self._storage) > length:
                for i in range(len(self._storage) - length):
                    final_tuple += (self._storage[i+length],)
            else:
                for i in range(len(other._storage) - length):
                    final_tuple += (other._storage[i+length],)
        elif isinstance(other, float):
            for i in range(len(self._storage)):
                final_tuple += (self._storage[i] + other,)
        else:
            raise TypeError("Input is nor an instance of Datum type or float type!")
        final._storage = final_tuple
        return final

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        final = self.clone()
        final_tuple = ()
        if isinstance(other, Datum):
            length = min(len(self._storage), len(other._storage))
            for i in range(length):
                final_tuple += (self._storage[i] - other._storage[i],)
            if len(self._storage) > length:
                for i in range(len(self._storage) - length):
                    final_tuple += (self._storage[i + length],)
            else:
                for i in range(len(other._storage) - length):
                    final_tuple += (-other._storage[i + length],)
        elif isinstance(other, float):
            for i in range(len(self._storage)):
                final_tuple += (self._storage[i] - other,)
        else:
            raise TypeError("Input is nor an instance of Datum type or float type!")
        final._storage = final_tuple
        return final

    def __mul__(self, other):
        final = self.clone()
        final_tuple = ()
        if isinstance(other, float):
            for i in range(len(self._storage)):
                final_tuple += (self._storage[i] * other,)
        else:
            raise TypeError("Input is not an instance of float type!")
        final._storage = final_tuple
        return final

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        final = self.clone()
        final_tuple = ()
        if isinstance(other, float):
            for i in range(len(self._storage)):
                final_tuple += (self._storage[i] / other,)
        else:
            raise TypeError("Input is not an instance of float type!")
        final._storage = final_tuple
        return final

    def __eq__(self, other):
        if not isinstance(other, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        origin = Datum()
        dis1 = origin.distanceFrom(self)
        dis2 = origin.distanceFrom(other)
        # print(dis1)
        # print(dis2)
        if dis1 != dis2:
            return False
        else:
            return True

    def __ne__(self, other):
        if not isinstance(other, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        origin = Datum()
        dis1 = origin.distanceFrom(self)
        dis2 = origin.distanceFrom(other)
        # print(dis1)
        # print(dis2)
        if dis1 == dis2:
            return False
        else:
            return True

    def __lt__(self, other):
        if not isinstance(other, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        origin = Datum()
        dis1 = origin.distanceFrom(self)
        dis2 = origin.distanceFrom(other)
        # print(dis1)
        # print(dis2)
        if dis1 < dis2:
            return True
        else:
            return False

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        if not isinstance(other, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        origin = Datum()
        dis1 = origin.distanceFrom(self)
        dis2 = origin.distanceFrom(other)
        # print(dis1)
        # print(dis2)
        if dis1 > dis2:
            return True
        else:
            return False

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)


class Data(collections.UserList):

    def __init__(self, dlist):
        for item in dlist:
            if not isinstance(item, Datum):
                raise TypeError("One of the inputs is not an instance of Datum type!")
        if dlist is None:
            initial = []
        else:
            initial = dlist
        super().__init__(initial)

    def computeBounds(self):
        minDatum = Datum()
        maxDatum = Datum()
        length = 0
        for item in self:
            if len(item) > length:
                length = len(item)
        minlist = [0]*length
        maxlist = [0]*length
        for item in self:
            for index in range(len(item)):
                if item[index] > maxlist[index]:
                    maxlist[index] = item[index]
                if item[index] < minlist[index]:
                    minlist[index] = item[index]
        minDatum._storage = minlist
        maxDatum._storage = maxlist
        return minDatum, maxDatum

    def computeMean(self):
        meanDatum = Datum()
        length = 0
        for item in self:
            if len(item) > length:
                length = len(item)
        sumlist = [0] * length
        for item in self:
            for index in range(len(item)):
                sumlist[index] += item[index]
        meanlist = numpy.array(sumlist)
        meanlist = list(meanlist/length)
        meanDatum._storage = meanlist
        return meanDatum

    def append(self, item: Datum) -> None:
        if not isinstance(item, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        super().append(item)

    def count(self, item: Datum) -> int:
        if not isinstance(item, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        result = super().count(item)
        return result

    def index(self, item: Datum, *args) -> int:
        if not isinstance(item, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        result = super().index(item, *args)
        return result

    def insert(self, i: int, item: Datum) -> None:
        if not isinstance(item, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        super().insert(i,item)

    def remove(self, item: Datum) -> None:
        if not isinstance(item, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        super().remove(item)

    def __setitem__(self, key, value):
        if not isinstance(value, Datum):
            raise TypeError("Input is not an instance of Datum type!")
        super().__setitem__(key, value)

    def extend(self, other) -> None:
        if not isinstance(other, Data):
            raise TypeError("Input is not an instance of Data type!")
        super().extend(other)


class DataClass(enum.Enum):
    Class1 = "Class1"
    Class2 = "Class2"


class DataClassifier:

    def __init__(self, group1, group2):
        if not isinstance(group1, Data):
            raise TypeError("First input is not an instances of Data type!")
        if not isinstance(group2, Data):
            raise TypeError("Second input is not an instances of Data type!")
        if len(group1) == 0:
            raise ValueError("First input empty!")
        if len(group2) == 0:
            raise ValueError("Second input empty!")
        self._class1 = group1
        self._class2 = group2

    def classify(self, item: Datum):
        mean1 = self._class1.computeMean()
        mean2 = self._class2.computeMean()
        dis1 = mean1.distanceFrom(item)
        dis2 = mean2.distanceFrom(item)
        if dis1 <= dis2:
            return DataClass.Class1
        else:
            return DataClass.Class2


if __name__ == "__main__":
    d1 = Datum(1.234, 5.341, 12, 1.007)
    print(d1)

    print()
    print("Test iteration:")
    for v in d1:
        print(v)

    print()
    print("Test neg function:")
    d2 = -d1
    print(d2)
    print(d1)

    print()
    print("Test get item function:")
    print(d2[1])

    print()
    print("Test add function:")
    d3 = Datum(4.512, 6.34, 3.6346)
    d4 = d1+d3
    print(d1)
    print(d3)
    print(d4)
    d4 = d1 + 1.5
    print(d4)

    print()
    print("Test sub function:")
    print(d1)
    d4 = d1-d3
    print(d4)
    d4 = d1 - 1.5
    print(d4)

    print()
    print("Test mul function:")
    d4 = d1 * 2.0
    print(d1)
    print(d4)

    print()
    print("Test div function:")
    d4 = d1 / 1.5
    print(d1)
    print(d4)

    print()
    print("Test eq function:")
    print(d1)
    d5 = d1.clone()
    print(d5)
    print(d1 == d5)

    print()
    print("Test eq function:")
    print(d1)
    print(d3)
    print(d1 == d3)

    print()
    print("Test neq function:")
    print(d1)
    print(d3)
    print(d1 != d3)

    print()
    print("Test lt,le function:")
    print(d1)
    print(d3)
    print(d1 < d3)
    print(d1 <= d3)

    print()
    print("Test gt,ge function:")
    print(d1)
    print(d3)
    print(d1 > d3)
    print(d1 >= d3)

    print()
    print("Test computeBound function:")
    list1 = [d1, d2, d3]
    data1 = Data(list1)
    print(data1.computeBounds())

    print()
    print("Test computeMean function:")
    print(data1.computeMean())

    data2 = Data([d1, d3, d4])
    dc1 = DataClassifier(data1, data2)
    print(dc1.classify(d1))


