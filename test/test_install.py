class InstallTest():

    def keras_import(self):
        import sys
        import keras
        assert('keras' in sys.modules)

    def matplotlib_import(self):
        import sys
        import matplotlib
        assert('matplotlib' in sys.modules)
        import matplotlib.pyplot as plt
        assert('matplotlib.pyplot' in sys.modules)

    def numpy_import(self):
        import sys
        import numpy
        assert('numpy' in sys.modules)

    def simple_nn(self):
        import numpy as np
        from keras.models import Sequential
        from keras.layers.core import Dense, Activation
        from keras.optimizers import SGD

        model = Sequential()
        model.add(Dense(2, input_dim=4))
        model.add(Activation('sigmoid'))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        sgd = SGD(lr=0.01)
        model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])
        result = model.predict(np.asarray([1,2,3,4]).reshape([1, 4]))
        assert(type(result) is np.ndarray)


if __name__ == "__main__":
    test = InstallTest()
    test.keras_import()
    test.matplotlib_import()
    test.numpy_import()
    test.simple_nn()
    print("If no assertion errors have been printed above, all tests passed and you are good to go!")
