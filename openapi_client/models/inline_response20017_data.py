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

from openapi_client.configuration import Configuration


class InlineResponse20017Data(object):
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
        'company_name': 'str',
        'overallrisk': 'int'
    }

    attribute_map = {
        'company_name': 'companyName',
        'overallrisk': 'overallrisk'
    }

    def __init__(self, company_name=None, overallrisk=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20017Data - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company_name = None
        self._overallrisk = None
        self.discriminator = None

        self.company_name = company_name
        self.overallrisk = overallrisk

    @property
    def company_name(self):
        """Gets the company_name of this InlineResponse20017Data.  # noqa: E501


        :return: The company_name of this InlineResponse20017Data.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this InlineResponse20017Data.


        :param company_name: The company_name of this InlineResponse20017Data.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company_name is None:  # noqa: E501
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def overallrisk(self):
        """Gets the overallrisk of this InlineResponse20017Data.  # noqa: E501


        :return: The overallrisk of this InlineResponse20017Data.  # noqa: E501
        :rtype: int
        """
        return self._overallrisk

    @overallrisk.setter
    def overallrisk(self, overallrisk):
        """Sets the overallrisk of this InlineResponse20017Data.


        :param overallrisk: The overallrisk of this InlineResponse20017Data.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and overallrisk is None:  # noqa: E501
            raise ValueError("Invalid value for `overallrisk`, must not be `None`")  # noqa: E501

        self._overallrisk = overallrisk

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
        if not isinstance(other, InlineResponse20017Data):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20017Data):
            return True

        return self.to_dict() != other.to_dict()
