from http import HTTPStatus
from typing import Tuple, List

from crossref.restful import Journals, Works, Members
from flask_restful import Resource

from monograph import ETIQUETTE


class LibraryAPI(Resource):
    def __init__(self):
        self.members = Members(etiquette=ETIQUETTE)

    def get(self) -> Tuple[List, int]:
        all_iter = self.members.all()
        all = [i for i in all_iter]
        return all, HTTPStatus.OK
