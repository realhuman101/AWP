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

from .predictions.future import future
from .predictions.present import present


def prediction(window: tk.Tk, width: int, height: int) -> None:
	# Setting the background color
	canvas = tk.Canvas(window, width = width, height = height, bg ='#545454')
	canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')

 	# Adding the font
	#pyglet.font.add_file('src\gui\fonts\Montserrat.ttf')

	# Creating the main text
	label = tk.Label(window, text='AUTOMATED', bg='#545454', fg='white', font=('Times new roman', 30))
	label.place(relx = 0.25,rely = 0.47, anchor = 'center')
	label = tk.Label(window, text='PREDICTIONS', bg='#545454', fg='white',  font=('Times new roman', 30))
	label.place(relx = 0.25,rely = 0.53, anchor = 'center')

	# Creating the Rectangle
	canvas = tk.Canvas(window, width = width/2, height = height, bg ='#323466')
	canvas.place(relx = 0.75, rely = 0.5, anchor = 'center')

	# Creating buttons
	button1 = tk.Button(window, text='PRESENT PREDICTION', font=('Times new roman', 20), borderwidth=0, command=lambda:present(window, width, height))
	button1.place(relx = 0.76, rely = 0.32, anchor = 'center')
	button2 = tk.Button(window, text='FUTURE PREDICTION', font=('Times new roman', 20), borderwidth=0, command=lambda:future(window, width, height))
	button2.place(relx = 0.76, rely = 0.63, anchor = 'center')

	window.mainloop()

