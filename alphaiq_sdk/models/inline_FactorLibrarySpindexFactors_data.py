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


class FactorLibrarySpindexFactorsData(object):
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
        'spindex_name': 'str',
        'spindex_definition': 'str'
    }

    attribute_map = {
        'spindex_name': 'spindexName',
        'spindex_definition': 'spindexDefinition'
    }

    def __init__(self, spindex_name=None, spindex_definition=None, local_vars_configuration=None):  # noqa: E501
        """FactorLibrarySpindexFactorsData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._spindex_name = None
        self._spindex_definition = None
        self.discriminator = None

        if spindex_name is not None:
            self.spindex_name = spindex_name
        if spindex_definition is not None:
            self.spindex_definition = spindex_definition

    @property
    def spindex_name(self):
        """Gets the spindex_name of this FactorLibrarySpindexFactorsData.  # noqa: E501


        :return: The spindex_name of this FactorLibrarySpindexFactorsData.  # noqa: E501
        :rtype: str
        """
        return self._spindex_name

    @spindex_name.setter
    def spindex_name(self, spindex_name):
        """Sets the spindex_name of this FactorLibrarySpindexFactorsData.


        :param spindex_name: The spindex_name of this FactorLibrarySpindexFactorsData.  # noqa: E501
        :type: str
        """

        self._spindex_name = spindex_name

    @property
    def spindex_definition(self):
        """Gets the spindex_definition of this FactorLibrarySpindexFactorsData.  # noqa: E501


        :return: The spindex_definition of this FactorLibrarySpindexFactorsData.  # noqa: E501
        :rtype: str
        """
        return self._spindex_definition

    @spindex_definition.setter
    def spindex_definition(self, spindex_definition):
        """Sets the spindex_definition of this FactorLibrarySpindexFactorsData.


        :param spindex_definition: The spindex_definition of this FactorLibrarySpindexFactorsData.  # noqa: E501
        :type: str
        """

        self._spindex_definition = spindex_definition

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
        if not isinstance(other, FactorLibrarySpindexFactorsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FactorLibrarySpindexFactorsData):
            return True

        return self.to_dict() != other.to_dict()
