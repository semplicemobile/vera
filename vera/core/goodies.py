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
# This file contains the goodies core library.
#
# Authors:
#     Eugenio "g7" Paolantonio <me@medesimo.eu>

def is_int(num):
	"""Returns True if the string num is an integer, False if not."""
	
	if type(num) == int: return True
	
	if num.strip("+-").isdigit():
		return True
	else:
		return False

def is_float(num):
	"""Returns True if the string num is a float, False if not."""
	
	if type(num) == float: return True
	
	if "." in num and is_int(num.replace(".","", 1)):
		return True
	else:
		return False

def is_bool(string):
	"""Returns True if the string string is a bool, False if not."""
	
	if type(string) == bool: return True
	
	if string.lower() in ("true","false"):
		return True
	else:
		return False
