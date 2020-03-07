# -*- coding: utf-8 -*-

import os
from typing import List

import matplotlib.pyplot as plt
import nptyping
import numpy as np


def plotMap(citiesLocation: nptyping.Array, orderList: List[int]) -> None:
    citiesSize = len(citiesLocation)

    citiesX = [citiesLocation[i, 0] for i in range(citiesSize)]
    citiesY = [citiesLocation[i, 1] for i in range(citiesSize)]

    rootLineX = [citiesLocation[orderList[i], 0] for i in range(citiesSize)]
    rootLineX.append(citiesLocation[orderList[0], 0])

    rootLineY = [citiesLocation[orderList[i], 1] for i in range(citiesSize)]
    rootLineY.append(citiesLocation[orderList[0], 1])

    plt.scatter(citiesX, citiesY, s=120)
    plt.plot(rootLineX, rootLineY, marker=None)

    plt.title("Traveling saleseman problem")

    plt.xlabel("x axis")
    plt.xlim([0, 100])

    plt.ylabel("y axis")
    plt.ylim([0, 100])

    plt.grid(True)

    plt.savefig("{0}/images/tmp/tsp.png".format(os.getcwd()))
    plt.close()


if __name__ == "__main__":
    demoSize = 10
    demoData = np.random.randint(0, 100, (demoSize, 2))
    demoOrder = [i for i in range(demoSize)]

    plotMap(demoData, demoOrder)
