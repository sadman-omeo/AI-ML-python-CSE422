import heapq

input_text = open("Input file.txt", 'r')
output_text = open('Output file.txt', 'w')

graph = {}
hue = {}
visit = {}
parent = {}
dist = {}

for i in range(20):
    line = input_text.readline().split()
    hue[line[0]] = line[1]
    neigh = []
    
    for j in range(2, len(line) - 1, 2):
        neigh.append((line[j], line[j + 1]))
    
    graph[line[0]] = neigh
    parent[line[0]] = None
    visit[line[0]] = False

for node in graph:
    dist[node] = float('inf')

prio_q = []
heapq.heapify(prio_q)



def A_star(graph, hue, start, end):
    heapq.heappush(prio_q, [hue[start], 0, start])
    dist[start] = 0
    
    while True:
        trd = heapq.heappop(prio_q)
        h, curr_cost, curr_node = trd
        visit[curr_node] = True
        if curr_node == end:
            break
        
        for i, j in graph[curr_node]:
            if visit[i] != True:
                new_cost = curr_cost + int(j)
                if new_cost < dist[i]:
                    dist[i] = new_cost
                    heapq.heappush(prio_q, [new_cost + int(hue[i]), new_cost, i])
                    parent[i] = curr_node
                    
    
    
#Driver
start = 'Arad'
end = 'Bucharest'
curr = end
A_star(graph, hue, start, end)
path = []
while curr != None:
    path.append(curr)
    curr = parent[curr]

path.reverse()

if dist[end] == float('inf'):
    output_text.write(f"No path found!")
else:
    output_text.write(' --> '.join(map(str, path)))
    output_text.write(f"\nTotal Distance: {dist[end]} km.")
