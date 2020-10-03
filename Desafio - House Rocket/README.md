> Disclaimer: o contexto a seguir é completamente fictício, a empresa, o CEO, as perguntas de negócio existem somente no imaginário humano.

[notebook.](https://nbviewer.jupyter.org/github/pauloreis-ds/Projetos/blob/master/Desafio%20-%20House%20Rocket/notebooks/House%20Rocket%20%28HR%29.ipynb)


<p align="center">
  <img src="images/Imagem1.jpg" width="450" />
</p>


## Contexto.
A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia.

O CEO da House Rocket gostaria de maximizar a receita da companhia encontrando boas oportunidades de negócio.<br>
E como Data Scientist contratado pela empresa para ajudar a encontrar as melhores oportunidades no mercado de <br>
imóveis, criar este projeto é a proposta de solução.

A principal estratégia da corporação é comprar boas casas em ótimas localizações com preços baixos e depois<br>
revendê-las a preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa<br>
e portanto maior sua receita.

Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores<br>
e a localização e o período do ano também podem influenciar os preços, o que dificulta uma abordagem de análise <br>
"manual" (sem o uso das ferramentas da Ciência de Dados).

Portanto, as questões a serem respondidas são:

    Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
    
    A House Rocket deveria fazer uma reforma para aumentar o preço da venda?
    
    Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?

O [conjunto de dados](https://www.kaggle.com/harlfoxem/housesalesprediction) que representa o contexto está disponível na plataforma do Kaggle e contém casas vendidas entre Maio de 2014 e Maio de 2015.

---
    
    Sumário:
        1 - Análise exploratória.
        2 - Modelagem.
        3 - Resultados.
        4 - Melhorias. O que faria diferente?
        5 - Sumário dos notebooks.
            Resources

## 1 - Análise exploratória.
Uma breve exploração mostrou que uma abordagem investigativa auxiliaria na resposta da primeira pergunta (através de conhecimento da área para definir quais casas buscar). E ao levantar hipóteses sobre como prodecer para encontrar os imóveis ideais para compra, ter essas hipóteses derrubadas e examinar novamente, foi possível decifrar o enigma e chegar a uma conclusão.

## 2 - Modelagem.
Para as outras perguntas, preprocessei os dados e utilizei um modelo para estimar os preços das casas e então lapidar soluções a partir dele. 


## 3 - Resultados.
No fim, temos **listas com:**

- _34 casas que não necessitam de reforma e estão localizadas em bairros que tendem a valorizar no decorrer do tempo._

- _62 casas que também não necessitam de reforma e que podem valorizar._

- _156 casas que ao serem reformadas tendem a trazer grande retorno por já estarem locais valorizados._

- _51 casas que ao serem reformadas podem trazer bons retornos._

E seus respectivos preços. Além disso, sim, há indícios de que uma reforma contribua para elevar o valor de venda (aumentando os lucros). 
 
 
<p align="center">
  <img src="images/luxuosas e indicações.png" width="650" />
</p> 
 
 
> ps: os resultados mostrados são arrendondados (sempre para baixo... fica mais fácil de pronunciar :) kkkkkk ).

Em mudanças mais particulares e específicas o ideal seria focar no **design** _['grade']_ e na **vista** _['view']_ . Pois são os que mais incrementam o valor da casa, em aproximadamente **75 mil** (olhando por uma estimativa média _"mínima"_ , explicação em detalhes ao fim do [notebook](https://nbviewer.jupyter.org/github/pauloreis-ds/Projetos/blob/master/Desafio%20-%20House%20Rocket/notebooks/House%20Rocket%20%28HR%29.ipynb)).

Já em alterações que afetam múltiplas áreas, podemos olhar para o conjunto [condition, grade e view], aplicando reformas que atingam tanto a **condição** quanto o **design** e a **vista** da casa, por apresentar acréscimos de em média **165 mil dólares**.

> Mais opções são apresentadas na explicação no fim do notebook e para não extender a leitura aqui as manterei lá.


<p align="center">
  <img src="images/renovated and grade.JPG" width="650" />
</p> 


## 4 - Melhorias. O que faria diferente?

1 - Execução de cada ciclo de maneira mais aprofundada. Para esse projeto pensei e agi de modo a criar uma solução simples e rápida, o próximo passo natural seria trabalhar em cima de melhorias focando nos detalhes que deixei passar. Por exemplo, desenvolvendo mais a análise, limpeza e feature engineering.

### 5 - Sumário do notebook

        1 - Visão geral (uma breve exploração)
        2 - Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?
            2.1 Opções de "Como prodecer?"
            2.2 Análise da 1ª filtragem
            2.3 Procedimentos avançados
            2.4 Solução (parte 1)
            2.5 Casas para reformar
                2.5.1 Ganhando $$ nos locais de luxo
                2.5.2 Solução (parte 2)
            2.6 "Reutilizando a separação de bairros da solução 1"
                2.6.1 Solução (parte 3)
        3 - A House Rocket deveria fazer uma reforma para aumentar o preço da venda?
            3.1 Análise de dados simples
            3.2 Testando correlações
            3.3 Feature Engineering
            3.4 Solução      
        4 - Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?
            4.1 Testando nas casas recomendadas.
            4.2 Mudanças
                4.2.1 Isoladas
                4.2.2 renovated e condition
                4.2.3 renovated, condition e grade
                4.2.4 renovated, condition, grade e view
                4.2.5 renovated, condition e view
                4.2.6 view e grade
                4.2.7 renovated e grade
                4.2.8 renovated e view
                4.2.9 renovated, view e grade
            4.3 Solução
            
            
**Resources:**

    Python 3.7
    Packages: pandas, matplotlib, seaborn,
              numpy, statsmodels, sklearn.
              
              
              
<p align="center">
  <img src="images/Locais luxuosos.png" width="650" />
</p> 

 
[<img align="right" width="60" height="60" src="https://github.com/pauloreis-ds/Paulo-Reis-Data-Science/blob/master/Paulo%20Reis/Pauloreis01.png">](https://github.com/pauloreis-ds)

---
