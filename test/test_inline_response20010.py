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
from alphaiq_sdk.models.inline_response20010 import InlineResponse20010  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse20010(unittest.TestCase):
    """InlineResponse20010 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20010
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response20010.InlineResponse20010()  # noqa: E501
        if include_optional :
            return InlineResponse20010(
                data = alphaiq_sdk.models.inline_response_200_10_data.inline_response_200_10_data(
                    as_of_date = '0', 
                    parent_industry = '0', 
                    low_risk_industries = [
                        alphaiq_sdk.models.inline_response_200_9_data_highrisk_industries.inline_response_200_9_data_highriskIndustries(
                            lvl4_industry_name = '0', 
                            lvl3_industry_name = '0', 
                            overallrisk_value = 56, 
                            overallrisk_change_4_w = 56, )
                        ], )
            )
        else :
            return InlineResponse20010(
                data = alphaiq_sdk.models.inline_response_200_10_data.inline_response_200_10_data(
                    as_of_date = '0', 
                    parent_industry = '0', 
                    low_risk_industries = [
                        alphaiq_sdk.models.inline_response_200_9_data_highrisk_industries.inline_response_200_9_data_highriskIndustries(
                            lvl4_industry_name = '0', 
                            lvl3_industry_name = '0', 
                            overallrisk_value = 56, 
                            overallrisk_change_4_w = 56, )
                        ], ),
        )

    def testInlineResponse20010(self):
        """Test InlineResponse20010"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
