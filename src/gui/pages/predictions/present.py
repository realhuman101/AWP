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


def present(window: tk.Tk, width: int, height: int) -> None:
	# Setting the background color
	canvas = tk.Canvas(window, width = width, height = height, bg ='#545454')
	canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')

	# Line 
	canvas = tk.Canvas(window, width = width/5*4, height = 0.01, bg ='#323466')
	canvas.place(relx = 0.5, rely = 0.15, anchor = 'center')

	# Creating the title
	label = tk.Label(window, text='PRESENT DATA PREDICTION', bg='#545454', fg='white', font=('Times new roman', 30))
	label.place(relx = 0.5,rely = 0.1, anchor = 'center')
  
	# Dropdown menu options
	options = [
		"Chose a reigon:",
		"New territory",
		"Tung Chung",
		"Sai Kung",
		"Kowloon",
		"Sai wan",
		"Wong Tai Sin",
	]
	
	# datatype of menu text
	clicked = tk.StringVar()
	clicked.set( "Chose a reigon:" )
	
	# Create Dropdown menu
	drop = tk.OptionMenu(window, clicked, *options)
	drop.config(font=('Times new roman', 20), borderwidth=0, width=20)
	drop.place(relx = 0.5, rely = 0.4, anchor = 'center')

	 # Creating buttons
	button1 = tk.Button(window, text='    PREDICT    ', font=('Times new roman', 20), borderwidth=0, command = window.destroy)
	button1.place(relx = 0.5, rely = 0.75, anchor = 'center')

	window.mainloop()
	