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
from openapi_client.models.inline_response20011 import InlineResponse20011  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20011(unittest.TestCase):
    """InlineResponse20011 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20011
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20011.InlineResponse20011()  # noqa: E501
        if include_optional :
            return InlineResponse20011(
                data = openapi_client.models.inline_response_200_11_data.inline_response_200_11_data(
                    lvl2_industries_with_latest_avg_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl2_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl2IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, )
                        ], 
                    lvl3_industries_with_latest_avg_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl3_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl3IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, 
                            parent_industry = '0', )
                        ], 
                    lvl4_industries_with_latest_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl3_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl3IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, 
                            parent_industry = '0', )
                        ], )
            )
        else :
            return InlineResponse20011(
                data = openapi_client.models.inline_response_200_11_data.inline_response_200_11_data(
                    lvl2_industries_with_latest_avg_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl2_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl2IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, )
                        ], 
                    lvl3_industries_with_latest_avg_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl3_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl3IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, 
                            parent_industry = '0', )
                        ], 
                    lvl4_industries_with_latest_overallrisk = [
                        openapi_client.models.inline_response_200_11_data_lvl3_industries_with_latest_avg_overallrisk.inline_response_200_11_data_lvl3IndustriesWithLatestAvgOverallrisk(
                            industry_name = '0', 
                            overallrisk = 56, 
                            parent_industry = '0', )
                        ], ),
        )

    def testInlineResponse20011(self):
        """Test InlineResponse20011"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
