import json
import unittest
from unittest import mock

from monograph.app import create_app


class LibraryAPITest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

    def tearDown(self) -> None:
        self.app_ctx.pop()

    @mock.patch('monograph.api.library.CONFIG')
    @mock.patch('monograph.api.library.Members')
    def test_basic_get_success(self, mock_config, mock_members):
        mock_config = {'monograph': {'memberlist': [0]}}
        with self.app.test_client() as c:
            resp = c.get('/api/library')
            self.assertEqual(200, resp.status_code)
            self.assertEqual({'items': []}, json.loads(resp.data))
