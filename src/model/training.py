# ======================================================================
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ======================================================================

# Importing the required libraries
import tensorflow as tf
import numpy as np
import os
from keras.models import Model, save_model
from keras.layers import Input, Dense, Dropout
from sklearn.model_selection import train_test_split

from datasets import dataset


# Loading in the training data
temp_train = np.asarray(dataset['Temperature'])
rh_train = np.asarray(dataset['RH'])
wind_train = np.asarray(dataset['Ws'])
rain_train = np.asarray(dataset['Rain'])

# Obtaining the x_train and y_train data
xData = np.column_stack((temp_train, rh_train, wind_train, rain_train))
yData = np.asarray(dataset['Classes'].apply(lambda x: 1 if x == 'fire' else 0))

x_train, x_test, y_train, y_test = train_test_split(xData, yData, test_size=0.25)

# Obtaining the shape of the input data
input_shape = x_train.shape[1:]

# Define the input layer
inputs = Input(shape=input_shape)

# Define the first dense layer
x = Dense(32, activation='relu', kernel_regularizer='l1')(inputs)

# Define the dropout layer
x = Dropout(0.2)(x)

# Define the second dense layer
x = Dense(16, activation='relu')(x)

# Define the output layer
outputs = Dense(1, activation='sigmoid')(x)

# Create the model
model = Model(inputs=inputs, outputs=outputs)

# Define the optimizer
optimizer = tf.keras.optimizers.Adam(
	learning_rate=0.001,
	beta_1=0.9,
	beta_2=0.999,
	epsilon=1e-07
)

# Compile the model
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0) # Verbose = 0 for minimal output
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)

# Save model
save_model(
    model,
    os.path.abspath(os.getcwd()) + "/src/model/raw/model.h5",
    overwrite=True,
    include_optimizer=True,
    save_format="h5",
    signatures=None,
    options=None
)
