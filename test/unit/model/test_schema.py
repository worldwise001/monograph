import unittest

from test.unit.model import SomeFieldSchema, SomeModelSchema, SomeField, SomeModel


class SchemaTest(unittest.TestCase):
    def test_simple_serialization(self) -> None:
        blob = '{"b-field": 123}'
        schema = SomeFieldSchema(strict=True)
        test = schema.loads(blob).data
        self.assertEqual(123, test.b_field)

    def test_complex_serialization(self) -> None:
        blob = '{"a-field": "test", "another-field": {"b-field": 123}}'
        schema = SomeModelSchema(strict=True)
        test = schema.loads(blob).data
        self.assertEqual("test", test.a_field)
        self.assertEqual(123, test.another_field.b_field)

    def test_simple_deserialization(self) -> None:
        test = SomeField(b_field=123)
        schema = SomeFieldSchema(strict=True)
        blob = schema.dumps(test).data
        self.assertEqual('{"b-field": 123}', blob)

    def test_complex_deserialization(self) -> None:
        test = SomeModel(a_field="test", another_field=SomeField(b_field=123))
        schema = SomeModelSchema(strict=True)
        blob = schema.dumps(test).data
        self.assertEqual('{"another-field": {"b-field": 123}, "a-field": "test"}', blob)
