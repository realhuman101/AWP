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


class RoundedButton(tk.Canvas):
	def __init__(self, master=None, text: str = "", font: tuple[str, int] = ("Montserrat", 30), radius=25, btnforeground="#000000", btnbackground="#ffffff", bg='#545454', clicked=None, *args, **kwargs):
		super(RoundedButton, self).__init__(master, *args, **kwargs)
		self.config(bg=bg)
		self.btnbackground = btnbackground
		self.clicked = clicked

		self.radius = radius

		self.rect = self.round_rectangle(0, 0, 0, 0, tags="button", radius=radius, fill=btnbackground)
		self.text = self.create_text(0, 0, text=text, tags="button", fill=btnforeground, font=font, justify="center")

		self.tag_bind("button", "<ButtonPress>", self.border)
		self.tag_bind("button", "<ButtonRelease>", self.border)
		self.bind("<Configure>", self.resize)

		text_rect = self.bbox(self.text)
		if int(self["width"]) < text_rect[2] - text_rect[0]:
			self["width"] = (text_rect[2] - text_rect[0]) + 10

		if int(self["height"]) < text_rect[3] - text_rect[1]:
			self["height"] = (text_rect[3] - text_rect[1]) + 10

	def round_rectangle(self, x1, y1, x2, y2, radius=25, update=False, **kwargs):
		points = [x1 + radius, y1,
				x1 + radius, y1,
				x2 - radius, y1,
				x2 - radius, y1,
				x2, y1,
				x2, y1 + radius,
				x2, y1 + radius,
				x2, y2 - radius,
				x2, y2 - radius,
				x2, y2,
				x2 - radius, y2,
				x2 - radius, y2,
				x1 + radius, y2,
				x1 + radius, y2,
				x1, y2,
				x1, y2 - radius,
				x1, y2 - radius,
				x1, y1 + radius,
				x1, y1 + radius,
				x1, y1]

		if not update:
			return self.create_polygon(points, **kwargs, smooth=True)
		else:
			self.coords(self.rect, points)

	def resize(self, event):
		text_bbox = self.bbox(self.text)

		if self.radius > event.width or self.radius > event.height:
			radius = min((event.width, event.height))
		else:
			radius = self.radius

		width, height = event.width, event.height

		if event.width < text_bbox[2] - text_bbox[0]:
			width = text_bbox[2] - text_bbox[0] + 30

		if event.height < text_bbox[3] - text_bbox[1]:
			height = text_bbox[3] - text_bbox[1] + 30

		self.round_rectangle(5, 5, width - 5, height - 5, radius, update=True)

		bbox = self.bbox(self.rect)

		x = ((bbox[2] - bbox[0]) / 2) - ((text_bbox[2] - text_bbox[0]) / 2)
		y = ((bbox[3] - bbox[1]) / 2) - ((text_bbox[3] - text_bbox[1]) / 2)

		self.moveto(self.text, x, y)

	def border(self, event):
		if event.type == "4":
			self.itemconfig(self.rect, fill="#d2d6d3")
			if self.clicked is not None:
				self.clicked()
		else:
			self.itemconfig(self.rect, fill=self.btnbackground)
