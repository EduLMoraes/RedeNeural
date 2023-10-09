# Implementação de um classificador de imagens simples:
# 
# Escolha um conjunto de dados pequeno, como o MNIST, que consiste em dígitos escritos à mão.
# Utilize uma biblioteca de aprendizado de máquina, como o scikit-learn, para treinar um classificador,
# como um modelo de regressão logística.
# Treine o modelo usando as imagens de treinamento e avalie sua precisão usando as imagens de teste.
# Experimente diferentes parâmetros e técnicas de pré-processamento para melhorar o desempenho do classificador.
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import *

(x_train, y_train),(x_test, y_test) = mnist.load_data()

model = Sequential()

model.add(Conv2D(100, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(100, activation="softmax"))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))