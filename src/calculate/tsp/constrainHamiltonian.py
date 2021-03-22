# -*- cofing utf-8 -*-
import nptyping
import numpy as np


def visitingConstrain(citiesSize: int) -> nptyping.NDArray[int]:
    quboSize = citiesSize ** 2
    quboMatrix = np.zeros((quboSize, quboSize), dtype=int)

    indices = [
        [i, j, k, l]
        for i in range(citiesSize)
        for j in range(citiesSize)
        for k in range(citiesSize)
        for l in range(citiesSize)
    ]
    for i, j, k, l in indices:
        rowIK = i * citiesSize + k
        columnJL = j * citiesSize + l

        if rowIK > columnJL:
            continue

        if rowIK == columnJL:
            quboMatrix[rowIK][columnJL] -= 1
        if i == j and k != l:
            quboMatrix[rowIK][columnJL] += 1
        if i < j and k == l:
            quboMatrix[rowIK][columnJL] += 1

    return quboMatrix


def oneUnitConstrain(citiesSize: int) -> nptyping.NDArray[int]:
    quboSize = citiesSize ** 2
    quboMatrix = np.zeros((quboSize, quboSize), dtype=int)

    indices = [
        [i, j, k, l]
        for i in range(citiesSize)
        for j in range(citiesSize)
        for k in range(citiesSize)
        for l in range(citiesSize)
    ]
    for i, j, k, l in indices:
        rowIK = i * citiesSize + k
        columnJL = j * citiesSize + l

        if rowIK > columnJL:
            continue

        if rowIK == columnJL:
            quboMatrix[rowIK][columnJL] -= 1
        if i == j and k != l:
            quboMatrix[rowIK][columnJL] += 1
        if i < j and k == l:
            quboMatrix[rowIK][columnJL] += 1

    return quboMatrix


def constrains(citiesSize: int) -> nptyping.NDArray[int]:
    return visitingConstrain(citiesSize) + oneUnitConstrain(citiesSize)


if __name__ == "__main__":
    print(constrains(3))
