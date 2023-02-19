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

from flask_restful import Resource, reqparse
import numpy as np
import os
from keras.models import load_model

class Manual(Resource):
	def get(self):
		# Add arguments
		parser = reqparse.RequestParser()

		parser.add_argument('temp', type=int, help='Temperature (Celsius) -> int')
		parser.add_argument('wind', type=int, help='Wind Speed (km/h) -> int')
		parser.add_argument('rain', type=float, help='Rain Size (mm) -> float')
		parser.add_argument('rh', type=int, help='Relative Humidity (%) -> int')

		args = parser.parse_args()

		# Check if all arguments are present
		if all([args['temp'], args['wind'], args['rain'], args['rh']]) is False:
			return {'data': 'Missing arguments. Please provide all arguments.'}, 400

		# Use model to predict fire risk
		data = np.array([[args['temp'], args['rh'], args['wind'], args['rain']]])
		model = load_model(os.getcwd() + '/src/model/raw/model.h5')

		prediction = model.predict(data)

		return {'data': prediction}, 200
