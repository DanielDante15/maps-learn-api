import matplotlib.pyplot as plt
import numpy as np

# Suponhamos que você tenha uma lista de pontos no formato (x, y)
pontos = [(1, 2), (4, 6), (7, 3), (2, 8), (5, 1)]

# Encontre o ponto mais à esquerda, à direita, acima e abaixo
esquerda = min(pontos, key=lambda p: p[0])
direita = max(pontos, key=lambda p: p[0])
acima = max(pontos, key=lambda p: p[1])
abaixo = min(pontos, key=lambda p: p[1])

# Calcule o centro do círculo
centro_x = (esquerda[0] + direita[0]) / 2
centro_y = (acima[1] + abaixo[1]) / 2

# Calcule o raio do círculo
raio = max(np.sqrt((p[0] - centro_x)**2 + (p[1] - centro_y)**2) for p in pontos)
raio+=0.3
# Crie o círculo
circulo = plt.Circle((centro_x, centro_y), raio, fill=False, color='b')

# Crie um gráfico para visualizar o círculo e os pontos
fig, ax = plt.subplots()
ax.add_patch(circulo)

# Adicione os pontos ao gráfico
x, y = zip(*pontos)
ax.scatter(x, y, color='r')

# Defina os limites do gráfico para mostrar todo o círculo
ax.set_xlim(centro_x - raio, centro_x + raio)
ax.set_ylim(centro_y - raio, centro_y + raio)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
