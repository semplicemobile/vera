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
# This file contains the main view.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os

import vera.core.applications as applications

import vera.core.objects.launcher as launcher 

import vera.core.view

from vera.core.scaling import getNewSize, WIDTH, HEIGHT

class View(vera.core.view.View):
	
	requires = ("main/wallpaper","main/minilauncher",)
	retrieve = {"main/wallpaper": ("wallpaper",),
				"main/minilauncher": ("minilauncher",)}
	to_stage = {"main/wallpaper": ("wallpaper",),
				"main/minilauncher": ("minilauncher",)}

	def build_minilauncher(self):
		"""Builds the minilauncher buttons"""
		
		directory = os.path.expanduser(self.settings["minilauncher_dir"])
		
		if not os.path.exists(directory):
			os.makedirs(directory)
			return
		
		for application in applications.getGroup(directory):
			self.objects["main/minilauncher"]["minilauncher"].add_child(
				launcher.Button(application.getIcon(), application.getExec())
			)
		

	def ready(self):
		
		# Do nice shortcuts...
		wallpaper = self.objects["main/wallpaper"]
		minilauncher = self.objects["main/minilauncher"]
		
		self.build_minilauncher()
		
		# We need to position down the minilauncher.
		buttonsize = getNewSize(launcher.BUTTONSIZE, 0)[0]
		newsize = HEIGHT - buttonsize
		minilauncher["minilauncher"].set_y(newsize)
