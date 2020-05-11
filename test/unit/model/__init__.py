import attr

from monograph.model.schema import CrossRefAttrsSchema


@attr.s(auto_attribs=True)
class SomeField:
    b_field: int


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
