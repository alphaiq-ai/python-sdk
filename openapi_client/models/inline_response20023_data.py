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


class InlineResponse20023Data(object):
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
        'date': 'str',
        'ticker': 'str',
        'signal_id': 'str',
        'signal_value': 'int'
    }

    attribute_map = {
        'date': 'date',
        'ticker': 'ticker',
        'signal_id': 'signalId',
        'signal_value': 'signalValue'
    }

    def __init__(self, date=None, ticker=None, signal_id=None, signal_value=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20023Data - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._ticker = None
        self._signal_id = None
        self._signal_value = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if ticker is not None:
            self.ticker = ticker
        if signal_id is not None:
            self.signal_id = signal_id
        if signal_value is not None:
            self.signal_value = signal_value

    @property
    def date(self):
        """Gets the date of this InlineResponse20023Data.  # noqa: E501


        :return: The date of this InlineResponse20023Data.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InlineResponse20023Data.


        :param date: The date of this InlineResponse20023Data.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def ticker(self):
        """Gets the ticker of this InlineResponse20023Data.  # noqa: E501


        :return: The ticker of this InlineResponse20023Data.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this InlineResponse20023Data.


        :param ticker: The ticker of this InlineResponse20023Data.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def signal_id(self):
        """Gets the signal_id of this InlineResponse20023Data.  # noqa: E501


        :return: The signal_id of this InlineResponse20023Data.  # noqa: E501
        :rtype: str
        """
        return self._signal_id

    @signal_id.setter
    def signal_id(self, signal_id):
        """Sets the signal_id of this InlineResponse20023Data.


        :param signal_id: The signal_id of this InlineResponse20023Data.  # noqa: E501
        :type: str
        """

        self._signal_id = signal_id

    @property
    def signal_value(self):
        """Gets the signal_value of this InlineResponse20023Data.  # noqa: E501


        :return: The signal_value of this InlineResponse20023Data.  # noqa: E501
        :rtype: int
        """
        return self._signal_value

    @signal_value.setter
    def signal_value(self, signal_value):
        """Sets the signal_value of this InlineResponse20023Data.


        :param signal_value: The signal_value of this InlineResponse20023Data.  # noqa: E501
        :type: int
        """

        self._signal_value = signal_value

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
        if not isinstance(other, InlineResponse20023Data):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20023Data):
            return True

        return self.to_dict() != other.to_dict()
