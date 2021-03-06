# -*- coding: utf-8 -*-

# Asyncode Runtime - XML framework allowing developing internet
# applications without using programming languages.
# Copyright (C) 2008-2010  Adrian Kalbarczyk

# This program is free software: you can redistribute it and/or modify
# it under the terms of the version 3 of GNU General Public License as published by
# the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from ACR.utils import replaceVars,prepareVars,generateID
from ACR.components import *
from hashlib import sha224

class KeyGenerator(Component):
	def generate(self,env,conf):
		#D=env.doDebug
		command=conf["command"]
		if command=="sha2":
			value=replaceVars(env,prepareVars(conf["params"]["value"]))
			return sha224(value).hexdigest()
		return generateID()

def getObject(config):
	return KeyGenerator(config)
