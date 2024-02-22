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


class InlineResponse20027Data(object):
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
        'ticker': 'str',
        'cik': 'str',
        'company_name': 'str'
    }

    attribute_map = {
        'ticker': 'ticker',
        'cik': 'cik',
        'company_name': 'companyName'
    }

    def __init__(self, ticker=None, cik=None, company_name=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20027Data - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ticker = None
        self._cik = None
        self._company_name = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if cik is not None:
            self.cik = cik
        if company_name is not None:
            self.company_name = company_name

    @property
    def ticker(self):
        """Gets the ticker of this InlineResponse20027Data.  # noqa: E501


        :return: The ticker of this InlineResponse20027Data.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this InlineResponse20027Data.


        :param ticker: The ticker of this InlineResponse20027Data.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def cik(self):
        """Gets the cik of this InlineResponse20027Data.  # noqa: E501


        :return: The cik of this InlineResponse20027Data.  # noqa: E501
        :rtype: str
        """
        return self._cik

    @cik.setter
    def cik(self, cik):
        """Sets the cik of this InlineResponse20027Data.


        :param cik: The cik of this InlineResponse20027Data.  # noqa: E501
        :type: str
        """

        self._cik = cik

    @property
    def company_name(self):
        """Gets the company_name of this InlineResponse20027Data.  # noqa: E501


        :return: The company_name of this InlineResponse20027Data.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this InlineResponse20027Data.


        :param company_name: The company_name of this InlineResponse20027Data.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

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
        if not isinstance(other, InlineResponse20027Data):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20027Data):
            return True

        return self.to_dict() != other.to_dict()
