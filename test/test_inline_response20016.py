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
from openapi_client.models.inline_response20016 import InlineResponse20016  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20016(unittest.TestCase):
    """InlineResponse20016 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20016
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20016.InlineResponse20016()  # noqa: E501
        if include_optional :
            return InlineResponse20016(
                data = [
                    openapi_client.models.inline_response_200_16_data.inline_response_200_16_data(
                        company1 = openapi_client.models.inline_response_200_16_company1.inline_response_200_16_company1(
                            overallrisk_value = 56, 
                            overallrisk_value_12_w_lag = 56, 
                            overallrisk_value_4_w_lag = 56, 
                            overallrisk_value_52_w_lag = 56, ), 
                        company2 = openapi_client.models.company2.company2(), 
                        company3 = openapi_client.models.inline_response_200_16_company1.inline_response_200_16_company1(
                            overallrisk_value = 56, 
                            overallrisk_value_12_w_lag = 56, 
                            overallrisk_value_4_w_lag = 56, 
                            overallrisk_value_52_w_lag = 56, ), )
                    ]
            )
        else :
            return InlineResponse20016(
                data = [
                    openapi_client.models.inline_response_200_16_data.inline_response_200_16_data(
                        company1 = openapi_client.models.inline_response_200_16_company1.inline_response_200_16_company1(
                            overallrisk_value = 56, 
                            overallrisk_value_12_w_lag = 56, 
                            overallrisk_value_4_w_lag = 56, 
                            overallrisk_value_52_w_lag = 56, ), 
                        company2 = openapi_client.models.company2.company2(), 
                        company3 = openapi_client.models.inline_response_200_16_company1.inline_response_200_16_company1(
                            overallrisk_value = 56, 
                            overallrisk_value_12_w_lag = 56, 
                            overallrisk_value_4_w_lag = 56, 
                            overallrisk_value_52_w_lag = 56, ), )
                    ],
        )

    def testInlineResponse20016(self):
        """Test InlineResponse20016"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
