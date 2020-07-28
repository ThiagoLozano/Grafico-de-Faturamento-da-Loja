import matplotlib.pyplot as plt

# Variável Linha x:
meses = ['Loja A',
         'Loja B',
         'Loja C',
         'Loja D',
         'Loja E',
         'Loja F']

# Variável linha y:
valores = [120000,
           150000,
           145500,
           120500,
           134400,
           119880]

# Título do gráfico.
plt.title('Faturamento total de cada loja no ano de 2019')

# Título linha x:
plt.xlabel('Meses')

# Título Linha y:
plt.ylabel('Faturado (R$)')

# Insere as variáveis em gráfico de barra.
plt.bar(meses, valores)

# Executa o gráfico.
plt.show()
