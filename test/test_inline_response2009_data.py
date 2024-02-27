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
from openapi_client.models.inline_response2009_data import InlineResponse2009Data  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2009Data(unittest.TestCase):
    """InlineResponse2009Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2009Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2009_data.InlineResponse2009Data()  # noqa: E501
        if include_optional :
            return InlineResponse2009Data(
                as_of_date = '0', 
                parent_industry = '0', 
                highrisk_industries = [
                    openapi_client.models.inline_response_200_9_data_highrisk_industries.inline_response_200_9_data_highriskIndustries(
                        lvl4_industry_name = '0', 
                        lvl3_industry_name = '0', 
                        overallrisk_value = 56, 
                        overallrisk_change_4_w = 56, )
                    ]
            )
        else :
            return InlineResponse2009Data(
                as_of_date = '0',
                parent_industry = '0',
                highrisk_industries = [
                    openapi_client.models.inline_response_200_9_data_highrisk_industries.inline_response_200_9_data_highriskIndustries(
                        lvl4_industry_name = '0', 
                        lvl3_industry_name = '0', 
                        overallrisk_value = 56, 
                        overallrisk_change_4_w = 56, )
                    ],
        )

    def testInlineResponse2009Data(self):
        """Test InlineResponse2009Data"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
