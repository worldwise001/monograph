import json
import os
import unittest

from monograph.model.work import WorkSchema
from test import ROOT_DIR


class WorkSchemaTest(unittest.TestCase):
    def test_deserialization(self) -> None:
        with open(os.path.join(ROOT_DIR, 'test', 'work.json')) as fp:
            blob = json.load(fp)
        schema = WorkSchema(strict=True)
        schema.load(blob)  # should not throw an error
