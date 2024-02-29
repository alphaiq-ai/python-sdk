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
from alphaiq_sdk.models.inline_response2002_data import InlineResponse2002Data  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse2002Data(unittest.TestCase):
    """InlineResponse2002Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2002Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response2002_data.InlineResponse2002Data()  # noqa: E501
        if include_optional :
            return InlineResponse2002Data(
                ticker = '0', 
                company_name = '0', 
                questions = [
                    alphaiq_sdk.models.inline_response_200_2_data_questions.inline_response_200_2_data_questions(
                        id = 56, 
                        question_text = '0', 
                        question_response = '0', 
                        question_context = [
                            alphaiq_sdk.models.inline_response_200_2_data_question_context.inline_response_200_2_data_question_context(
                                id = 56, 
                                text = '0', 
                                document_id = '0', 
                                document_section = '0', 
                                document_type = '0', 
                                document_date = '0', 
                                document_link = '0', )
                            ], )
                    ]
            )
        else :
            return InlineResponse2002Data(
                ticker = '0',
                company_name = '0',
                questions = [
                    alphaiq_sdk.models.inline_response_200_2_data_questions.inline_response_200_2_data_questions(
                        id = 56, 
                        question_text = '0', 
                        question_response = '0', 
                        question_context = [
                            alphaiq_sdk.models.inline_response_200_2_data_question_context.inline_response_200_2_data_question_context(
                                id = 56, 
                                text = '0', 
                                document_id = '0', 
                                document_section = '0', 
                                document_type = '0', 
                                document_date = '0', 
                                document_link = '0', )
                            ], )
                    ],
        )

    def testInlineResponse2002Data(self):
        """Test InlineResponse2002Data"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
