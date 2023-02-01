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
from typing import Callable


def backbutton(GUI, prev_page: Callable, x: int, y: int, anchor: str = 'center') -> None:
	# Create buttons
	button = tk.Button(GUI.window, text='← Back', font=('Montserrat', 10), borderwidth=0, command=prev_page)
	button.place(relx=x, rely=y, anchor=anchor)

	GUI.window.mainloop()
