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
import requests
import math
import re
from collections import defaultdict

from .unitConvert import convertWind


def accessAPI(dataType: str) -> dict:
	'''
	To access the HKO API, documentation can be found at https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf

	`datatype: str` = The type of data to be accessed, can be one of the following:
	- `flw`: Local Weather Forecast
	- `fnd`: 9-day Weather Forecast
	- `rhrread`: Current Weather Report
	- `warnsum`: Weather Warning Summary
	- `warningInfo`: Weather Warning Information
	- `swt`: Special Weather Tips

	Returns a JSON of the response data
	'''

	url = f'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang=en'
	response = requests.get(url)
	data = response.json()
	return data

# CURRENT DATA


def getCurrentWind(place: str) -> float:
	csv = pd.read_csv('https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_10min_wind.csv')

	try:
		result = csv.loc[csv['Automatic Weather Station'] == place, '10-Minute Mean Speed(km/hour)'].iloc[0]
	except IndexError:
		result = csv['10-Minute Mean Speed(km/hour)'].iloc[0]

	if math.isnan(result):
		result = csv['10-Minute Mean Speed(km/hour)'].iloc[0]

	return result


def currentWeather(place: str) -> dict:
	'''
	To access current weather data, specifically the temperature (C), humidity (%) and rainfall (mm)
	The data is returned in a dictionary with the following keys:
	- `temperature`: The temperature in degrees Celsius
	- `humidity`: The humidity in percentage
	- `rain`: The rainfall in millimetres
	- `wind`: The wind speed in kilometres per hour

	`place: str` = The place to get the data from

	In the event that the data is not available, the value will be set to 0 (unless the temperature, which will be set to 20)
	'''

	# Access data
	data = accessAPI('rhrread')
	result = defaultdict(lambda: 'N/A')

	rainfall_data = data['rainfall']['data']
	temperature_data = data['temperature']['data']
	humidity_data = data['humidity']['data']

	# Get data specific to place
	for item in rainfall_data:
		if item['place'] == place:
			result['rain'] = item['max']
			break

	for item in temperature_data:
		if item['place'] == place:
			result['temperature'] = item['value']
			break

	for item in humidity_data:
		if item['place'] == place:
			result['humidity'] = item['value']
			break

	# If data is not available, use the first available data
	# If there is no data available, set to 0 (except temperature, which is set to 20 degrees)
	try:
		if result['humidity'] == 'N/A':
			result['humidity'] = humidity_data[0]['value']
	except IndexError:
		result['humidity'] = 0

	try:
		if result['temperature'] == 'N/A':
			result['temperature'] = temperature_data[0]['value']
	except IndexError:
		result['temperature'] = 20  # Approx room temperature

	try:
		if result['rain'] == 'N/A':
			result['rain'] = rainfall_data[0]['max']
	except IndexError:
		result['rain'] = 0

	# Get wind speed
	result['wind'] = getCurrentWind(place)

	return dict(result)

# FUTURE DATA


def futureWeather() -> dict:
	'''
	To access future weather data, specifically the temperature (C), humidity (%), wind speed (km/h) and rainfall (mm)
	The data is returned in a dictionary of days, from 1-9, with the following keys:
	- `temp`: The temperature in degrees Celsius
	- `rh`: The humidity in percentage
	- `wind`: The wind speed in kilometres per hour
	- `rain`: The rainfall in millimetres
	'''

	# Access data
	data = accessAPI('fnd')
	result = {}

	# Get data for each day in the 9 day forecast
	for time, forecast in enumerate(data['weatherForecast'], 1):
		windSpeed = convertWind(int(re.search(r'\d+', forecast['forecastWind']).group()))  # Convert wind speed to km/h

		# Set results for each day
		result[time] = {
			'temp': (forecast['forecastMaxtemp']['value'] + forecast['forecastMintemp']['value']) / 2,
			'rh': (forecast['forecastMaxrh']['value'] + forecast['forecastMinrh']['value']) / 2,
			'wind': windSpeed,
			'rain': 10 if forecast['PSR'] == 'High' else 5 if forecast['PSR'] == 'Medium High' else 0
		}

	return result
