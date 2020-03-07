# -*- coding: utf-8 -*-

import pyqubo
from demo.fakeData import makeDemoData
from pyquboSolver.tsp.costHamiltonian import TSPHamiltonian, makeHamiltonian

if __name__ == "__main__":
    cities = 5

    citiesLocation, paths = makeDemoData(citiesSize=cities)

    hamiltonian = TSPHamiltonian(citiesSize=cities, pathsWeight=paths)
    feedDict = {"lamTime": 10.0, "lamVisit": 10.0}

    qubo, offset = hamiltonian.compile().to_qubo(feed_dict=feedDict)
    rawSolution = pyqubo.solve_qubo(qubo)
    decodeSolution, broken, energu = hamiltonian.compile().decode_solution(
        rawSolution, vartype="BINARY", feed_dict=feedDict
    )

    print(decodeSolution)
