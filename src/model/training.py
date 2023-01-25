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
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras import Model
from .datasets import *

# Loading in the training data
temp_train = np.asarray(training_data['temp'])
rh_train = np.asarray(training_data['RH'])
wind_train = np.asarray(training_data['wind'])
rain_train = np.asarray(training_data['rain'])

# Obtaining the x_train and y_train data
x_train = np.column_stack((temp_train, rh_train, wind_train, rain_train))
y_train = np.asarray(training_data['area'].apply(lambda x: 1 if x > 0 else 0))

# Obtaining the shape of the input data
input_shape = x_train.shape[1:]
