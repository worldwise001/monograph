from datetime import datetime
from typing import Dict, Any, List

import attr

from monograph.model.schema import CrossRefAttrsSchema


@attr.s(auto_attribs=True)
class ISBNType:
    value: str
    type: str


class ISBNTypeSchema(CrossRefAttrsSchema):
    class Meta:
        target = ISBNType
        register_as_scheme = True


@attr.s(auto_attribs=True)
class ContentDomain:
    domain: List[str]
    crossmark_restriction: bool


class ContentDomainSchema(CrossRefAttrsSchema):
    class Meta:
        target = ContentDomain
        register_as_scheme = True


@attr.s(auto_attribs=True)
class DateParts:
    date_parts: List[List[int]]


class DatePartsSchema(CrossRefAttrsSchema):
    class Meta:
        target = DateParts
        register_as_scheme = True


@attr.s(auto_attribs=True)
class Author:
    given: str
    family: str
    sequence: str
    affiliation: List[str]


class AuthorSchema(CrossRefAttrsSchema):
    class Meta:
        target = Author
        register_as_scheme = True


@attr.s(auto_attribs=True)
class Event:
    name: str
    location: str
    start: DateParts
    end: DateParts


class EventSchema(CrossRefAttrsSchema):
    class Meta:
        target = Event
        register_as_scheme = True


@attr.s(auto_attribs=True)
class Link:
    url: str
    content_type: str
    content_version: str
    intended_application: str


class LinkSchema(CrossRefAttrsSchema):
    class Meta:
        target = Link
        register_as_scheme = True


@attr.s(auto_attribs=True)
class Work:
    indexed: datetime
    reference_count: int
    publisher: str
    isbn_type: List[ISBNType]
    content_domain: ContentDomain
    published_print: DateParts
    doi: str
    type: str
    created: datetime
    source: str
    is_referenced_by_count: int
    title: List[str]
    prefix: str
    author: List[Author]
    member: str
    event: Event
    container_title: List[str]
    link: List[Link]
    deposited: datetime
    score: float
    issued: DateParts
    isbn: List[str]
    references_count: int
    url: str

    def get_simple(self) -> Dict[str, Any]:
        return {}


class WorkSchema(CrossRefAttrsSchema):
    class Meta:
        target = Work
        register_as_scheme = True
