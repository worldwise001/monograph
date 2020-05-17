from datetime import datetime
from typing import Optional

import attr

from monograph.model.schema import CrossRefAttrsSchema


@attr.s(auto_attribs=True)
class SomeDateTimeField:
    a_date: Optional[datetime] = None


class SomeDateTimeFieldSchema(CrossRefAttrsSchema):
    class Meta:
        target = SomeDateTimeField
        register_as_scheme = True


@attr.s(auto_attribs=True)
class SomeField:
    isbn: int


class SomeFieldSchema(CrossRefAttrsSchema):
    class Meta:
        target = SomeField
        register_as_scheme = True


@attr.s(auto_attribs=True)
class SomeModel:
    a_field: str
    another_field: SomeField


class SomeModelSchema(CrossRefAttrsSchema):
    class Meta:
        target = SomeModel
        register_as_scheme = True
