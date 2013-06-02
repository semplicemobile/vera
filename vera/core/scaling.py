#
# vera - Semplice Mobile User Interface
# Copyright (C) 2013  Semplice Mobile Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file contains the scaling core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os

WIDTH = int(os.environ["VERA_WIDTH"])
HEIGHT = int(os.environ["VERA_HEIGHT"])
SCALING = float(os.environ["VERA_SCALING"])

def getNewSize(width, height, scaling=SCALING):
	"""Returns the modified width and height basing on scaling."""
	
	width = int(scaling*width/1.0)
	height = int(scaling*height/1.0)
	
	return width, height

def resize(obj, scaling=SCALING):
	"""Resizes obj to match the scaling value."""
	
	# Size
	width, height = getNewSize(obj.get_size())

	obj.set_size(width,height)
