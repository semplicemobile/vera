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
# This file contains the config core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

import os, ConfigParser
import vera.core.goodies as goodies

CONFIGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../config")
if not os.path.exists(CONFIGDIR):
	CONFIGDIR = "/etc/vera"

class Configuration(ConfigParser.SafeConfigParser):
	def __init__(self, config):
		
		ConfigParser.SafeConfigParser.__init__(self)
		self.read(os.path.join(CONFIGDIR, config + ".conf"))
	
	def parse_value(self, value):
		"""Properly casts types if it needs to do so."""
		
		if goodies.is_float(value):
			return float(value)
		elif goodies.is_int(value):
			return int(value)
		elif goodies.is_bool(value):
			return bool(value.capitalize())
		else:
			return value
	
	def to_dict(self, section):
		"""Turns section into a dictionary."""
		
		dct = {}
		
		for name, value in self.items(section):
			dct[name] = self.parse_value(value)
		
		return dct
