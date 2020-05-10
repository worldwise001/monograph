from flask import Blueprint
from flask_restful import Api

from monograph.api.analyze import AnalyzeAPI
from monograph.api.search import SearchAPI


class ApiBlueprint(Blueprint):
    def __init__(self):
        super().__init__('api', __name__, url_prefix='/api')
        self.api = Api(self)
        self.api.add_resource(AnalyzeAPI, '/analyze')
        self.api.add_resource(SearchAPI, '/search')
