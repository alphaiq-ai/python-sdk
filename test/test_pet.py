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
from alphaiq_sdk.models.pet import Pet  # noqa: E501
from alphaiq_sdk.rest import ApiException

class TestPet(unittest.TestCase):
    """Pet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Pet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = alphaiq_sdk.models.pet.Pet()  # noqa: E501
        if include_optional :
            return Pet(
                id = 1, 
                category = alphaiq_sdk.models.category.Category(
                    id = 1, 
                    name = '0', ), 
                name = '0', 
                photo_urls = [
                    '0'
                    ], 
                tags = [
                    alphaiq_sdk.models.tag.Tag(
                        id = 1, 
                        name = '0', )
                    ], 
                status = 'available'
            )
        else :
            return Pet(
                id = 1,
                category = alphaiq_sdk.models.category.Category(
                    id = 1, 
                    name = '0', ),
                name = '0',
                photo_urls = [
                    '0'
                    ],
                tags = [
                    alphaiq_sdk.models.tag.Tag(
                        id = 1, 
                        name = '0', )
                    ],
                status = 'available',
        )

    def testPet(self):
        """Test Pet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
