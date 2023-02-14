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
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            raise ValueError("Error: cornerradius is greater than width")

        if cornerradius > 0.5*height:
            raise ValueError("Error: cornerradius is greater than height")

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
