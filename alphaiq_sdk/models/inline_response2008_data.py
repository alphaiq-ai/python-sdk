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


class InlineResponse2008Data(object):
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
        'as_of_date': 'str',
        'industries_details': 'list[InlineResponse2008DataIndustriesDetails]'
    }

    attribute_map = {
        'as_of_date': 'asOfDate',
        'industries_details': 'industriesDetails'
    }

    def __init__(self, as_of_date=None, industries_details=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2008Data - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._as_of_date = None
        self._industries_details = None
        self.discriminator = None

        self.as_of_date = as_of_date
        self.industries_details = industries_details

    @property
    def as_of_date(self):
        """Gets the as_of_date of this InlineResponse2008Data.  # noqa: E501


        :return: The as_of_date of this InlineResponse2008Data.  # noqa: E501
        :rtype: str
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this InlineResponse2008Data.


        :param as_of_date: The as_of_date of this InlineResponse2008Data.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and as_of_date is None:  # noqa: E501
            raise ValueError("Invalid value for `as_of_date`, must not be `None`")  # noqa: E501

        self._as_of_date = as_of_date

    @property
    def industries_details(self):
        """Gets the industries_details of this InlineResponse2008Data.  # noqa: E501


        :return: The industries_details of this InlineResponse2008Data.  # noqa: E501
        :rtype: list[InlineResponse2008DataIndustriesDetails]
        """
        return self._industries_details

    @industries_details.setter
    def industries_details(self, industries_details):
        """Sets the industries_details of this InlineResponse2008Data.


        :param industries_details: The industries_details of this InlineResponse2008Data.  # noqa: E501
        :type: list[InlineResponse2008DataIndustriesDetails]
        """
        if self.local_vars_configuration.client_side_validation and industries_details is None:  # noqa: E501
            raise ValueError("Invalid value for `industries_details`, must not be `None`")  # noqa: E501

        self._industries_details = industries_details

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
        if not isinstance(other, InlineResponse2008Data):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2008Data):
            return True

        return self.to_dict() != other.to_dict()