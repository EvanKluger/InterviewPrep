def knapsack_greedy(items, capacity):
    #items -> [(value, weight)]
    density_items = []
    curr_weight = 0
    value = 0
    count = 0
    for item in items:
        density_items.append((item[0]/item[1], count))
        count += 1
    
    density_items.sort(reverse=True, key=lambda x: x[0])
    
    for density, index in density_items:
        item_value, item_weight = items[index]
        
        if curr_weight + item_weight <= capacity:
            curr_weight += item_weight
            value += item_value
        else:
            remaining_capacity = capacity - curr_weight
            fraction = remaining_capacity / item_weight
            value += item_value * fraction
            break
    
    return value

        
        
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

print(knapsack_greedy(items, capacity))

items = [(40, 5), (100, 20), (70, 10)]
capacity = 25
print(knapsack_greedy(items, capacity))  
