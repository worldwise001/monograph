from typing import Any, Dict, cast
from urllib.parse import unquote

from crossref.restful import Works
from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from monograph import ETIQUETTE, CONFIG
from monograph.model.work import WorkSchema


class SearchAPI(Resource):
    def __init__(self) -> None:
        self.works = Works(etiquette=ETIQUETTE)
        self.work_schema = WorkSchema(strict=True)
        self.sort_map = {'Score': 'score', 'Published': 'published', 'Citations': 'is-referenced-by-count'}
        self.limit_map = {'10': 10, '20': 20, '50': 50, '100': 100}

    def get(self) -> Dict[str, Any]:
        query = request.args.get('q')
        if not query:
            raise BadRequest('need to specify query')
        sort = self.sort_map.get(cast(str, request.args.get('sort')), 'score')
        limit = self.limit_map.get(cast(str, request.args.get('limit')), 10)

        w = self.works
        for member in CONFIG['monograph'].get('memberlist'):
            w = w.filter(member=member)
        w = w.query(query).sort(sort)
        url = unquote(w.url)
        total = w.count()
        results = []
        for work in w:
            results.append(self.work_schema.load(work).data.get_simple())
            if len(results) >= limit:
                break
        return {'items': results, 'total': total, 'url': url}
