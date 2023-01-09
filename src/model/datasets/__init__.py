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

import pandas as pd
import os

# Reading the CSV files into Dataframes
training_data: pd.DataFrame = pd.read_csv(
											os.path.join(
												os.path.dirname(__file__), 
												"Training_Data.csv"
											)
										)

testing_data: pd.DataFrame = pd.read_csv(
											os.path.join(
												os.path.dirname(__file__), 
												"Testing_Data.csv"
											)
										)

# Removing/Dropping useless columns for the testing data
testing_data = testing_data.drop(['year','month','day','FFMC','DMC','DC','ISI','BUI','FWI'], axis=1)
training_data = training_data.drop(['X','Y','month','day','FFMC','DMC','DC','ISI',], axis=1)

# Stripping whitespaces from all the data
training_data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
testing_data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
