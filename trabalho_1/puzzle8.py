import sys
import time

expected_output = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
sys.setrecursionlimit(90000)
class Node:
    def __init__(self, father = None, current_state = None, visited = False, direction = None, depth = None):
        self.father = father
        self.current_state = current_state
        self.visited = visited
        self.direction = direction
        self.depth = depth
        
    def get_index(self):  
        return self.current_state.index("0")
    
    def catch_neiboughrs(self):
        if self.current_state  == None:
            return []
        index = self.current_state.index("0")

        if index == 0:
            return [1, 3]
        elif index == 1:
            return [0, 2, 4]
        elif index == 2:
            return [1, 5]
        elif index == 3:
            return [0, 4, 6]
        elif index == 4:
            return [1, 3, 5, 7]
        elif index == 5:
            return [2, 4, 8]
        elif index == 6:
            return [3, 7] 
        elif index == 7:
            return [4, 6, 8]
        elif index == 8:
            return [5, 7]  

    def show_pretty_matrix(self):
        count = 0
        for _ in range(3):
            arquivo.write("|")             
            for j in range(3):
                if j == 2:
                    arquivo.write(f"{self.current_state[j+count]}") 
                else:
                    arquivo.write(f"{self.current_state[j+count]} ")                    
            arquivo.write("|\n")     
            count += 3

    def get_direction(self, current, next, number):
        if current > next:
            if current - next == 1:
                self.direction = f"{number} para esquerda"
            else:
                self.direction = f"{number} para cima"
        else:
            if next - current == 1:
                self.direction = f"{number} para direita"
            else:
                self.direction = f"{number} para baixo"               

        
def has_solution(list):
    count = 0
    for i in range(len(list)-1):
        if list[i] == "0":
            continue
        for j in range(i+1,len(list)):
            if list[j] == "0":
                continue
            if list[i] > list[j]:
                count += 1  
    return [count%2 == 0, count]            

algorithm = sys.argv[1]

if algorithm == "BFS":
    file_name = 'bfs.txt'
else:
    file_name = 'dfs.txt'    

with open(file_name, 'w', encoding='utf-8') as arquivo:
    inicio = time.time()

    current_state = list(sys.argv[2:])

    visited_states = set()
    nodes_list = []
    initial_node = Node(None, current_state, True, None, 0)
    nodes_list.append(initial_node)

    has_solution, count = has_solution(current_state)

    arquivo.write(f"Tem solução? {has_solution}, paridade? {count}\n")

    if(has_solution is False):
        exit()


    visited_states.add(tuple(current_state))
    count_visits = 0
    while(len(nodes_list) != 0):
        if algorithm == "BFS":
            node = nodes_list.pop(0)  
        else:
            node = nodes_list.pop()    

        if node.current_state == expected_output:
            arquivo.write("Sucesso.\n")
            break
        
        index = node.get_index()
        len_neighbours = len(node.catch_neiboughrs())
        neighbours = node.catch_neiboughrs()

        for i in range(len_neighbours):   

            new_state = node.current_state.copy()
            new_state[neighbours[i]], new_state[index] = new_state[index], new_state[neighbours[i]]


            state_tuple = tuple(new_state)

            if state_tuple not in visited_states:
                count_visits += 1
                visited_states.add(state_tuple)
                newNode = Node(node,new_state, True, None, node.depth + 1)
                nodes_list.append(newNode)

                newNode.get_direction(neighbours[i], index, new_state[index])
               
        
    count = 0   
    arquivo.write("\n")     
    while(node):
        arquivo.write(f"Profundidade: {node.depth}\n") 
        node.show_pretty_matrix()

        arquivo.write("\n")
        arquivo.write(f"Sentido: {node.direction}\n")   
        
        node = node.father
        count+=1
    arquivo.write(f"Número de ancestrais: {count - 1}\n")  
    arquivo.write(f"Visitas totais: {count_visits}\n")

    fim = time.time()
    arquivo.write(f"Tempo total de execução: {fim - inicio} segundos")





