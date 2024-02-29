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
from alphaiq_sdk.models.inline_response2008_data_financials_drill_down_industries_details import InlineResponse2008DataFinancialsDrillDownIndustriesDetails  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestInlineResponse2008DataFinancialsDrillDownIndustriesDetails(unittest.TestCase):
    """InlineResponse2008DataFinancialsDrillDownIndustriesDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2008DataFinancialsDrillDownIndustriesDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.inline_response2008_data_financials_drill_down_industries_details.InlineResponse2008DataFinancialsDrillDownIndustriesDetails()  # noqa: E501
        if include_optional :
            return InlineResponse2008DataFinancialsDrillDownIndustriesDetails(
                real_estate = alphaiq_sdk.models.inline_response_200_8_data_financials_real_estate.inline_response_200_8_data_Financials_Real_Estate(
                    overallrisk_value = 56, 
                    drill_down_industries_details = [
                        alphaiq_sdk.models.inline_response_200_8_data_financials_real_estate_drill_down_industries_details.inline_response_200_8_data_Financials_Real_Estate_drillDownIndustriesDetails(
                            real_estate_rental = alphaiq_sdk.models.inline_response_200_8_data_financials_real_estate_real_estate_rental.inline_response_200_8_data_Financials_Real_Estate_Real_Estate_Rental(
                                overallrisk_value = 56, 
                                high_risk_companies = [
                                    alphaiq_sdk.models.inline_response_200_8_data_financials_real_estate_real_estate_rental_high_risk_companies.inline_response_200_8_data_Financials_Real_Estate_Real_Estate_Rental_highRiskCompanies(
                                        company_name = '0', 
                                        overallrisk_value = 56, )
                                    ], 
                                low_risk_companies = [
                                    alphaiq_sdk.models.inline_response_200_8_data_financials_real_estate_real_estate_rental_high_risk_companies.inline_response_200_8_data_Financials_Real_Estate_Real_Estate_Rental_highRiskCompanies(
                                        company_name = '0', 
                                        overallrisk_value = 56, )
                                    ], ), )
                        ], )
            )
        else :
            return InlineResponse2008DataFinancialsDrillDownIndustriesDetails(
        )

    def testInlineResponse2008DataFinancialsDrillDownIndustriesDetails(self):
        """Test InlineResponse2008DataFinancialsDrillDownIndustriesDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
