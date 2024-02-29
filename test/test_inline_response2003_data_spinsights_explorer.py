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
from alphaiq_sdk.models.inline_response2003_data_spinsights_explorer import InlineResponse2003DataSpinsightsExplorer  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse2003DataSpinsightsExplorer(unittest.TestCase):
    """InlineResponse2003DataSpinsightsExplorer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2003DataSpinsightsExplorer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response2003_data_spinsights_explorer.InlineResponse2003DataSpinsightsExplorer()  # noqa: E501
        if include_optional :
            return InlineResponse2003DataSpinsightsExplorer(
                id = 56, 
                factor_name = '0', 
                factor_description = '0', 
                factor_summary = '0'
            )
        else :
            return InlineResponse2003DataSpinsightsExplorer(
                id = 56,
                factor_name = '0',
                factor_description = '0',
                factor_summary = '0',
        )

    def testInlineResponse2003DataSpinsightsExplorer(self):
        """Test InlineResponse2003DataSpinsightsExplorer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
