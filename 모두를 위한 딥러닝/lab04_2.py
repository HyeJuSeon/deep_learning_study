# lab4 - multi-variable linear regression
import numpy as np
import tensorflow as tf 

xy = np.loadtxt("C:/Users/tjswn/Workspace/VSCode/deep_learning/data-01-test-score.csv", delimiter=',', dtype=np.float32)
x_data = xy[:, :-1]
y_data = xy[:, [-1]]

# Make sure the shape and data are OK
print(x_data, "\nx_data shape: ", x_data.shape)
print(y_data, "\ny_data shape: ", y_data)

tf.model = tf.keras.Sequential()
# activation function doesn't have to be added as a separate layer. Add it as an argument of Dense() layer
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=3, activation='linear'))
#tf.model.add(tf.keras.layers.Activation('linear'))
tf.model.summary()

tf.model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-5))
history = tf.model.fit(x_data, y_data, epochs=2000)

# Ask my score
print("Your score will be ", tf.model.predict([[100, 70, 101]]))
print("Other scores will be ", tf.model.predict([[60, 70, 100], [40, 80, 90]]))