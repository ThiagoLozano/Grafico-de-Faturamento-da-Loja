# PROJETO PYTHON: Gráfico de Faturamento da Loja

> Um sistema simples que gera um gráfico.

  O programa deve gerar um gráfico de faturamento de cada loja registrada:
- Loja A R$120000;
- Loja B R$150000;
- Loja C R$145500 ;
- Loja D R$120500;
- Loja E R$134400;
- Loja F R$119880;

Mostrar em Gráfico de barra o nome das lojas e o valor de sua fatura.
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
