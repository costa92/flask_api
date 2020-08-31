#!/usr/bin/python
# -*- coding: UTF-8 -*
from flask import request
from flask_restful import Resource

class interfaceArticle(Resource):

    def get(self, dpt_id=None):
        return 11