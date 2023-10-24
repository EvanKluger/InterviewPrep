

def activity_sel(start, end):
    activities = []
    
    for i in range(len(start)):
        activities.append([start[i],end[i]])
    
    activities.sort(key=lambda x: x[1])

    best_plan = [activities[0]]

    for i in range(len(activities)):
        if activities[i][0] >= best_plan[-1][1]:
            best_plan.append(activities[i])
    
    return best_plan


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print(activity_sel(start, finish))
# Expected output: [(1, 2), (3, 4), (5, 7), (8, 9)]

start2 = [1, 3, 5, 5, 6]
finish2 = [2, 4, 6, 7, 8]

print(activity_sel(start2, finish2))
# Expected output: [(1, 2), (3, 4), (5, 6), (6, 8)]
