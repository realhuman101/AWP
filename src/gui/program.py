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
import pyglet
import os


class GUI:
	def __init__(self):
		# Opening the main window
		self.window = tk.Tk()
		self.window.title('AWP')

		self.width = self.window.winfo_width()
		self.height = self.window.winfo_height()

		# Adding the font
		pyglet.font.add_file(os.getcwd() + '/src/gui/pages/assets/fonts/Montserrat.ttf')

		self.window.bind("<Configure>", self.resize)

		# Showing homepage
		self.start()

		self.window.mainloop()

	# Pages
	from .pages.home import start
	from .pages.predictionPages.manualInput import manual_input
	from .pages.predictions import prediction
	from .pages.predictionPages.future import future
	from .pages.predictionPages.present import present
	from .pages.finalOutput import final_output

	# Widgets
	from .pages.assets.backbutton import backbutton
