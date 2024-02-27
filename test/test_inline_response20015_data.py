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
from openapi_client.models.inline_response20015_data import InlineResponse20015Data  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20015Data(unittest.TestCase):
    """InlineResponse20015Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20015Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20015_data.InlineResponse20015Data()  # noqa: E501
        if include_optional :
            return InlineResponse20015Data(
                insecure_value = 56, 
                uncertain_value = 56, 
                evasive_value = 56, 
                operationalrisk_value = 56, 
                financialrisk_value = 56, 
                speculative_value = 56, 
                constrained_value = 56, 
                earningsrisk_value = 56, 
                economicrisk_value = 56, 
                date = '0', 
                overallrisk_value = 56
            )
        else :
            return InlineResponse20015Data(
                insecure_value = 56,
                uncertain_value = 56,
                evasive_value = 56,
                operationalrisk_value = 56,
                financialrisk_value = 56,
                speculative_value = 56,
                constrained_value = 56,
                earningsrisk_value = 56,
                economicrisk_value = 56,
                date = '0',
                overallrisk_value = 56,
        )

    def testInlineResponse20015Data(self):
        """Test InlineResponse20015Data"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
