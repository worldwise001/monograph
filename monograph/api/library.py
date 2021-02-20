from typing import Dict, Any

from crossref.restful import Members
from flask_restful import Resource

from monograph import ETIQUETTE, CONFIG
from monograph.model.member import MemberSchema


class LibraryAPI(Resource):
    def __init__(self) -> None:
        self.members = Members(etiquette=ETIQUETTE)
        self.schema = MemberSchema(many=True, strict=True)

    def get(self) -> Dict[str, Any]:
        members = []
        member_ids = CONFIG['monograph'].get('memberlist')
        for member_id in member_ids:
            members.append(self.members.member(member_id=member_id))
        parsed_members = [member.get_simple() for member in self.schema.load(members).data]
        return {'items': parsed_members}
