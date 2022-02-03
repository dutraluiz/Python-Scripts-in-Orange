# *Scripts python* no *Orange Data Mining*

### 1. Apresentação
O repositório reúne alguns scripts em [`python`](https://www.python.org) para o [Orange Data Mining](https://orangedatamining.com), previamente utilizados no pré-processamento
de dados aerogeofísicos e derivados em estudos preditivos em Geociências.

### 2. Orange Data Mining
O Orange Data Mining [^1] é um software de código aberto baseado no python que não requer conhecimento de programação ou domínio de estatística e matemática.
O software é gratuitamente distribuido em: [orangedatamining.com](https://orangedatamining.com).

### 3. Utilização dos scripts
#### 3.1 Fluxograma
Os scripts são executados no [*widget Python Script*](https://orangedatamining.com/widget-catalog/data/pythonscript/). O banco de dados deve ser carregado em um dos
*widget*: [`File`](https://orangedatamining.com/widget-catalog/data/file/), [`CSV File Import`](https://orangedatamining.com/widget-catalog/data/csvfileimport/),
[`Datasets`](https://orangedatamining.com/widget-catalog/data/datasets/) ou [`SQL Table`](https://orangedatamining.com/widget-catalog/data/sqltable/) e conectado ao *widget Python Script*.
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/76756542/152425299-d7b74c00-a877-4538-9bfb-94a85589a91c.JPG" width="50%" height="50%"></p>

#### 3.2 *Widget Python Script*
A entrada dos códigos no widgets pode ser feito colando ou importando. Para colar um código previamente copiado é necessário clicar no `+` e apertar `CTRL + V` no Windows ou `Command + V` no Mac.
Já para importação,  deve-se clicar em *`More`* > *`Import script from File`* e selecionar o *script* baixado em seu computador.

### 4. *Scripts python*
#### 4.1 Remoção de valores extremos
Os dados radiométricos (*i.e.*, K, eU e Th) comumentemente apresentam valores extremos, sejam muito alto em relação à média e moda ou negativos. A substituição (ou remoção) desses valores podem levar a melhorias significativas no desempenho do algoritmo [^2],[^3]. Assim, o *script*
`Cut-offs` calcula os limites inferior (LI) e superior (LS) e substitui os valores abaixo e acima, respectivamente, conforme sugere Naghetini e Silveira (2021) [^3].


| LI  | LS | Referência | 
| ---- | ---- | ---- |
| μ/10  | P99,5(X)  | Naghetini e Silveira (2021) |

Onde μ é média e P99,5(X)é o percentil 99,5 de um dado radioelemento.

Mais informações sobre essa proposta pode ser consultada na [monografia](http://dx.doi.org/10.13140/RG.2.2.11870.97607) e no [repositório](https://github.com/fnaghetini/Mapa-Preditivo).

#### 4.2 Superamostragem
A superamostragem consiste na geração de dados sintéticos. A técnica envolve a seleção aleatória de um ponto da classe minoritária e de seu vizinho mais próximo. A diferença entre eles é multiplicada por um número aleatório entre 0 e 1, resultando na geração do dado sintético, em outras palavras, um ponto aleatório é escolhido entre um ponto selecionado e seu vizinho [^4].

<div>
<p align="center">
  <img src="https://miro.medium.com/max/1400/1*yRumRhn89acByodBz0H7oA.png" width="50%" height="50%"></p>
</div>
<div>
  <p align="center">
  (Retirado de <a href="https://medium.com/@asheshdas.ds/oversampling-to-remove-class-imbalance-using-smote-94d5648e7d35l">Das, 2019</a>)</p>
</div> 

O *script* gera os dados sintéticos utilizando o algoritmo SVM (*support vector machine*). Esse método foi utilizado por Prado et al. (2020) [^5]. A documentação completa pode ser consultada em [SVM-SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SVMSMOTE.html).
A execução desse *script* requer a instalação do pacote [`imbalanced-learn`](https://imbalanced-learn.org/) no Orange, conforme o tutorial:
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/76756542/152425250-fa166d5b-6650-485d-b462-e27cc5b9d704.png" width="50%" height="50%"></p>


[^1]: Demsar J, Curk T, Erjavec A, Gorup C, Hocevar T, Milutinovic M, Mozina M, Polajnar M, Toplak M, Staric A, Stajdohar M, Umek L, Zagar L, Zbontar J,
Zitnik M, Zupan B (2013) Orange: Data Mining Toolbox in Python, Journal of Machine Learning Research 14(Aug): 2349−2353.

[^2]: Kuhn, M., e Johnson, K., 2013b, Data Pre-processing, in Applied Predictive Modeling, New York, NY, Springer New York, p. 27–59, [doi:10.1007/978-1-4614-6849-3_3](http://dx.doi.org/10.1007/978-1-4614-6849-3_3).

[^3]: Naghetini, F., e Silveira, G., 2021, Utilização de técnicas de Aprendizado de Máquina Supervisionado para mapeamento geológico: um estudo de caso na região de Diamantina, Minas Gerais, Brasil: Universidade Federal de Minas Gerais, 97 p., [doi:10.13140/RG.2.2.11870.97607](http://dx.doi.org/10.13140/RG.2.2.11870.97607).

[^4]: Chawla, N. V., Bowyer, K.W., Hall, L.O., e Kegelmeyer, W.P., 2002, SMOTE: Synthetic Minority Over-sampling Technique: Journal of Artificial Intelligence Research, v. 16, p. 321–357, [doi:10.1613/jair.953](http://dx.doi.org/10.1613/jair.953).

[^5]: Prado, E.M.G., de Souza Filho, C.R., Carranza, E.J.M., e Motta, J.G., 2020, Modeling of Cu-Au prospectivity in the Carajás mineral province (Brazil) through machine learning: Dealing with imbalanced training data: Ore Geology Reviews, v. 124, p. 103611, [doi:10.1016/j.oregeorev.2020.103611](http://dx.doi.org/10.1016/j.oregeorev.2020.103611).
