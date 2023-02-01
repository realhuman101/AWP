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

import tkinter as tk


def present(GUI) -> None:
	# Setting the background color
	canvas = tk.Canvas(GUI.window, width=GUI.width, height=GUI.height, bg='#545454')
	canvas.place(relx=0.5, rely=0.5, anchor='center')

	# Line
	canvas = tk.Canvas(GUI.window, width=GUI.width / 5 * 4, height=0.01, bg='#323466')
	canvas.place(relx=0.5, rely=0.15, anchor='center')

	# Creating the title
	label = tk.Label(GUI.window, text='PRESENT DATA PREDICTION', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.5, rely=0.1, anchor='center')

	# Dropdown menu options
	REGIONS = ['Cheung Chau', 'Wan Chai', 'Ta Kwu Ling', 'Tai Po Kau', 'Wong Tai Sin', 'Pak Shek Kok', 'Ma On Shan', 'Chek Lap Kok', 'Cheung Sha', 'Central & Western District', 'Pak Tam Chung', 'Yau Tsim Mong', 'Sai Kung Man Yee Road', 'Kwai Tsing', 'Eastern District', 'Nei Kung Uk', 'Lee Kum Kee Family Walk', 'Peng Chau', 'Hong Kong Museum of History', 'Pak Tam Au', 'Sham Shui Po', 'Tuen Mun', 'High Island', 'Shatin Pass', 'Kwun Tong Ferry', 'Happy Valley', 'Man Kam To', 'Kwai Chung', 'Kwun Tong', 'Plover Cove', 'Nam Long Shan', 'Ngong Ping', 'Kowloon City', 'Tai Mei Tuk', 'Mui Wo', 'Wong Chuk Hang', 'Tsing Yi', 'Hong Kong Park', "King's Park", 'Sai Kung Ho Chung', 'Hong Kong Observatory', 'Ho Man Tin', 'Lantau Island', 'Golden Hill', 'Kwai Fong', 'Tai Po', 'Yuen Long', 'Shek Kong', 'Lion Rock', 'Lamma Island', 'Kwun Yam Shan', 'Tseung Kwan O', 'Hang Hau', 'Sai Kung', 'Islands District', 'Sha Tin', 'Pak Kong', 'Lau Fau Shan', 'Southern District', 'North District', 'Tsuen Wan', 'Lo Wu', 'Tai Mo Shan']

	options = [
		"Chose a reigon:",
		*REGIONS
	]

	# datatype of menu text
	clicked = tk.StringVar()
	clicked.set("Chose a reigon:")

	# Create Dropdown menu
	drop = tk.OptionMenu(GUI.window, clicked, *options)
	drop.config(font=('Montserrat', 20), borderwidth=0, width=20)
	drop.place(relx=0.5, rely=0.4, anchor='center')

	# Creating buttons
	button1 = tk.Button(GUI.window, text='    PREDICT    ', font=('Montserrat', 20), borderwidth=0, command=GUI.window.destroy)
	button1.place(relx=0.5, rely=0.75, anchor='center')

	GUI.window.mainloop()
