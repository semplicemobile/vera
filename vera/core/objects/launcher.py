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
# This file contains objects useful to the launcher.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os

from vera.core.scaling import getNewSize

from gi.repository import Clutter, Gtk, GObject

icontheme = Gtk.IconTheme.get_default()

BUTTONSIZE = 64

class Button(Clutter.Texture):
	def __init__(self, image, target, size=BUTTONSIZE):
		"""Initialize the class."""
		
		Clutter.Texture.__init__(self)
		
		width, height = getNewSize(size,size)
		self.set_size(width,height)
		
		icon = icontheme.lookup_icon(image,width,Gtk.IconLookupFlags.USE_BUILTIN)
		if icon:
			print icon.get_filename(), width
			self.set_from_file(icon.get_filename())
		
		self.set_reactive(True)
		self.connect("button-press-event", self.on_click, target)
		
		# Create transition
		self.transition = Clutter.PropertyTransition()
		self.transition.set_progress_mode(Clutter.AnimationMode.EASE_OUT_BOUNCE)
		self.transition.set_duration(5000)
		self.transition.set_from(100.0)
		self.transition.set_to(50.0)
		self.transition.set_animatable(self)
		
		self.transition.start()
		

		#self.set_y(self.get_width()/2.0)

		#self.save_easing_state()

		#self.restore_easing_state()
	
	def on_click(self, caller, event, target):
		"""Fired when the button is clicked."""
		
		print "CLICKED!"
		
		GObject.idle_add(self.set_easing_mode, Clutter.AnimationMode.EASE_OUT_BOUNCE)
		GObject.idle_add(self.set_easing_duration, 500)		
		#os.system(target)
