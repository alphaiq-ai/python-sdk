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
from openapi_client.models.inline_response200_data import InlineResponse200Data  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse200Data(unittest.TestCase):
    """InlineResponse200Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse200Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response200_data.InlineResponse200Data()  # noqa: E501
        if include_optional :
            return InlineResponse200Data(
                access_token = '0', 
                challenge_parameters = None, 
                id_token = '0', 
                refresh_token = '0', 
                token_type = '0', 
                expires_in = 56
            )
        else :
            return InlineResponse200Data(
                access_token = '0',
                challenge_parameters = None,
                id_token = '0',
                refresh_token = '0',
                token_type = '0',
                expires_in = 56,
        )

    def testInlineResponse200Data(self):
        """Test InlineResponse200Data"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
