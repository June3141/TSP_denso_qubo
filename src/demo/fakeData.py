# -*- coding: utf-8 -*-

import math
from typing import Tuple

import nptyping
import numpy as np


def makeData(citiSize: int) -> Tuple[nptyping.Array[int], nptyping.Array[int]]:
    citiesLocation = np.random.randint(0, 100, (citiSize, 2))
    pathsWeight = [
        [
            [
                math.sqrt(abs(citiesLocation[i, 0] ** 2 - citiesLocation[j, 0] ** 2)),
                math.sqrt(abs(citiesLocation[i, 1] ** 2 - citiesLocation[j, 1] ** 2)),
            ]
            for j in range(citiSize)
        ]
        for i in range(citiSize)
    ]

    pathsWeight = np.array(pathsWeight)

    return citiesLocation, pathsWeight


if __name__ == "__main__":
    citiesLocation, pathsWeight = makeData(3)

    print("==== cities location ==================================")
    print(citiesLocation)

    print("\n==== paths array ==================================")
    print(pathsWeight)
