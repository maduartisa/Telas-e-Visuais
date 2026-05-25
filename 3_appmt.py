# Importa as bibliotecas

import matplotlib.pyplot as plt

import seaborn as sns
 
# Dados

meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]

vendas = [10, 25, 18, 30, 22]
 
# Estilo do gráfico com Seaborn

sns.set_style("darkgrid")
 
# Cria o gráfico com Matplotlib

plt.plot(meses, vendas, marker="o")
 
# Título e nomes dos eixos

plt.title("Vendas da Loja")

plt.xlabel("Meses")

plt.ylabel("Quantidade de Vendas")
 
# Mostra o gráfico

plt.show()

 