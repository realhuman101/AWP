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

import time
import requests

from ..observing import currentWeather, futureWeather


def test_currentWeather() -> None:
	'''
	Test the current weather function
	'''

	# List of some places in Hong Kong to test the weather data
	places = ['Cheung Chau', 'Wan Chai', 'Ta Kwu Ling', 'Tai Po Kau', 'Wong Tai Sin', 'Pak Shek Kok', 'Ma On Shan', 'Chek Lap Kok', 'Cheung Sha', 'Central & Western District', 'Pak Tam Chung', 'Yau Tsim Mong', 'Sai Kung Man Yee Road', 'Kwai Tsing', 'Eastern District', 'Nei Kung Uk', 'Lee Kum Kee Family Walk', 'Peng Chau', 'Hong Kong Museum of History', 'Pak Tam Au', 'Sham Shui Po', 'Tuen Mun', 'High Island', 'Shatin Pass', 'Kwun Tong Ferry', 'Happy Valley', 'Man Kam To', 'Kwai Chung', 'Kwun Tong', 'Plover Cove', 'Nam Long Shan', 'Ngong Ping', 'Kowloon City', 'Tai Mei Tuk', 'Mui Wo', 'Wong Chuk Hang', 'Tsing Yi', 'Hong Kong Park', "King's Park", 'Sai Kung Ho Chung', 'Hong Kong Observatory', 'Ho Man Tin', 'Lantau Island', 'Golden Hill', 'Kwai Fong', 'Tai Po', 'Yuen Long', 'Shek Kong', 'Lion Rock', 'Lamma Island', 'Kwun Yam Shan', 'Tseung Kwan O', 'Hang Hau', 'Sai Kung', 'Islands District', 'Sha Tin', 'Pak Kong', 'Lau Fau Shan', 'Southern District', 'North District', 'Tsuen Wan', 'Lo Wu', 'Tai Mo Shan']

	# Test the weather data for each place
	for place in places:
		while True:
			try:
				weather = currentWeather(place)
				break
			except requests.exceptions.ConnectionError:
				time.sleep(0.01)

		# Check if the weather data is within the expected range
		assert 50 >= weather['temperature'] >= -20
		assert 100 >= weather['humidity'] >= 0
		assert 500 >= weather['rain'] >= 0
		assert 200 >= weather['wind'] >= 0


def test_futureWeather() -> None:
	'''
	Test the future weather function and the return values
	'''

	weather = futureWeather()

	for day in range(1, 10):  # 9 days of weather data
		# Check if the weather data is within the expected range
		assert 50 >= weather[day]['temp'] >= -20
		assert 100 >= weather[day]['rh'] >= 0
		assert 192 >= weather[day]['wind'] >= 0 and weather[day]['wind'] in [0, 3, 9, 16, 24, 34, 44, 56, 68, 82, 96, 110, 124, 141, 157, 175, 192]
		assert 500 >= weather[day]['rain'] >= 0
