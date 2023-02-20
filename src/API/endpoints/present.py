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

from flask import request
from flask_restful import Resource
import numpy as np
import os
from keras.models import load_model

from .assets.observing import currentWeather

class Present(Resource):
	def get(self):
		# Get arguments
		args = dict(request.args)

		# Check if all arguments are present
		if args['place'] == False:
			return {'data': 'Missing arguments. Please provide all arguments.'}, 400

		# Use model to predict fire risk
		weather = currentWeather(args['place'])
		temp = weather['temperature']
		wind = weather['wind']
		rain = weather['rain']
		rh = weather['humidity']

		data = np.array([[temp, rh, wind, rain]])
		path = os.getcwd()

		if path.endswith('src/API'):
			model = load_model(os.getcwd() + '/src/API/endpoints/assets/model/model.h5')
		else:
			model = load_model(os.getcwd() + '/endpoints/assets/model/model.h5')

		prediction = model.predict(data)

		return {'data': str(prediction[0][0])}, 200
