from sklearn.neighbors import KNeighborsClassifier

# Dados de treinamento
X_train = [[1.2, 3.4], [2.3, 4.5], [3.1, 1.8], [2.4, 3.7]]
y_train = ['Iris setosa', 'Iris setosa', 'Iris versicolor', 'Iris versicolor']

# Dados de teste
X_test = [[1.4, 4.1], [1.5, 4.0], [3.5, 3.0]]

# Criação do classificador
knn = KNeighborsClassifier(n_neighbors=1)

# Treinamento do modelo
knn.fit(X_train, y_train)

# Classificação dos dados de teste
y_pred = knn.predict(X_test)

# Resultados
for i in range(len(X_test)):
    print("Flor de teste:", X_test[i])
    print("Classe prevista:", y_pred[i])
    print()
