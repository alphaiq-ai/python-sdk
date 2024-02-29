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
from alphaiq_sdk.models.inline_response20026 import InlineResponse20026  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse20026(unittest.TestCase):
    """InlineResponse20026 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20026
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response20026.InlineResponse20026()  # noqa: E501
        if include_optional :
            return InlineResponse20026(
                data = alphaiq_sdk.models.inline_response_200_26_data.inline_response_200_26_data(
                    question_answer = [
                        alphaiq_sdk.models.inline_response_200_26_data_question_answer.inline_response_200_26_data_question_answer(
                            id = 56, 
                            question_text = '0', 
                            question_response = '0', )
                        ], )
            )
        else :
            return InlineResponse20026(
                data = alphaiq_sdk.models.inline_response_200_26_data.inline_response_200_26_data(
                    question_answer = [
                        alphaiq_sdk.models.inline_response_200_26_data_question_answer.inline_response_200_26_data_question_answer(
                            id = 56, 
                            question_text = '0', 
                            question_response = '0', )
                        ], ),
        )

    def testInlineResponse20026(self):
        """Test InlineResponse20026"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
