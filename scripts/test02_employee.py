import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ApiEmployee()

    def test01_post(self, username="bjjj21", mobile="13015214222", workNumber="888"):
        r = self.api.api_post_employee(username, mobile, workNumber)
        api.user_id = r.json().get("data").get("id")
        assert_common(self, r)

    def test04_delete(self):
        r = self.api.api_delete_employee(api.user_id)
        assert_common(self, r)
