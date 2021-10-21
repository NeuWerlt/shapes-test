import json

from core.tests import APITestCaseBase
from django.urls import reverse


class TestShape(APITestCaseBase):
    def test_shape(self):
        url = reverse('shapes-list')
        resp = self.client.post(
            url,
            content_type='application/json',
            data=json.dumps({
                "name": "s1",
                "type": "Diamond",
                "parameters": {
                    "diagonal_1": 2,
                    "diagonal_2": 3,
                }
            })
         ).json()

        self.assertTrue(resp['success'])
