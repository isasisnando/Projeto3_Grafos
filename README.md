<h1 align="center">Coloração de Grafos - Projeto 3</h1>

<ul>
    <li><a href="#-autores">💻 Autores</a>
    <li><a href="#-sobre-o-projeto">💬 Sobre o projeto</a></li>
    <li><a href="#-tecnologias">🛠 Tecnologias</a></li>
    <li><a href="#-funcionalidades"> Funcionalidades</a></li>
</ul>

---


<h2>💻 Autores</h2>

<table>
  <tr>
    <td align="center"><a href="https://github.com/isasisnando" target="_blank"><img style="border-radius: 50%;" src="https://github.com/isasisnando.png" width="100px;" alt="Isabela Souza"/><br /><sub><b>Isa Souza</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/lucasdbr05" target="_blank"><img style="border-radius: 50%;" src="https://github.com/lucasdbr05.png" width="100px;" alt="Lucas Lima"/><br /><sub><b>Lucas Lima - 231003406</b></sub></a><br /></td>
</table>

# Setup
Para instalar as dependencias que utilizamos no projeto, é necessário ter o compilador python instalado e o gerenciador de pacotes `pip` que utilizamos para instalar as bibliotecas que nos auxiliaram neste trabalho
```sheel
pip install matplotlib networkx
```
# Run
Executar o seguinte comando no terminal:
```sheel
py main.py
```
ou 
```sheel
python main.py
```


<h2>💬 Sobre o projeto</h2>

<p>
    O projeto consiste em montar um sequência de 14 rodadas de jogos de futebol (com dois turnos com mandos diferentes) em um campeonato onde 7 times competem. Além disso, sabe-se que um time só joga uma partida por rodada e são dadas algumas restrições adicionais descritas abaixo:
    <img  alt="graph" src= "./readme_utils/restricoes.png">
    Para resolver o problema, o campeonato será modelado como um grafo e a sequência será definida com base em um algoritmo de coloração em grafos.
</p>

---
<h2>Solução</h2>

<li>
   O campeonato foi modelado em um grafo, onde os vértices representam as rodadas e as partidas , e as arestas representam uma proibição, ou seja, os dois eventos indicados pelos vértices conectados por uma aresta não podem ocorrer simultaneamente. Assim, adicionaremos as seguintes arestas:

    - Entre todas as rodadas, pois uma rodada não pode ocorrer juntamente com outra.
   
    - Entre duas partidas que compartilham algum time em comum, pois cada time participa de uma partida por vez.
   
    - Entre os vértices que representam as restrições dadas no enunciado do problema, por exemplo adiciona-se uma aresta entre as rodadas 1 e 14 e o jogo (DFC,CFC).
    
    A partir do grafo modelado, iremos realizar uma coloração, onde cada cor representará uma rodada. Dois vértices conectados por uma aresta não ocorrem numa mesma rodada. Para realizar essa coloração foi utilizado um algoritmo recursivo com backtracking, descrito abaixo: 
    
</li>

## Resultados
Modelando o grafo como explicado acima, obtivemos o seguinte modelo:
<img  alt="graph" src= "./readme_utils/grafo_sem_coloração.png">


Após rodar o algoritmo de coloração, que tem as especificações 
---
<h2> Funcionalidades</h2>

<p></p>



