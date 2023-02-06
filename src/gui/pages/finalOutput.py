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
import numpy as np
import os
from keras.models import load_model


def final_output(GUI, temp: int, rh: int, wind: int, rain: int) -> None:
	# Setting the background color
	canvas = tk.Canvas(GUI.window, width=GUI.width, height=GUI.height, bg='#545454')
	canvas.place(relx=0.5, rely=0.5, anchor='center')

	# Load the model & find the percentage
	new_model = load_model(os.getcwd() + '/src/model/raw/model.h5')
	prediction = new_model.predict(np.array([[temp, rh, wind, rain]]))
	percentage =  prediction[0][0]*100

	# Adding a backbutton
	GUI.backbutton(GUI.start, 0.05, 0.05)

	# Line
	canvas = tk.Canvas(GUI.window, width=GUI.width / 5 * 4, height=0.01, bg='#323466')
	canvas.place(relx=0.5, rely=0.15, anchor='center')

	# Creating the title
	label = tk.Label(GUI.window, text='FINAL OUTPUT', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.5, rely=0.1, anchor='center')

	# Creating other text
	label = tk.Label(GUI.window, text=f'{percentage:.2f}%', bg='#545454', fg='white', font=('Montserrat', 50))
	label.place(relx=0.5, rely=0.5, anchor='center')

	# Creating buttons
	button1 = tk.Button(GUI.window, text='    EXIT    ', font=('Montserrat', 20), borderwidth=0, command=GUI.window.destroy)
	button1.place(relx=0.5, rely=0.9, anchor='center')

	GUI.window.mainloop()
