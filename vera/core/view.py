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
# This file contains the view core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

from gi.repository import Clutter

class View:
	"""The View base class is a convenient class to easily create new
	views."""

	requires = ()
	retrieve = {}
	to_stage = {}
	
	def __init__(self, handler, stage, settings=None):
		"""Initialize the View.
		
		handler is a ScriptHandler object, from vera.core.scriptLoader.
		stage is the main vera stage."""
		
		self.handler = handler
		self.stage = stage
		self.settings = settings
		self.loaded = {}
		self.objects = {}
				
		for item in self.requires:
			self.loaded[item] = handler.load(item)
			
			if item in self.retrieve:
				# We need to fill self.objects with retrieved items
				self.objects[item] = {}
				for obj in self.retrieve[item]:
					self.objects[item][obj] = self.loaded[item].get_object(obj)
	
	def ready(self):
		"""Called by the view loader after the View construction.
		
		Store here what the view should do."""
		
		pass
	
	def add_to_stage(self):
		"""Called after ready, it adds the items in self.to_stage to the
		main stage."""
		
		# We need to follow a order, so see the sorting of requires...
		
		for resource in self.requires:
			if not resource in self.to_stage: continue
			for item in self.to_stage[resource]:
				self.stage.add_actor(self.objects[resource][item])
