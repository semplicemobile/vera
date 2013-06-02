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
# This file contains the scriptLoader core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os

from gi.repository import Clutter

RESDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../resources")

class ScriptHandler:
	"""The ScriptHandler class handles one (or more) ClutterScripts. """
	
	def __init__(self):
		
		self.loaded = {}
	
	def load(self, script):
		"""Loads script from the resources directory.
		
		If it is already loaded, it will return the script's handle in self.loaded."""
		
		if not script in self.loaded:
			self.loaded[script] = Clutter.Script()
			self.loaded[script].load_from_file(os.path.join(RESDIR, script + ".json"))
		
		return self.loaded[script]
