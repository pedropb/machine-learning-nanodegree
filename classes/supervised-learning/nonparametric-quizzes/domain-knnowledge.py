import math

def manhattan_distance(p1, p2):
    return abs((p2[0] - p1[0])) + abs((p2[1] - p1[1]))

def euclidean_distance(p1, p2):
    return math.sqrt(pow((p2[0] - p1[0]),2) + pow((p2[1] - p1[1]),2))

def compute_average(n_neighbors, distances, distance_idx):
    sum = 0
    i = 0
    while i < n_neighbors:
        cur = distances[i][2]
        sum += cur
        while distances[i+1][distance_idx] == distances[i][distance_idx] and i+1 < len(distances):
            sum += distances[i+1][2]
            i += 1
        i += 1
    return float(sum) / i 

data = [(1,6,7), (2,4,8), (3,7,16), (6,8,44), (7,1,50), (8,4,68)]
query = (4,2)

distances = []
for p in data:
    distances.append((euclidean_distance(p, query), manhattan_distance(p, query), p[2])) 

# sort by euclidean_distance
euclidean = sorted(distances, key=lambda d: d[0])
print "euclidean 1: ", compute_average(1, euclidean, 0)
print "euclidean 3: ", compute_average(3, euclidean, 0)

manhattan = sorted(distances, key=lambda d: d[1])
print "manhattan 1: ", compute_average(1, manhattan, 1)
print "manhattan 3: ", compute_average(3, manhattan, 1)
