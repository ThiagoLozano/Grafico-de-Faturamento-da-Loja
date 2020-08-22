import matplotlib.pyplot as plt


class Grafico:
    def __init__(self):
        # Linha X
        self.lojas = ['Loja A', 'Loja B', 'Loja C',
                      'Loja D', 'Loja E', 'Loja F']
        # Linha y
        self.valores = [120000, 150000, 145500,
                        120500, 134400, 119880]

    def GerarGrafico(self):
        # Título do gráfico.
        plt.title('Faturamento total de cada loja no ano de 2019')

        # Título linha x:
        plt.xlabel('Loja')

        # Título Linha y:
        plt.ylabel('Faturado (R$)')

        # Insere as variáveis em gráfico de barra.
        plt.bar(self.lojas, self.valores)

        # Executa o gráfico.
        plt.show()


user = Grafico()
user.GerarGrafico()
