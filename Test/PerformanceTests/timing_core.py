# run with python3 -m Test.PerformanceTests.timing_core from root dir

import timeit
import sys

sys.path.append("../..")
# sys.path.append("..")
#

NUMBER_OF_FUNC_CALLS = 100000

print("timing calculateSeries")

print(
    "Model:       ",
    min(
        timeit.repeat(
            "calculateSeries([1.0, 1.5, 2.2, 3.3, 4.7, 6.8],6.28)",
            number=NUMBER_OF_FUNC_CALLS,
            setup="from Test.Model.core import calculateSeries",
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
            "calculateSeries([1.0, 1.5, 2.2, 3.3, 4.7, 6.8],6.28)",
            number=NUMBER_OF_FUNC_CALLS,
            setup="from PassiveComp.core import calculateSeries",
        )
    )
    / NUMBER_OF_FUNC_CALLS
    * pow(10, 9),
    "ns",
)
