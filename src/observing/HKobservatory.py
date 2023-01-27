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

class futureWeather:
	def __init__(self) -> None:
		data = accessAPI('fnd')
