# PROJETO PYTHON: Gráfico de Faturamento da Loja

> Um sistema simples que gera um gráfico.

  O projeto tem como objetivo, gerar um gráfico com base nos dados já pré estabelecidos entre as lojas citadas
e quais faturamentos foram obtidos no final do ano de 2019 (Valores Hipotéticos)

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3_**

# Exemplo de Uso

### Classe:
```
class Grafico:
    def __init__(self):
        # Linha X
        self.lojas = ['Loja A', 'Loja B', 'Loja C',
                      'Loja D', 'Loja E', 'Loja F']
        # Linha y
        self.valores = [120000, 150000, 145500,
                        120500, 134400, 119880]
```
![Valores do Gráfico](https://github.com/ThiagoLozano/Grafico-de-Faturamento-da-Loja/blob/master/Screenshot/Classe.PNG)

![Gráfico](https://github.com/ThiagoLozano/Grafico-de-Faturamento-da-Loja/blob/master/Screenshot/gr%C3%A1fico.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada.

```
import matplotlib.pyplot as plt
```
![Biblioteca](https://github.com/ThiagoLozano/Grafico-de-Faturamento-da-Loja/blob/master/Screenshot/Biblioteca.PNG)


### Referências.
* https://github.com/pythonizando
* https://www.alura.com.br/artigos/criando-graficos-no-python-com-a-matplotlib
