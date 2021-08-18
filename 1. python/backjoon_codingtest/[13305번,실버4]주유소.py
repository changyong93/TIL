inputs = iter([
    ["4", "2 3 1", "5 2 4 1"], #18,0
    ["4", "3 3 4", "1 1 1 1"], #10,1
    ][0])

num_of_cities = int(next(inputs))
dist_bw_cities = list(map(int,next(inputs).split()))
oil_prices = list(map(int,next(inputs).split()))

# num_of_cities = int(input())
# dist_bw_cities = list(map(int,input().split()))
# oil_prices = list(map(int,input().split()))

total_cost = oil_prices[0] * dist_bw_cities[0]
oil_price = oil_prices[0]
for i in range(1, num_of_cities-1):
    if oil_prices[i] < oil_price:
        oil_price = oil_prices[i]
    total_cost += oil_price*dist_bw_cities[i]
print(total_cost)    

