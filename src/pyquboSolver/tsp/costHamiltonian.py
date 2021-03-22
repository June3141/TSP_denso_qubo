# -*- coding: utf-8 -*-
import sys

import nptyping
import pyqubo


def pathsWeightChecker(citiesSize: int, pathsWeight: nptyping.NDArray[int]) -> bool:

    if len(pathsWeight) == citiesSize and len(pathsWeight[0]) == citiesSize:
        return True

    else:
        print(
            """
            There is something wrong!
            Cities: {0}
            Correct Array Size: {0} x {0}
            Passed Array Size: {1} x {2}
        """.format(
                citiesSize, len(pathsWeight), len(pathsWeight[0])
            )
        )
        return False


def TSPHamiltonian(citiesSize: int, pathsWeight: nptyping.NDArray[int]):

    if pathsWeightChecker(citiesSize, pathsWeight):
        pass
    else:
        sys.exit()

    timeSteps = citiesSize
    x = pyqubo.Array.create("x", (citiesSize - 1, citiesSize - 1), "BINARY")

    # goal -> start
    costHamiltonian = pyqubo.Sum(0, citiesSize - 1, lambda start: pathsWeight[citiesSize - 1, start] * x[start][0])

    # on the way
    costHamiltonian += pyqubo.Sum(
        0,
        timeSteps - 2,
        lambda time: pyqubo.Sum(
            0,
            citiesSize - 2,
            lambda i: pyqubo.Sum(i + 1, citiesSize - 1, lambda j: pathsWeight[i, j] * x[i][time] * x[j][time + 1]),
        ),
    )

    # on the way -> goal
    costHamiltonian += pyqubo.Sum(0, citiesSize - 1, lambda j: pathsWeight[j, citiesSize - 1] * x[j][timeSteps - 2])

    ## Constrain
    timeConstrain = pyqubo.Constraint(
        pyqubo.Sum(0, timeSteps - 1, lambda time: (pyqubo.Sum(0, citiesSize - 1, lambda i: x[i][time]) - 1) ** 2),
        label="time",
    )
    visitConstrain = pyqubo.Constraint(
        pyqubo.Sum(0, citiesSize - 1, lambda i: (pyqubo.Sum(0, timeSteps - 1, lambda time: x[i][time]) - 1) ** 2),
        label="city",
    )

    hamiltonian = (
        costHamiltonian
        + pyqubo.Placeholder("lamTime") * timeConstrain
        + pyqubo.Placeholder("lamVisit") * visitConstrain
    )

    return hamiltonian


def makeHamiltonian(citiesSize: int, pathsWeight: nptyping.NDArray[int]):
    costFunction = TSPHamiltonian(citiesSize, pathsWeight)

    return costFunction.compile()


if __name__ == "__main__":
    pass
