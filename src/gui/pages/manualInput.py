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


def manual_input(GUI) -> None:
	# Setting the background color
	canvas = tk.Canvas(GUI.window, width=GUI.width, height=GUI.height, bg='#545454')
	canvas.place(relx=0.5, rely=0.5, anchor='center')

	# Adding a backbutton
	GUI.backbutton(GUI.start, 0.05, 0.05)

	# Line
	canvas = tk.Canvas(GUI.window, width=GUI.width / 5 * 4, height=0.01, bg='#323466')
	canvas.place(relx=0.5, rely=0.15, anchor='center')

	# Creating the title
	label = tk.Label(GUI.window, text='MANUAL INPUT', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.5, rely=0.1, anchor='center')

	# Creating other text
	label = tk.Label(GUI.window, text='TEMPERATURE (Celcius)', bg='#545454', fg='white', font=('Montserrat', 15))
	label.place(relx=0.33, rely=0.30, anchor='center')
	label = tk.Label(GUI.window, text='RELATIVE HUMIDITY (%)', bg='#545454', fg='white', font=('Montserrat', 15))
	label.place(relx=0.66, rely=0.30, anchor='center')
	label = tk.Label(GUI.window, text='WIND SPEED (km/h)', bg='#545454', fg='white', font=('Montserrat', 15))
	label.place(relx=0.33, rely=0.60, anchor='center')
	label = tk.Label(GUI.window, text='RAIN (mm)', bg='#545454', fg='white', font=('Montserrat', 15))
	label.place(relx=0.66, rely=0.60, anchor='center')

	# Creating the entry boxes
	temp = tk.Entry(GUI.window, width=20, font=('Montserrat', 20))
	temp.place(relx=0.33, rely=0.35, anchor='center')
	rh = tk.Entry(GUI.window, width=20, font=('Montserrat', 20))
	rh.place(relx=0.66, rely=0.35, anchor='center')
	ws = tk.Entry(GUI.window, width=20, font=('Montserrat', 20))
	ws.place(relx=0.33, rely=0.65, anchor='center')
	rain = tk.Entry(GUI.window, width=20, font=('Montserrat', 20))
	rain.place(relx=0.66, rely=0.65, anchor='center')

	# Creating buttons
	button1 = tk.Button(GUI.window, text='    PREDICT    ', font=('Montserrat', 20), borderwidth=0, command=lambda: GUI.final_output(float(temp.get()), float(rh.get()), float(ws.get()), float(rain.get())))
	button1.place(relx=0.5, rely=0.9, anchor='center')

	GUI.window.mainloop()
