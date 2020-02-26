## Reconhecer ovos de mosquito da dengue

Instalar dependencia:  
`pip install numpy`

Executar Open Cv na [imagem.png](./img/imagem.png), criando uma outra imagem com a quantidade e com quadrado verde:  
`python openCvCascade`

Pode ser adicionado:
- [ ] Transformar em uma função com parametros como "versao cascade, caminho da imagem, saida e entrada e etc"
- [ ] Transformar openCvCascade em um objeto para ser importado em outro projeto, ex: Web

### Melhores Resultados até o momento

1 - V0.1.1 (3- "" 4- "-w 18 -h 18" 5- "-w 18 -h 18")
2 - V0.1.4 (3- "" 4- "-w 15 -h 15" 5- "-w 15 -h 15")
3 - V0.1.6 (3- "-num 3000" 4- "-num 3000" 5 - "-numPos 2000 -numNeg 3200 -numStages 10")
4 - V0.1.2 (3- "" 4- "-w 20 -h 20" 5- "-w 20 -h 20")
5 - V0.1.3 (3- "-w 48 -h 48" 4- "-w 20 -h 20" 5- "-w 20 -h 20")
6 - V0.1.5 (3- "-num 3000" 4- "-num 3000" 5 - "-numPos 2500 -numNeg 3200 -numStages 15")

