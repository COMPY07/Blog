from keras import layers, models
from sklearn.preprocessing import *
from sklearn.datasets import load_diabetes
import numpy as np

class ANN(models.Model):
    def __init__(self, Nin, Nh, Nout):
        # network 계층 준비 및 기능 활성화
        hidden = layers.Dense(Nh)
        output = layers.Dense(Nout)
        relu = layers.Activation("relu")

        # network 요소 연결

        x = layers.Input(shape=(Nin,))
        h = relu(hidden(x))
        y = output(h)

        super().__init__(x, y)
        self.compile(loss="mse", optimizer="sgd")

def Data_PreProcessing():
    diabets = load_diabetes()
    diabets_x = diabets.data
    X_train = diabets_x[:-30]
    Y_train = diabets.target[:-30]

    X_test=  diabets_x[-30:]
    Y_test=  diabets.target[-30:]

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return (X_train, Y_train), (X_test, Y_test)


# 시각화

import matplotlib as plt


def main():
    Nin = 0
    Nh = 5
    Nout = 1

    model = ANN(Nin, Nh, Nout)
    print("start")
    (X_train, y_train), (X_test, y_test) = Data_PreProcessing()
    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)

    learn_history = model.fit(X_train, y_train, epochs = 100, batch_size = 100, validation_split = 0.2, verbose=2)

    performance_test = model.evaluate(X_test, y_test, batch_size = 100)
    print(f"loss : {performance_test}")


    # plot_loss(learn_history)

if "__main__" == __name__:
    main()