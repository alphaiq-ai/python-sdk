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

import alphaiq_sdk
from alphaiq_sdk.models.inline_response20019 import InlineResponse20019  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse20019(unittest.TestCase):
    """InlineResponse20019 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20019
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response20019.InlineResponse20019()  # noqa: E501
        if include_optional :
            return InlineResponse20019(
                data = '0'
            )
        else :
            return InlineResponse20019(
                data = '0',
        )

    def testInlineResponse20019(self):
        """Test InlineResponse20019"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
