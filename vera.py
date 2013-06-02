#!/usr/bin/env python
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
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import sys, os

import vera.core.config as config
maincfg = config.Configuration("vera")
settings = maincfg.to_dict("vera")
os.environ["VERA_WIDTH"] = str(settings["width"])
os.environ["VERA_HEIGHT"] = str(settings["height"])
os.environ["VERA_SCALING"] = str(settings["scaling"])

import vera.core.scriptLoader as scriptLoader
import vera.views.main as mainView

from gi.repository import Clutter


def _quit(caller=None):
	
	Clutter.main_quit()

class MainStage(Clutter.Stage):
	
	"""The MainStage is the main vera window.
	
	If we are travelling onboard our shiny new A380s is thanks to it ;)"""
	
	def __init__(self):
		"""We only need to set some things on the default stage."""
		
		Clutter.Stage.__init__(self)
		
		self.set_size(settings["width"], settings["height"])
		
		self.connect("destroy", _quit)
		
		self.show()

if __name__ == "__main__":
	Clutter.init(sys.argv)
	
	handler = scriptLoader.ScriptHandler()
	
	ms = MainStage()
	
	# Show the main view
	main = mainView.View(handler, ms, maincfg.to_dict("main"))
	main.ready()
	main.add_to_stage()
	
	Clutter.main()
