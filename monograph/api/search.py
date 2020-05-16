from typing import Any, Dict, Tuple

from flask_restful import Resource


class SearchAPI(Resource):
    def get(self) -> Tuple[Dict[str, Any], int]:
        pass
