################ Overview of Recursion ################

## Mission 2

search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']

def search(strings, term, index=0):
    if strings[0] == term:
        return index
    if len(strings) <= 1:
        return -1
    return search(strings[1:], term, index=index+1)

apple_index = search(search_list, "apple")
pear_index = search(search_list, "pear")
foo_index = search(search_list, "foo")

## Mission 3

def traverse_list(values):
    return traverse_list(values)

traverse_list([])

## Mission 4

import csv
f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]
    
def summation(values):
    if (len(values)) == 0:
        return 0
    if (len(values)) == 1:
        return values[0]
    
    midpoint = len(values) // 2
    return (summation(values[:midpoint]) + summation(values[midpoint:]))

divide_and_conquer_sum = summation(random_integers)

## Mission 6

f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    
    midpoint = len(unsorted) // 2
    left_list = merge_sort(unsorted[:midpoint])
    right_list = merge_sort(unsorted[midpoint:])
    
    sorted = merge(left_list, right_list)
    return sorted

random_sorted = merge_sort(random_integers)

