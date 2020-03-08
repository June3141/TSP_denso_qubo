# -*- cofing utf-8 -*-
import itertools
import sys
from typing import Dict, List, Tuple

import nptyping
import numpy as np


def pathsDictChecker(citiesSize: int, pathsWeight: Dict[Tuple[int, int], int]) -> bool:
    correctCombinations = int(citiesSize * (citiesSize - 1) / 2)

    if len(pathsWeight) == correctCombinations:
        return True

    else:
        print(
            """
            There is something wrong!
            Cities: {0}
            Correct number of combinations: {1}
            Dictionary length: {2}
        """.format(
                citiesSize, correctCombinations, len(pathsWeight)
            )
        )
        return False


def distanceCosts(citiesSize: int, pathsWeight: dict) -> nptyping.Array[int]:

    if pathsDictChecker(citiesSize, pathsWeight):
        pass
    else:
        sys.exit()

    pathsWeightArray: nptyping.Array[int] = pathsWeightMatrix(citiesSize, pathsWeight)

    quboSize: int = citiesSize ** 2
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

        if (rowIK > columnJL) and (i > j):
            continue

        # first place
        if l == 0 and (k == 1 or k == citiesSize - 1):
            quboMatrix[rowIK, columnJL] += pathsWeightArray[j, i]

        # last place
        elif l == (citiesSize - 1) and (k == citiesSize - 2 or k == 0):
            quboMatrix[rowIK, columnJL] += pathsWeightArray[j, i]

        # others
        elif k == l - 1 or k == l + 1:
            quboMatrix[rowIK, columnJL] += pathsWeightArray[j, i]

    return quboMatrix


def pathsWeightMatrix(citiesSize: int, pathsWeight: Dict[Tuple[int, int], int]) -> nptyping.Array[int]:
    indices: List[Tuple[int, ...]] = list(itertools.combinations(range(citiesSize), 2))

    pathsWeightArray: nptyping.Array[int] = np.zeros((citiesSize, citiesSize), dtype=int)

    for t in range(len(indices)):
        (i, j) = indices[t]
        weightIJ: int = pathsWeight[(i, j)]

        pathsWeightArray[i, j] = weightIJ
        pathsWeightArray[j, i] = weightIJ

    return pathsWeightArray


def costs(citiesSize: int, pathsWeight: dict) -> nptyping.Array[int]:
    return distanceCosts(citiesSize, pathsWeight)


if __name__ == "__main__":
    cities = 4
    pathsDict = {
        (0, 1): 1,
        (1, 2): 2,
        (2, 3): 3,
        (0, 3): 4,
        (0, 2): 5,
        (1, 3): 6,
    }

    print(costs(cities, pathsDict))
