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
from .assets.roundedbutton import RoundedButton


def start(GUI) -> None:
	# Setting the background color
	canvas = tk.Canvas(GUI.window, width=GUI.width, height=GUI.height, bg='#545454')
	canvas.place(relx=0.5, rely=0.5, anchor='center')

	# Creating the main text
	label = tk.Label(GUI.window, text='AUTOMATED', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.25, rely=0.47, anchor='center')
	label = tk.Label(GUI.window, text='WILDFIRE', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.25, rely=0.53, anchor='center')
	label = tk.Label(GUI.window, text='PREDICTION', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.25, rely=0.59, anchor='center')

	# Creating the Rectangle
	canvas = tk.Canvas(GUI.window, width=GUI.width / 2, height=GUI.height, bg='#323466')
	canvas.place(relx=0.75, rely=0.5, anchor='center')

	# Creating buttons
	button1 = RoundedButton(GUI.window, text='MANUAL PREDICTION', width=300, height=45, font=('Montserrat', 20), bg='#323466', clicked=GUI.manual_input)
	button1.place(relx=0.76, rely=0.32, anchor='center')
	button2 = RoundedButton(GUI.window, text='AUTOMATED PREDICTION', width=300, height=45, font=('Montserrat', 20), bg='#323466', clicked=GUI.prediction)
	button2.place(relx=0.76, rely=0.63, anchor='center')

	GUI.window.mainloop()
