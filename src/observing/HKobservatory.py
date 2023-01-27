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

import requests
import json
import re
from collections import defaultdict

from .unitConvert import convertWind

def accessAPI(dataType: str) -> dict:
	url = f'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang=en'
	response = requests.get(url)
	data = response.json()
	return data

# CURRENT DATA

def currentWeather(place: str) -> dict:
	data = accessAPI('rhrread')
	result = defaultdict(lambda: 'N/A')

	rainfall_data = data["rainfall"]["data"]
	temperature_data = data["temperature"]["data"]
	humidity_data = data["humidity"]["data"]

	for item in rainfall_data:
		if item["place"] == place:
			result['rain'] = item["max"]
			break

	for item in temperature_data:
		if item["place"] == place:
			result['temperature'] = item["value"]
			break

	for item in humidity_data:
		if item["place"] == place:
			result['humidity'] = item["value"]
			break

	try:
		if result['humidity'] == 'N/A':
			result['humidity'] = humidity_data[0]["value"]
	except IndexError:
		result['humidity'] = 0
	
	try:
		if result['temperature'] == 'N/A':
			result['temperature'] = temperature_data[0]["value"]
	except IndexError:
		result['temperature'] = 20 # Approx room temperature
	
	try:
		if result['rain'] == 'N/A':
			result['rain'] = rainfall_data[0]["max"]
	except IndexError:
		result['rain'] = 0
	
	return result

# FUTURE DATA

def futureWeather() -> dict:
	data = accessAPI('fnd')
	result = {}

	for time, forecast in enumerate(data["weatherForecast"], 1):
		windSpeed = convertWind(int(re.search(r'\d+', forecast["forecastWind"]).group()))

		result[time] = {
			"temp": (forecast["forecastMaxtemp"]["value"]+forecast["forecastMintemp"]["value"])/2,
			"rh": (forecast["forecastMaxrh"]["value"]+forecast["forecastMinrh"]["value"])/2,
			"wind": windSpeed,
			"rain": 10 if forecast["PSR"] == "High" else 5 if forecast["PSR"] == "Medium High" else 0
		}
	
	return result
