from datetime import datetime, timezone
from typing import Any, Dict

from marshmallow import pre_load, post_dump
from marshmallow_annotations.ext.attrs import AttrsSchema

SPECIAL_KEYS = ['isbn', 'doi', 'url']


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
            converted = convert_keys_in_dict(data, '-', '_')
            keys = list(converted.keys())
            for key in keys:
                if type(converted[key]) is dict and converted[key].keys() == {'date_parts', 'date_time', 'timestamp'}:
                    converted_date = datetime.fromtimestamp(converted[key]['timestamp'] / 1000, tz=timezone.utc)
                    converted[key] = converted_date.isoformat()
                if key.lower() in SPECIAL_KEYS:
                    converted[key.lower()] = converted[key]
                    del converted[key]
            return converted
        else:
            return data

    @post_dump
    def postdump(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if type(data) is dict:
            converted = convert_keys_in_dict(data, '_', '-')
            keys = list(converted.keys())
            for key in keys:
                if type(converted[key]) is str:
                    try:
                        converted_date = datetime.fromisoformat(converted[key])
                        converted[key] = {
                            'date-parts': [[converted_date.year, converted_date.month, converted_date.day]],
                            'date-time': converted_date.isoformat().replace('+00:00', 'Z'),
                            'timestamp': int(converted_date.timestamp()) * 1000
                        }
                    except ValueError:
                        pass
                if key in SPECIAL_KEYS:
                    converted[key.upper()] = converted[key]
                    del converted[key]
            return converted
        else:
            return data
