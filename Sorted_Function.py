sales_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

# sales_prices.sort()
# print(sales_prices)
# [1, 3, 10, 40, 83, 100, 100, 220, 400]

# sorted_list = sales_prices.sort()
# print(sorted_list)
# None

# sorted_list = sorted(sales_prices)
# print(sorted_list)
# print(sales_prices)
# [1, 3, 10, 40, 83, 100, 100, 220, 400]
# [100, 83, 220, 40, 100, 400, 10, 1, 3]


sorted_list = sorted(sales_prices, reverse=True)
print(sorted_list)
# [400, 220, 100, 100, 83, 40, 10, 3, 1]