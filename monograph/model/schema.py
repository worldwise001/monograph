from typing import Any, Dict

from marshmallow import pre_load, post_dump
from marshmallow_annotations.ext.attrs import AttrsSchema


def convert_keys_in_dict(data: Dict[str, Any], char_from: str, char_to: str) -> Dict[str, Any]:
    new_data = {}
    for key in data.keys():
        new_key = key.replace(char_from, char_to)
        if type(data[key]) is dict:
            new_data[new_key] = convert_keys_in_dict(data[key], char_from, char_to)
        else:
            new_data[new_key] = data[key]
    return new_data


class CrossRefAttrsSchema(AttrsSchema):
    @pre_load
    def preload(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if type(data) is dict:
            return convert_keys_in_dict(data, '-', '_')
        else:
            return data

    @post_dump
    def postdump(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if type(data) is dict:
            return convert_keys_in_dict(data, '_', '-')
        else:
            return data
