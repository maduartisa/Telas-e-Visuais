import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Estilo geral
sns.set_theme(style="white")
plt.figure(figsize=(10, 8))

# Gerando dados de exemplo (matriz)
np.random.seed(42)
data = np.random.rand(10, 12)

# Transformando em DataFrame para nomes mais amigáveis
df = pd.DataFrame(
    data,
    index=[f"Linha {i}" for i in range(1, 11)],
    columns=[f"Coluna {j}" for j in range(1, 13)]
)

# Criando o mapa de calor
heatmap = sns.heatmap(
    df,
    cmap="mako",               # paleta elegante
    annot=True,                # mostra valores
    fmt=".2f",                 # formato
    linewidths=0.5,            # linhas sutis
    linecolor='white',
    cbar_kws={"shrink": 0.8},  # barra menor
    square=True
)

# Ajustes visuais
plt.title("Mapa de Calor Estético com Seaborn", fontsize=16, weight='bold', pad=20)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

# Remover bordas superiores e laterais
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()  