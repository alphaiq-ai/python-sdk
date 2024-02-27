# coding: utf-8

"""
    AlphaIQ API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.inline_object3 import InlineObject3  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineObject3(unittest.TestCase):
    """InlineObject3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_object3.InlineObject3()  # noqa: E501
        if include_optional :
            return InlineObject3(
                first_name = '0', 
                last_name = '0'
            )
        else :
            return InlineObject3(
                first_name = '0',
                last_name = '0',
        )

    def testInlineObject3(self):
        """Test InlineObject3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
