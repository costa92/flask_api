#!/usr/bin/python
# -*- coding: UTF-8 -*

from flask_restful import Api
from api.articles.interface_article import interfaceArticle
from api.index.interface_index import interfaceIndex
api = Api()

api.add_resource(
  interfaceArticle,
  '/article'
)

api.add_resource(
  interfaceIndex,
  '/'
)