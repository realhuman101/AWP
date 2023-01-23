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
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, concatenate
from keras import Model
from .datasets import *

# Loading in the training data
x_train = np.asarray(training_data['temp'])
y_train = np.asarray(training_data['RH'])
z_train = np.asarray(training_data['wind'])
l_train = np.asarray(training_data['rain'])

v_train = np.asarray(training_data['area'])

# define 4  sets of inputs
inputA = x_train.shape[1]
inputB = y_train.shape[1]
inputC = z_train.shape[1]
inputD = l_train.shape[1]

# the first branch operates on the first input
x = Dense(8, activation="relu")(inputA)
x = Dense(4, activation="relu")(x)
x = Model(inputs=inputA, outputs=x)

# the second branch opreates on the second input
y = Dense(64, activation="relu")(inputB)
y = Dense(32, activation="relu")(y)
y = Dense(4, activation="relu")(y)
y = Model(inputs=inputB, outputs=y)

# the 3rd branch opreates on the second input
z = Dense(64, activation="relu")(inputC)
z = Dense(32, activation="relu")(z)
z = Dense(4, activation="relu")(z)
z = Model(inputs=inputC, outputs=z)

# the 4th branch opreates on the second input
l = Dense(64, activation="relu")(inputD)
l = Dense(32, activation="relu")(l)
l = Dense(4, activation="relu")(l)
l = Model(inputs=inputD, outputs=l)

# combine the output of the 4 branches
combined = concatenate([x.output, y.output, z.output, l.output])

# apply a FC layer and then a regression prediction on the
# combined outputs
v = Dense(2, activation="relu")(combined)
v = Dense(1, activation="linear")(v)

# our model will accept the inputs of the 4 branches and
# then output a single value
model = Model(inputs=[x.output, y.output, z.output, l.output], outputs=vars)
