# -*- coding: utf-8 -*-

import math
from typing import Tuple

import nptyping
import numpy as np


def makeDemoData(citiesSize: int) -> Tuple[nptyping.NDArray[int], nptyping.NDArray[int]]:
    citiesLocation = np.random.randint(0, 100, (citiesSize, 2))
    pathsWeight = [
        [
            math.sqrt(
                (citiesLocation[i, 0] - citiesLocation[j, 0]) ** 2 + (citiesLocation[i, 1] - citiesLocation[j, 1]) ** 2
            )
            for j in range(citiesSize)
        ]
        for i in range(citiesSize)
    ]

    pathsWeight = np.array(pathsWeight)

    return citiesLocation, pathsWeight


if __name__ == "__main__":
    citiesLocation, pathsWeight = makeDemoData(3)

    print("==== cities location ==================================")
    print(citiesLocation)

    print("\n==== paths array ==================================")
    print(pathsWeight)
