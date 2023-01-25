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
import pandas as pd
import os
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D, concatenate
from keras import Model
from .datasets import *

# Loading in the training data
x_train = np.asarray(training_data['temp'])
y_train = np.asarray(training_data['RH'])
z_train = np.asarray(training_data['wind'])
l_train = np.asarray(training_data['rain'])

v_train = np.asarray(training_data['area'])

# Set our input layers
inputA = Input(shape=x_train.shape,)
inputB = Input(shape=y_train.shape,)
inputC = Input(shape=z_train.shape,)
inputD = Input(shape=l_train.shape,)

# The first branch operates on the first input
x = Dense(8, activation="relu")(inputA)
x = Dense(4, activation="relu")(x)
x = Model(inputs=inputA, outputs=x)

# The second branch operates on the second input
y = Dense(64, activation="relu")(inputB)
y = Dense(32, activation="relu")(y)
y = Dense(4, activation="relu")(y)
y = Model(inputs=inputB, outputs=y)

# The 3rd branch operates on the second input
z = Dense(64, activation="relu")(inputC)
z = Dense(32, activation="relu")(z)
z = Dense(4, activation="relu")(z)
z = Model(inputs=inputC, outputs=z)

# The 4th branch operates on the second input
l = Dense(64, activation="relu")(inputD)
l = Dense(32, activation="relu")(l)
l = Dense(4, activation="relu")(l)
l = Model(inputs=inputD, outputs=l)

# Combine the output of the 4 branches
combined = concatenate([x.output, y.output, z.output, l.output])

# Apply a FC layer and then a regression prediction on the combined outputs
v = Dense(2, activation="relu")(combined)
v = Dense(1, activation="linear")(v)

# The model will accept the inputs of the 4 branches and then output a single value
model = Model(inputs=[x.output, y.output, z.output, l.output], outputs=vars)
