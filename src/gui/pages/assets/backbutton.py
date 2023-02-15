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

from typing import Callable
from .roundedbutton import RoundedButton


def backbutton(GUI, prev_page: Callable, x: int, y: int, anchor: str = 'center', bg: str = '#545454') -> None:
	# Create buttons
	button = RoundedButton(GUI.window, text='← Back', width=100, height=40, font=('Montserrat', 15), bg=bg, clicked=prev_page)
	button.place(relx=x, rely=y, anchor=anchor)
