def tower_of_hanoi(n, source, auxiliary, destination):
    
    if n == 1:
        destination.append(source.pop())
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary)

    destination.append(source.pop())

    tower_of_hanoi(n-1, auxiliary, source, destination)

def setup_and_solve(n):
    source = [i for i in range(n, 0, -1)]
    auxiliary = []
    destination = []
    tower_of_hanoi(n, source, auxiliary, destination)
    return source, auxiliary, destination

source, auxiliary, destination = setup_and_solve(15)
print("Source:", source)
print("Auxiliary:", auxiliary)
print("Destination:", destination)