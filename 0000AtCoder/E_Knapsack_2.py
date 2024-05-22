# take inputs
items, knapsack_capacity = map(int, input().split())
weights, values = [0]*items, [0]*items
for i in range(items):
    item_weight, item_value = map(int, input().split())
    weights[i] = item_weight
    values[i] = item_value
# end of taking inputs

if items == 1:
    if weights[0] > knapsack_capacity:
        print(0)
    else:
        print(values[0])
        
else:
    last_index = [0]*(knapsack_capacity+1)

    for remaining_capacity in range(weights[0], knapsack_capacity+1):
        last_index[remaining_capacity] = values[0]

    current_index = last_index[:]

    for index in range(1, items):
        for remaining_capacity in range(knapsack_capacity+1):
            not_take = last_index[remaining_capacity]
            take = -float('inf')

            if remaining_capacity >= weights[index]:
                new_capacity = remaining_capacity-weights[index]
                take = values[index] + last_index[new_capacity]

            current_index[remaining_capacity] = max(take, not_take)
        last_index = current_index[:]

    print(last_index[knapsack_capacity])
