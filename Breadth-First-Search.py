 # Input Graph
graph = {
'A' : ['B','C'],
'B' : ['A','C','D'],
'C' : ['A','B','E'],
'D' : ['B','E'],
'E' : ['C','D']
}
# To store visited nodes.
visitedNodes = []
# To store nodes in queue
queueNodes = [] 
# function
def bfs(visitedNodes, graph, snode):
	visitedNodes.append(snode)
	queueNodes.append(snode)
	print()
	print("RESULT :")
	while queueNodes:
		s = queueNodes.pop(0)
		print (s, end = " ")
		for neighbour in graph[s]:
			if neighbour not in visitedNodes:
				visitedNodes.append(neighbour)
				queueNodes.append(neighbour)
		
# Main Code
snode = input("Enter Starting Node(A, B, C, D, or E) :").upper()
# calling bfs function
bfs(visitedNodes, graph, snode)











### OUTPUT ###

# Sample Output 1:
# -------------------
# Enter Starting Node(A, B, C, D, or E) :A

# RESULT :
# A B C D E
# ------------------------------------------------------------------
# Sample Output 2:
# -------------------
# Enter Starting Node(A, B, C, D, or E) :B

# RESULT :
# B A C D E