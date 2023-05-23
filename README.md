# Classes-em-Python-2

Programa em Python com a utilização de classes que funciona como um painel de informações de um elevador.
Sendo possível a movimentação deste em um prédio e a entrada e saída de pessoas do mesmo.

Objetivo do código:

Criar uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = O),
total de andares no prédio, excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele. A classe deve receber como parâmetros no método
construtor a capacidade do elevador e o total de andares no prédio.
OBS: os elevadores sempre começam no térreo e vazio

A classe deve também disponibilizar os seguintes métodos:

* Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
* Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
* Sobe: para subir um andar (não deve subir se já estiver no último andar);
* Desce: para descer um andar (não deve descer se já estiver no térreo);
* Encapsular todos os atributos da classe (criar os métodos set e get).
