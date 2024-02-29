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
from alphaiq_sdk.models.inline_response20022_data import InlineResponse20022Data  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse20022Data(unittest.TestCase):
    """InlineResponse20022Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20022Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response20022_data.InlineResponse20022Data()  # noqa: E501
        if include_optional :
            return InlineResponse20022Data(
                date = '0', 
                ticker = '0', 
                signal_id = '0', 
                signal_value = 56
            )
        else :
            return InlineResponse20022Data(
                date = '0',
                ticker = '0',
                signal_id = '0',
                signal_value = 56,
        )

    def testInlineResponse20022Data(self):
        """Test InlineResponse20022Data"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
