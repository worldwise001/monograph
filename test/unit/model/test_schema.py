import unittest
from datetime import datetime

from test.unit.model import SomeFieldSchema, SomeModelSchema, SomeField, SomeModel, SomeDateTimeFieldSchema, \
    SomeDateTimeField


class SchemaTest(unittest.TestCase):
    def test_simple_serialization(self) -> None:
        blob = '{"ISBN": 123}'
        schema = SomeFieldSchema(strict=True)
        test = schema.loads(blob).data
        self.assertEqual(123, test.isbn)

    def test_complex_serialization(self) -> None:
        blob = '{"a-field": "test", "another-field": {"ISBN": 123}}'
        schema = SomeModelSchema(strict=True)
        test = schema.loads(blob).data
        self.assertEqual("test", test.a_field)
        self.assertEqual(123, test.another_field.isbn)

    def test_simple_deserialization(self) -> None:
        test = SomeField(isbn=123)
        schema = SomeFieldSchema(strict=True)
        blob = schema.dump(test).data
        self.assertEqual({"ISBN": 123}, blob)

    def test_complex_deserialization(self) -> None:
        test = SomeModel(a_field="test", another_field=SomeField(isbn=123))
        schema = SomeModelSchema(strict=True)
        blob = schema.dump(test).data
        self.assertEqual({"another-field": {"ISBN": 123}, "a-field": "test"}, blob)

    def test_complex_date_serialization(self) -> None:
        blob = '{"a-date": {"date-parts": [[2013,11,11]],"date-time": "2013-11-11T17:22:24Z",' \
               '"timestamp": 1384190544000}}'
        schema = SomeDateTimeFieldSchema(strict=True)
        test = schema.loads(blob).data
        self.assertEqual(datetime(2013, 11, 11, 17, 22, 24), test.a_date)

    def test_complex_date_deserialization(self) -> None:
        test = SomeDateTimeField(a_date=datetime(2013, 11, 11, 17, 22, 24))
        schema = SomeDateTimeFieldSchema(strict=True)
        blob = schema.dump(test).data
        self.assertEqual({'a-date': {'date-parts': [[2013, 11, 11]],
                                     'date-time': '2013-11-11T17:22:24Z',
                                     'timestamp': 1384190544000}}, blob)
