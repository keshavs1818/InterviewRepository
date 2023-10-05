# You have an array.
# We have a cost of an array as follows: take each pair until the last pair, square the difference of each pair of numbers and add them all up.
# Example: [0, 1, 5, 6, 8]
# (0-1)^2 + (1-5)^2 + (5-6)^2 + (6-8)^2 = 22
# If we add a number in between any two pairs, it needs to be the minimum cost possible.
# Say we add 3 between 1 and 5 or add 7 between 6 and 8.
# We would have (0-1)^2 + (1-3)^2 + (3-5)^2 + (5-6)^2 + (6-8)^2 = 14
import math
def minimumcost(array):
    lst = [(array[i] - array[i + 1]) ** 2 for i in range(len(array) - 1)]
    cost = sum(lst)
    pairs_hash = {}
    for i in range(0, len(array) - 1):
        new_arr = array.copy()
        median = math.floor((new_arr[i] + new_arr[i + 1]) / 4)
        new_arr.insert(i + 1, median)
        new_lst = [(new_arr[i] - new_arr[i + 1]) ** 2 for i in range(len(new_arr) - 1)]
        pairs_hash[(i, i + 1)] = sum(new_lst)
        cost = min(cost, pairs_hash[(i, i + 1)])   
    return cost
print(minimumcost([0, 1, 5, 6, 8]))