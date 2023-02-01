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
from tkinter import ttk


def future(window: tk.Tk, width: int, height: int) -> None:
	# Setting the background color
	main = tk.Canvas(window, width=width, height=height, bg='#545454')
	main.place(relx=0.5, rely=0.5, anchor='center')

	# Line
	main = tk.Canvas(window, width=width / 5 * 4, height=0.01, bg='#323466')
	main.place(relx=0.5, rely=0.15, anchor='center')

	# Creating the title
	label = tk.Label(window, text='FUTURE DATA PREDICTION', bg='#545454', fg='white', font=('Montserrat', 30))
	label.place(relx=0.5, rely=0.1, anchor='center')

	# Creating radio buttons
	v = tk.StringVar(window, "1")

	# Dictionary to create multiple buttons
	values = {str(i): str(i) for i in range(1, 10)}  # Max 9 days, 1-9

	# Creating style element
	s = ttk.Style()
	s.configure('style.TRadiobutton', background='#545454', foreground='white', font=('Montserrat', 20))

	# Rather than creating each button separately
	x = 1
	for (text, value) in values.items():
		ttk.Radiobutton(window, text=text, variable=v, style='style.TRadiobutton', value=value).place(relx=x / 10, rely=0.5, anchor='center')
		x += 1

	# Creating button
	button1 = tk.Button(window, text='    PREDICT    ', font=('Montserrat', 20), borderwidth=0, command=window.destroy)
	button1.place(relx=0.5, rely=0.75, anchor='center')

	window.mainloop()
