#Store the data about the shares held by the user as 
#tuples containing the following information about shares: 
#share name, cost price, number of shares, selling price. 
# Write a program to determine:
# a.total cost of the portfolio
# b.total amount gained or lost

shares = [("TCS", 1000, 10, 1200), ("INFY", 2000, 5, 2200), ("WIPRO", 500, 20, 600)]
total_cost = 0
total_amount = 0
for share in shares:
    total_cost += share[1] * share[2]
    total_amount += share[3] * share[2]
print("Total cost of the portfolio: ", total_cost)
print("Total amount gained or lost: ", total_amount - total_cost)

#Output: Total cost of the portfolio:  30000
#        Total amount gained or lost:  5000
