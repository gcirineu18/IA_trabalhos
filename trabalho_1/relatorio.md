
## Relatório - Resolução do 8-Puzzle por Busca em Largura e Busca em Profundidade

### Como executar:
```bash
python3 puzzle8.py BFS 1 2 3 0 4 5 6 8 7
```

- Considera-se o `0` o espaço vazio do jogo.

- Será gerado um arquivo `dfs.txt` ou `bfs.txt` a depender do algoritimo escolhido. Nele vão haver informações como o tempo de execução, o número de nós visitados, o número de ancestrais e a exibição deles (de baixo para cima) até chegar na resolução e o sentido escolhido.
--- 

### Modelagem:

1.  O estado inicial do problema será a entrada inserida no comando, como exemplificada acima;
2. O estado objetivo será quando a sequência de números estiver ordenada em 1 2 3 4 5 6 7 8 0;
3. O conjunto de ações conterá os sentidos ou vizinhança que um nó pode ter. Considera-se então, dado cada situação específica de um índice i, se ele pode seguir para as posições `i + 1`, `i - 1` , `i + 3` ou `i - 3`; 
4. A função sucessora indicará o próximo estado a ser alcançando, que ainda não tenha sido expandido;
5. O teste de objetivo verificará se o estado objetivo foi atingido, a cada novo nó visitado;
6. A representação do nó de busca será a classe **`Node`**, que conterá os atributos `father`, `current_state`, `visited`, `direction`
7. O algoritmo utiliza a estrutura de dados *`Set`* para controlar que cada nó com um dado estado só pode ser armazenado uma vez, e impedir que estados sejam revisitados.

### Análise comparativa

- Observou-se a profundidade do estado objetivo com o BFS é quase sempre menor do que a profundidade obtida pelo DFS, o que é natural, já que é da propriedade do algoritmo DFS encontrar sempre explorar ao máximo a profundidade de um nó. Porém, tanto o consumo de memória quanto o tempo de execução variam muito já que irá depender da posição mais relevante na busca do estado objetivo na árvore, se ela se encontra nos extremos ou mais centralizada.

- Como os pesos das arestas não são relevantes para o problema, a questão de otimalidade não é levada em conta, apenas a estrutura de dado (Pilha ou Fila) escolhida é considerada como distinção principal.
 
O algoritmo executa em tempo `O(V + E)` com o controle de estados visitados, considerando V os vértices (nós), e E as arestas (vizinhos) de cada vértice.

