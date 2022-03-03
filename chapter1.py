import networkx as nx

## 무방향 그래프
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_edge(1,2)

G.add_nodes_from([3,4,5])
G.add_edges_from([(3,4),(3,5)])


G.nodes()
G.edges()
G.neighbors(3)


for n in G.nodes:
    print(n,G.neighbors(n))

for n in G.nodes:
    print(n, G.neighbors(n))

for u,v in G.edges:
    print(u,v)

## 방향그래프

D = nx.DiGraph()
D.add_edge(1,2)
D.add_edge(2,1)

# 링크추가할 때 노드가 없는 경우 자동으로 노드 추가
D.add_edges_from([(2,3), (3,4)])

D.number_of_edges()
D.number_of_nodes()

## 한 노드의 이웃노드 확인 가능
D.neighbors(2)

# 해당 노드를 향해 연결된 에지와 해당 노드로부터 나가는 에지구분
D.predecessors(2)
D.successors(2)

# 완전이분네트워크
B = nx.complete_bipartite_graph(4,5)

#순환경로
C = nx.cycle_graph(4)

#star
S = nx.star_graph(6)

#경로.. 일직선
P = nx.path_graph(5)

#조밀도 성김도

nx.density(G)

CG = nx.complete_graph(8471)
print(nx.density(CG))


## 서브네트워크
# 클리크 : 노드의 부분집합이 모두 서로 연결된 완전 서브네트워크
#자기주변 네트워크 : 에고네트워크

