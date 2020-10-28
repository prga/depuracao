import numpy as np

n = int(input('Digite o número de incógnitas: '))

#cria matriz de zeros
a = np.zeros((n, n + 1))

#cria vetor solução com zeros
x = np.zeros(n)

# Lê coeficientes da matriz aumentada
print('Entre com os coeficientes da matriz aumentada:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

# Aplicando método de eliminação da Gauss
# considere que o usuário não dá como entrada pivôs iguais a zero
for i in range(n):

    for j in range(i + 1, n):
        razao = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[k][j] = a[j][k] - razao * a[k][k]

# substituição retrocedida
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

# mostrando solução
print('O vetor solução é: ')
for i in range(n):
    print('X[{}] = {:.2f}'.format(i, x[i]), end='\t')