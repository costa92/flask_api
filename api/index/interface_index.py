#!/usr/bin/python
# -*- coding: UTF-8 -*

from flask_restful import Resource
from utils.api_version_verify import api_version

class interfaceIndex(Resource):
    def get(self):
        return {'hello': 'world'}