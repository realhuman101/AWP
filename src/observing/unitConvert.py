def convertWind(windSpeed: int) -> int:
	'''
	Converts wind speed from Beaufort scale to km/h
	'''

	match windSpeed:
		case 0:
			windSpeed = 0
		case 1:
			windSpeed = 3
		case 2:
			windSpeed = 9
		case 3:
			windSpeed = 16
		case 4:
			windSpeed = 24
		case 5:
			windSpeed = 34
		case 6:
			windSpeed = 44
		case 7:
			windSpeed = 56
		case 8:
			windSpeed = 68
		case 9:
			windSpeed = 82
		case 10:
			windSpeed = 96
		case 11:
			windSpeed = 110
		case 12:
			windSpeed = 124
		case 13:
			windSpeed = 141
		case 14:
			windSpeed = 157
		case 15:
			windSpeed = 175
		case 16:
			windSpeed = 192
	
	return windSpeed
