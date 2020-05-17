from datetime import datetime
from typing import Dict, Any, List, Optional

import attr
from marshmallow import pre_load

from monograph.model.schema import CrossRefAttrsSchema


@attr.s(auto_attribs=True, kw_only=True)
class ISBNType:
    value: str
    type: str


class ISBNTypeSchema(CrossRefAttrsSchema):
    class Meta:
        target = ISBNType
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class ContentDomain:
    domain: List[str]
    crossmark_restriction: bool


class ContentDomainSchema(CrossRefAttrsSchema):
    class Meta:
        target = ContentDomain
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class DateParts:
    date_parts: List[List[int]] = []


class DatePartsSchema(CrossRefAttrsSchema):
    class Meta:
        target = DateParts
        register_as_scheme = True

    @pre_load
    def preload(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        converted = super().preload(data, **kwargs)
        if converted['date_parts'] == [[None]]:
            converted['date_parts'] = []
        return converted


@attr.s(auto_attribs=True, kw_only=True)
class Affiliation:
    name: str


class AffiliationSchema(CrossRefAttrsSchema):
    class Meta:
        target = Affiliation
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Author:
    family: str
    sequence: str
    given: Optional[str] = None
    affiliation: List[Affiliation] = []


class AuthorSchema(CrossRefAttrsSchema):
    class Meta:
        target = Author
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Event:
    name: str
    location: Optional[str] = None
    start: Optional[DateParts] = None
    end: Optional[DateParts] = None


class EventSchema(CrossRefAttrsSchema):
    class Meta:
        target = Event
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Link:
    url: str
    content_type: str
    content_version: str
    intended_application: str


class LinkSchema(CrossRefAttrsSchema):
    class Meta:
        target = Link
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Reference:
    key: Optional[str] = None
    unstructured: Optional[str] = None
    author: Optional[str] = None
    volume: Optional[str] = None
    volume_title: Optional[str] = None
    year: Optional[str] = None
    doi: Optional[str] = None
    doi_asserted_by: Optional[str] = None
    first_name: Optional[str] = None
    journal_title: Optional[str] = None
    article_title: Optional[str] = None


class ReferenceSchema(CrossRefAttrsSchema):
    class Meta:
        target = Reference
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class Work:
    indexed: datetime
    reference_count: int
    publisher: str
    content_domain: ContentDomain
    type: str
    created: datetime
    source: str
    is_referenced_by_count: int
    title: List[str]
    prefix: str
    member: str
    container_title: List[str]
    deposited: datetime
    score: float
    references_count: int
    url: str
    issued: DateParts
    isbn: List[str] = []
    isbn_type: List[ISBNType] = []
    link: List[Link] = []
    event: Optional[Event] = None
    author: List[Author] = []
    alternative_id: List[str] = []
    publisher_location: Optional[str] = None
    published_online: Optional[DateParts] = None
    published_print: Optional[DateParts] = None
    reference: List[Reference] = []
    doi: Optional[str] = None

    def get_simple(self) -> Dict[str, Any]:
        link: Optional[str] = None
        for entry in self.link:
            if not link or ('xplorestaging' not in entry.url and 'xplorestaging' in link):
                link = entry.url
        if link:
            link = link.replace('xplorestaging', 'ieeexplore')

        return {
            'title': self.title[0] or 'Unknown',
            'doi': self.doi or None,
            'cited_by': self.is_referenced_by_count,
            'year': self.issued.date_parts[0][0]
            if self.issued.date_parts or len(self.issued.date_parts) > 0
            else None,
            'from': self.container_title[0] or None,
            'authors': AuthorSchema(many=True).dump(self.author).data,
            'pdf': link,
            'score': self.score
        }


class WorkSchema(CrossRefAttrsSchema):
    class Meta:
        target = Work
        register_as_scheme = True
