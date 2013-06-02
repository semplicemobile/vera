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
# This file contains the applications core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os

from xdg import DesktopEntry

def getGroup(directory):
	"""Returns a tuple with every Application-able objects in directory."""
	
	lst = []
	
	for _file in os.listdir(directory):
		if _file.endswith(".desktop"):
			lst.append(Application(_file.strip(".desktop"), directory))
	
	return tuple(lst)

class Application(DesktopEntry.DesktopEntry):
	
	"""The Application class represents a 3rd-party application in vera."""
	
	
	def __init__(self, application, searchdirs="/usr/share/applications"):
		"""Initialize the object.
		
		application: the .desktop file name (without path and extension)
		searchdirs: the directories where search for the file.
		            It can be a string or a tuple/list.
		            It defaults to "/usr/share/applications."
		"""
		
		filename = None
		
		if type(searchdirs) in (tuple, list):
			for _dir in searchdirs:
				path = os.path.join(_dir, application + ".desktop")
				if os.path.exists(path):
					filename = path
					break
		else:
			path = os.path.join(searchdirs, application + ".desktop")
			if os.path.exists(path): filename = path
					
		DesktopEntry.DesktopEntry.__init__(self, filename)
		
		self.application = application
		
		
		
