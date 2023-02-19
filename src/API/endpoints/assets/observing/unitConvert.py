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

def convertWind(windSpeed: int) -> int:
	'''
	Converts wind speed from Beaufort scale to km/h

	Conversion table from https://www.weather.gov/jetstream/beaufort_max
	'''

	if windSpeed == 0:
		windSpeed = 0
	elif windSpeed == 1:
		windSpeed = 3
	elif windSpeed == 2:
		windSpeed = 9
	elif windSpeed == 3:
		windSpeed = 16
	elif windSpeed == 4:
		windSpeed = 24
	elif windSpeed == 5:
		windSpeed = 34
	elif windSpeed == 6:
		windSpeed = 44
	elif windSpeed == 7:
		windSpeed = 56
	elif windSpeed == 8:
		windSpeed = 68
	elif windSpeed == 9:
		windSpeed = 82
	elif windSpeed == 10:
		windSpeed = 96
	elif windSpeed == 11:
		windSpeed = 110
	elif windSpeed == 12:
		windSpeed = 124
	elif windSpeed == 13:
		windSpeed = 141
	elif windSpeed == 14:
		windSpeed = 157
	elif windSpeed == 15:
		windSpeed = 175
	elif windSpeed == 16:
		windSpeed = 192
	

	return windSpeed
