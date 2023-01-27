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

def accessAPI(dataType: str) -> dict:
	url = f'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang=en'
	response = requests.get(url)
	data = json.loads(response.json())
	return data

# CURRENT DATA

class currentWeather:
	def __init__(self) -> None:
		data = accessAPI('rhrread')

# FUTURE DATA

def futureWeather() -> dict:
	data = accessAPI('fnd')
	result = {}

	for time, forecast in enumerate(data["weatherForecast"]):
		result[time] = {
			"temp": (forecast["forecastMaxtemp"]["value"]+forecast["forecastMintemp"]["value"])/2,
			"rh": (forecast["forecastMaxrh"]["value"]+forecast["forecastMinrh"]["value"])/2,
			"wind": int(re.search(r'\d+', forecast["forecastWind"]).group()),
			"rain": 10 if forecast["PSR"] == "High" else 5 if forecast["PSR"] == "Medium High" else 0
		}
	return data
