import math
import numpy as np


def createSeries(n):
    values = []
    for m in range(0, n):
        k = math.pow(math.pow(10, m), 1 / n)
        # k = math.ceil(k * 100) / 100
        if n <= 24:
            k = round(k, 1)
            match k:
                case 2.6:
                    k = 2.7
                case 2.9:
                    k = 3.0
                case 3.2:
                    k = 3.3
                case 3.5:
                    k = 3.6
                case 3.8:
                    k = 3.9
                case 4.2:
                    k = 4.3
                case 4.6:
                    k = 4.7
                case 8.3:
                    k = 8.2
        else:
            k = round(k, 2)
            if k == 8.3:
                k = 8.2

        values.append(k)
    return values


def norminalizeValue(value):
    factor = 1
    if value >= 10 and value < 100:
        value /= 10
        factor = 10
    elif value >= 100 and value < 1000:
        value /= 100
        factor = 100
    return value, factor


def denorminalizeValue(value, factor):
    return value * factor


def getNextClosestValue(list, value):
    buff = []
    for i in list:
        buff.append(abs(i - value))
    return buff.index(min(buff))


def calculateSeries(list2, value):
    """
    caculates the best combination of values from list to archive value with value = r1 + r2
    returns a touple with length 3. The 2 resistor values and achieved Resistance
    """
    # todo : minimize result matrix, add zero and infinity
    #
    list = np.array(list2)

    # calc (minimized) result matrix
    horizontal = np.tile(list, (list.size, 1))
    vertical = np.transpose(horizontal)

    resultMatrix = np.add(horizontal, vertical)

    # calc error matrix
    targetMatrix = np.full(resultMatrix.shape, value)

    errorMatrix = np.abs(value - targetMatrix)

    # get coordinates of min error
    xCords, yCords = np.where(errorMatrix == errorMatrix.min())
    # first coordinates are enough atm
    x = xCords[0]
    y = yCords[0]

    # translate coordinates to values
    xVal = list[x]
    yVal = list[y]
    resultVal = resultMatrix[x, y]

    # for x in range(xCords.size):
    # print(list[xCords[x]], list[yCords[x]])
    return (xVal, yVal, resultVal)


def calculateParallel(list, value):
    buff = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            total = (list[i] * list[j]) / (list[i] + list[j])
            total = round(total, 1)
            buff.append((list[i], list[j], total))

    out = getNextClosestValue([x[2] for x in buff], value)
    return buff[out]


def calculateError(target, value):
    return ((value - target) / target) * 100
