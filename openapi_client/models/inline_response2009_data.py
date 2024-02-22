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


class InlineResponse2009Data(object):
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
        'parent_industry': 'str',
        'highrisk_industries': 'list[InlineResponse2009DataHighriskIndustries]'
    }

    attribute_map = {
        'as_of_date': 'asOfDate',
        'parent_industry': 'parentIndustry',
        'highrisk_industries': 'highriskIndustries'
    }

    def __init__(self, as_of_date=None, parent_industry=None, highrisk_industries=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2009Data - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._as_of_date = None
        self._parent_industry = None
        self._highrisk_industries = None
        self.discriminator = None

        self.as_of_date = as_of_date
        self.parent_industry = parent_industry
        self.highrisk_industries = highrisk_industries

    @property
    def as_of_date(self):
        """Gets the as_of_date of this InlineResponse2009Data.  # noqa: E501


        :return: The as_of_date of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this InlineResponse2009Data.


        :param as_of_date: The as_of_date of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and as_of_date is None:  # noqa: E501
            raise ValueError("Invalid value for `as_of_date`, must not be `None`")  # noqa: E501

        self._as_of_date = as_of_date

    @property
    def parent_industry(self):
        """Gets the parent_industry of this InlineResponse2009Data.  # noqa: E501


        :return: The parent_industry of this InlineResponse2009Data.  # noqa: E501
        :rtype: str
        """
        return self._parent_industry

    @parent_industry.setter
    def parent_industry(self, parent_industry):
        """Sets the parent_industry of this InlineResponse2009Data.


        :param parent_industry: The parent_industry of this InlineResponse2009Data.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent_industry is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_industry`, must not be `None`")  # noqa: E501

        self._parent_industry = parent_industry

    @property
    def highrisk_industries(self):
        """Gets the highrisk_industries of this InlineResponse2009Data.  # noqa: E501


        :return: The highrisk_industries of this InlineResponse2009Data.  # noqa: E501
        :rtype: list[InlineResponse2009DataHighriskIndustries]
        """
        return self._highrisk_industries

    @highrisk_industries.setter
    def highrisk_industries(self, highrisk_industries):
        """Sets the highrisk_industries of this InlineResponse2009Data.


        :param highrisk_industries: The highrisk_industries of this InlineResponse2009Data.  # noqa: E501
        :type: list[InlineResponse2009DataHighriskIndustries]
        """
        if self.local_vars_configuration.client_side_validation and highrisk_industries is None:  # noqa: E501
            raise ValueError("Invalid value for `highrisk_industries`, must not be `None`")  # noqa: E501

        self._highrisk_industries = highrisk_industries

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
        if not isinstance(other, InlineResponse2009Data):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2009Data):
            return True

        return self.to_dict() != other.to_dict()
