#!/usr/bin/env python

from ACR.utils import json_compat
try:
	from pymongo.json_util import default
except:
	from bson.json_util import default

name="JSON"
def serialize(acenv):
	if not json_compat:
		return "ERROR: JSON serializer not installed"
	#try:
	return json_compat.dumps(acenv.generations,default=default)
	#except:
	#	raise Exception("simplejson module not installed. Can't output JSON.")
