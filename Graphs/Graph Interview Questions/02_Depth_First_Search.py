#!/usr/bin/env python3

graph = {
	'A': set(['B', 'C']),
	'B': set(['A', 'D', 'E']),
	'C': set(['A', 'F']),
	'D': set(['B']),
	'E': set(['B', 'F']),
	'F': set(['C', 'E'])
}

def dfs(graph, start):
	visited = set()
	stack = [start]

	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			print('Visiting vertex: ' + str(vertex))
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)

	return visited

def dfs_recursive(graph, start, visited=None):
	if visited is None:
		visited = set()
	print('Visiting vertex: ' + str(start))
	visited.add(start)
	for nxt in graph[start] - visited:
		dfs_recursive(graph, nxt, visited)
	return visited

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for nxt in graph[vertex] - set(path):
			if nxt == goal:
				yield path + [nxt]
			else:
				stack.append([nxt, path + [nxt]])

print('### Depth-First Search')
print('\n# Standard')
print("dfs(graph, 'A')")
print(dfs(graph, 'A'))
print('\n# Recursive')
print("dfs_recursive(graph, 'A')")
print(dfs_recursive(graph, 'A'))
print('\n# Paths')
print("list(dfs_paths(graph, 'A', 'F'))")
print(list(dfs_paths(graph, 'A', 'F')))