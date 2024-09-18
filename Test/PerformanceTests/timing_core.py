# run with python3 -m Test.PerformanceTests.timing_core from root dir

import timeit
import sys

sys.path.append("../..")
# sys.path.append("..")

import Test.Model as model

NUMBER_OF_FUNC_CALLS = 100

print("timing calculateSeries")

print(
    "Model:       ",
    min(
        timeit.repeat(
            "calculateSeries(model.E_192,6.28)",
            number=NUMBER_OF_FUNC_CALLS,
            setup="import Test.Model.eseries as model;from Test.Model.core import calculateSeries",
        )
    )
    / NUMBER_OF_FUNC_CALLS
    * pow(10, 9),
    "ns",
)
print(
    "PassiveComp: ",
    min(
        timeit.repeat(
            "calculateSeries(model.E_192,6.28)",
            number=NUMBER_OF_FUNC_CALLS,
            setup="import Test.Model.eseries as model; from PassiveComp.core import calculateSeries",
        )
    )
    / NUMBER_OF_FUNC_CALLS
    * pow(10, 9),
    "ns",
)
