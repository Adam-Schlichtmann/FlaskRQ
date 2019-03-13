import random
import math


def cocktailSort(items):
    comparisons = 0
    swaps = 0
    top = len(items)
    bottom = 0

    for j in range(0, len(items)):
        swapped = False
        for x in range(bottom, top-1):
            comparisons += 1
            if items[x] > items[x+1]:
                swaps += 1
                items[x], items[x+1] = items [x+1], items[x]
                swapped = True

        top -= 1

        for k in range(top, bottom, -1):
            comparisons += 1
            if items[k] < items[k - 1]:
                swaps += 1
                items[k], items[k - 1] = items[k - 1], items[k]
                swapped = True

        bottom += 1

        if not swapped:
            break
    #print "Comparisons: {} \nSwaps: {}".format(comparisons, swaps)
    return items


def newSort(numbers):
    temp = -11
    swap = False
    while(True):
        swap = False
        for i in range(0,len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swap = True
        if not swap:
            break
    return numbers


def bubbleSort(items):
    comparisons = 0
    swaps = 0
    swapped = False
    top = len(items) - 1
    for j in range(0, len(items)):
        for x in range(0, top):
            comparisons += 1
            if items[x] > items[x+1]:
                swaps += 1
                items[x], items[x+1] = items [x+1], items[x]
                swapped = True
        top -= 1
        if not swapped:
            break
    #print("Comparisons: {} \nSwaps: {}".format(comparisons, swaps))
    return items


def make_list(len_of_list):
    items = []
    for i in range(0, len_of_list):
        items.append(random.randint(0, math.floor(1.5*len_of_list)))
    #print items
    return items