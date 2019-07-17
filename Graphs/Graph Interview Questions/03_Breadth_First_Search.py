#!/usr/bin/env python3

graph = {
	'A': set(['B', 'C']),
	'B': set(['A', 'D', 'E']),
	'C': set(['A', 'F']),
	'D': set(['B']),
	'E': set(['B', 'F']),
	'F': set(['C', 'E'])
}

def bfs(graph, start):
	visited = set()
	queue = [start]

	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			print('Visiting vertex: ' + str(vertex))
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)

	return visited

def bfs_paths(graph, start, goal):
	queue = [(start, [start])]
	while queue:
		(vertex, path) = queue.pop(0)
		for nxt in graph[vertex] - set(path):
			if nxt == goal:
				yield path + [nxt]
			else:
				queue.append([nxt, path + [nxt]])


print('### Breadth-First Search')
print('\n# Standard')
print("bfs(graph, 'A')")
print(bfs(graph, 'A'))
print('\n# Paths')
print("list(bfs_paths(graph, 'A', 'F'))")
print(list(bfs_paths(graph, 'A', 'F')))