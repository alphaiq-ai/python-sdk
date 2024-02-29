# coding: utf-8

"""
    AlphaIQ API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from alphaiq_sdk.configuration import Configuration


class InlineResponse2008DataFinancialsDrillDownIndustriesDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'real_estate': 'InlineResponse2008DataFinancialsRealEstate'
    }

    attribute_map = {
        'real_estate': 'Real Estate'
    }

    def __init__(self, real_estate=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2008DataFinancialsDrillDownIndustriesDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._real_estate = None
        self.discriminator = None

        if real_estate is not None:
            self.real_estate = real_estate

    @property
    def real_estate(self):
        """Gets the real_estate of this InlineResponse2008DataFinancialsDrillDownIndustriesDetails.  # noqa: E501


        :return: The real_estate of this InlineResponse2008DataFinancialsDrillDownIndustriesDetails.  # noqa: E501
        :rtype: InlineResponse2008DataFinancialsRealEstate
        """
        return self._real_estate

    @real_estate.setter
    def real_estate(self, real_estate):
        """Sets the real_estate of this InlineResponse2008DataFinancialsDrillDownIndustriesDetails.


        :param real_estate: The real_estate of this InlineResponse2008DataFinancialsDrillDownIndustriesDetails.  # noqa: E501
        :type: InlineResponse2008DataFinancialsRealEstate
        """

        self._real_estate = real_estate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2008DataFinancialsDrillDownIndustriesDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2008DataFinancialsDrillDownIndustriesDetails):
            return True

        return self.to_dict() != other.to_dict()