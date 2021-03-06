#!/usr/bin/env python
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ACR.utils import mail,replaceVars,prepareVars,dicttree
from ACR.components import Component
from ACR.components.interpreter import makeTree
from ACR.errors import *

class Email(Component):
	def generate(self,acenv,conf):
		D=acenv.doDebug
		if D:acenv.debug("START Email.send with: %s",conf)
		content=conf["content"]
		headers={}
		params=conf["params"]
		for h in params:
			headers[h]=params[h].execute(acenv)
			if type(headers[h]) is list:
				headers[h]=", ".join(headers[h])
		if D:acenv.debug("Computed headers: %s",headers)
		content=replaceVars(acenv,content)
		try:
			mail.send(headers,content)
		except Exception,e:
			return {
				"@status":"error",
				"@error":type(e),
				"@message":str(e)
			}
		return {"@status":"ok"}

	def parseAction(self,conf):
		ret={"params":{}}
		try:
			conf["params"]["From"]
		except KeyError:
			raise Error("FromAdressNotSpecified", "'From' should be specified")
		try:
			conf["params"]["To"]
		except KeyError:
			raise Error("ToAdressNotSpecified", "'To' should be specified")
		try:
			conf["params"]["Subject"]
		except KeyError:
			raise Error("SubjectNotSpecified", "'Subject' should be specified")
		# params=conf["params"]
		# for i in params:
		# 	if params[i]:
		# 		params[i]=prepareVars(params[i])
		for i in conf["params"]:
			ret["params"][i]=makeTree(conf["params"][i])
		try:
			ret['content']=prepareVars("".join(conf['content']))
		except:
			raise Error("StringExpected", "Please use CDATA mail content.")
		return ret

def getObject(config):
	return Email(config)
