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
from alphaiq_sdk.models.inline_response20025_data_compass_content import InlineResponse20025DataCompassContent  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse20025DataCompassContent(unittest.TestCase):
    """InlineResponse20025DataCompassContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20025DataCompassContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response20025_data_compass_content.InlineResponse20025DataCompassContent()  # noqa: E501
        if include_optional :
            return InlineResponse20025DataCompassContent(
                compass_title = '0', 
                compass_asof_date = '0', 
                executive_summary = '0', 
                trending_up_article = '0', 
                trending_up_topics = '0', 
                popularity_article = '0', 
                popularity_topics = '0', 
                trending_down_article = '0', 
                trending_down_topics = '0'
            )
        else :
            return InlineResponse20025DataCompassContent(
                compass_title = '0',
                compass_asof_date = '0',
                executive_summary = '0',
                trending_up_article = '0',
                trending_up_topics = '0',
                popularity_article = '0',
                popularity_topics = '0',
                trending_down_article = '0',
                trending_down_topics = '0',
        )

    def testInlineResponse20025DataCompassContent(self):
        """Test InlineResponse20025DataCompassContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
