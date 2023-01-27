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
from tkinter import *

def start() -> None:
	# Opening the main window
	window = tk.Tk()
	window.title('AFFP')
	window.geometry('1200x800')

	# Making the Background #545454
	canvas = tk.Canvas(window, width = 1200, height = 800, bg ='#545454')
	canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')

	# Creating the main text
	label = tk.Label(window, text='AUTOMATED FOREST', bg='#545454', fg='white', font=('Garamond', 30))
	label.place(relx = 0.25,rely = 0.47, anchor = 'center')
	label = tk.Label(window, text='FIRE PREDICTION', bg='#545454', fg='white',  font=('Garamond', 30))
	label.place(relx = 0.25,rely = 0.53, anchor = 'center')

	# Creating the Rectangle
	canvas = tk.Canvas(window, width = 600, height = 800, bg ='#323466')
	canvas.place(relx = 0.75, rely = 0.5, anchor = 'center')

	# Creating buttons
	button1 = tk.Button(window, text='Manual Prediction', font=('Garamond', 20), command = lambda: window.destroy())
	button1.place(relx = 0.76, rely = 0.32, anchor = 'center')
	button2 = tk.Button(window, text='Automated Prediction', font=('Garamond', 20), command = lambda: window.destroy())
	button2.place(relx = 0.76, rely = 0.63, anchor = 'center')

	window.mainloop()
	
