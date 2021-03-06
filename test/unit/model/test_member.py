import json
import os
import unittest

from monograph.model.member import MemberSchema
from test import ROOT_DIR


class MemberSchemaTest(unittest.TestCase):
    def test_deserialization(self) -> None:
        with open(os.path.join(ROOT_DIR, 'test', 'member.json')) as fp:
            blob = json.load(fp)
        schema = MemberSchema(strict=True)
        schema.load(blob)  # should not throw an error
