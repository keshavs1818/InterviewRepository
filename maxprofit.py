# You have a prices array and a profits array. 
# If we have prices = [0, 6, 7, 8, 9] and profits = [45, 67, 38, 29, 90], we need to find three indexes in prices such that i < j < k and also that price[i] < price[j] < price[k], and using that,
# find the sum of profits corresponding to those indices. Find the maximum profit.
# Example: prices = [0, 6, 7, 9, 8] profits = [45, 67, 38, 29, 90]
# (0, 1, 2) (1, 2, 3) (0, 1, 3) (0, 1, 4) (1, 2, 4)
# profits_with_conditions = [150, 141, 202, 134, 195]
# Answer: 202
def maxprofit(price, profit):
    maximum = -1
    for i in range(0, len(price) - 2):
       for j in range(i + 1, len(price) - 1): 
           for k in range(j + 1, len(price)):
               if price[i] < price[j] < price[k]:
                   maximum = max(maximum, profit[i] + profit[j] + profit[k])
    return maximum
print(maxprofit([0, 6, 7, 9, 8], [45, 67, 38, 29, 90]))