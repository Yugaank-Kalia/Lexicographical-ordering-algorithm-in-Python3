# importing dependencies

import math


def swap(array, i, j):

    array[i], array[j] = array[j], array[i]


# global variables

total = list()


def getvalue():
    arr = []
    while True:
        i = input("Enter q to exit : ")
        if(i != 'q'):
            arr.append(int(i))
        else:
            break
    return (arr)


def permutations():

    value = getvalue()
    for z in range(math.factorial(len(value))):
        total.append(value)

        for k in range(math.factorial(len(value))):
            largestX = -1

            for i in range(len(value) - 1):
                if (value[i] < value[i + 1]):
                    largestX = i

            largestY = -1

            for j in range(len(value)):

                if (value[largestX] < value[j]):

                    largestY = j

            swap(value, largestX, largestY)

            endArray = value[largestX + 1:]

            value = value[:largestX + 1]

            endArray.reverse()

            value.extend(endArray)

    return (total)


print(permutations())
