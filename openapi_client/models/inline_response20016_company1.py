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


class InlineResponse20016Company1(object):
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
        'overallrisk_value': 'int',
        'overallrisk_value_12_w_lag': 'int',
        'overallrisk_value_4_w_lag': 'int',
        'overallrisk_value_52_w_lag': 'int'
    }

    attribute_map = {
        'overallrisk_value': 'OVERALLRISK-VALUE',
        'overallrisk_value_12_w_lag': 'OVERALLRISK-VALUE_12W_LAG',
        'overallrisk_value_4_w_lag': 'OVERALLRISK-VALUE_4W_LAG',
        'overallrisk_value_52_w_lag': 'OVERALLRISK-VALUE_52W_LAG'
    }

    def __init__(self, overallrisk_value=None, overallrisk_value_12_w_lag=None, overallrisk_value_4_w_lag=None, overallrisk_value_52_w_lag=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20016Company1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overallrisk_value = None
        self._overallrisk_value_12_w_lag = None
        self._overallrisk_value_4_w_lag = None
        self._overallrisk_value_52_w_lag = None
        self.discriminator = None

        self.overallrisk_value = overallrisk_value
        self.overallrisk_value_12_w_lag = overallrisk_value_12_w_lag
        self.overallrisk_value_4_w_lag = overallrisk_value_4_w_lag
        self.overallrisk_value_52_w_lag = overallrisk_value_52_w_lag

    @property
    def overallrisk_value(self):
        """Gets the overallrisk_value of this InlineResponse20016Company1.  # noqa: E501


        :return: The overallrisk_value of this InlineResponse20016Company1.  # noqa: E501
        :rtype: int
        """
        return self._overallrisk_value

    @overallrisk_value.setter
    def overallrisk_value(self, overallrisk_value):
        """Sets the overallrisk_value of this InlineResponse20016Company1.


        :param overallrisk_value: The overallrisk_value of this InlineResponse20016Company1.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and overallrisk_value is None:  # noqa: E501
            raise ValueError("Invalid value for `overallrisk_value`, must not be `None`")  # noqa: E501

        self._overallrisk_value = overallrisk_value

    @property
    def overallrisk_value_12_w_lag(self):
        """Gets the overallrisk_value_12_w_lag of this InlineResponse20016Company1.  # noqa: E501


        :return: The overallrisk_value_12_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :rtype: int
        """
        return self._overallrisk_value_12_w_lag

    @overallrisk_value_12_w_lag.setter
    def overallrisk_value_12_w_lag(self, overallrisk_value_12_w_lag):
        """Sets the overallrisk_value_12_w_lag of this InlineResponse20016Company1.


        :param overallrisk_value_12_w_lag: The overallrisk_value_12_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and overallrisk_value_12_w_lag is None:  # noqa: E501
            raise ValueError("Invalid value for `overallrisk_value_12_w_lag`, must not be `None`")  # noqa: E501

        self._overallrisk_value_12_w_lag = overallrisk_value_12_w_lag

    @property
    def overallrisk_value_4_w_lag(self):
        """Gets the overallrisk_value_4_w_lag of this InlineResponse20016Company1.  # noqa: E501


        :return: The overallrisk_value_4_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :rtype: int
        """
        return self._overallrisk_value_4_w_lag

    @overallrisk_value_4_w_lag.setter
    def overallrisk_value_4_w_lag(self, overallrisk_value_4_w_lag):
        """Sets the overallrisk_value_4_w_lag of this InlineResponse20016Company1.


        :param overallrisk_value_4_w_lag: The overallrisk_value_4_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and overallrisk_value_4_w_lag is None:  # noqa: E501
            raise ValueError("Invalid value for `overallrisk_value_4_w_lag`, must not be `None`")  # noqa: E501

        self._overallrisk_value_4_w_lag = overallrisk_value_4_w_lag

    @property
    def overallrisk_value_52_w_lag(self):
        """Gets the overallrisk_value_52_w_lag of this InlineResponse20016Company1.  # noqa: E501


        :return: The overallrisk_value_52_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :rtype: int
        """
        return self._overallrisk_value_52_w_lag

    @overallrisk_value_52_w_lag.setter
    def overallrisk_value_52_w_lag(self, overallrisk_value_52_w_lag):
        """Sets the overallrisk_value_52_w_lag of this InlineResponse20016Company1.


        :param overallrisk_value_52_w_lag: The overallrisk_value_52_w_lag of this InlineResponse20016Company1.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and overallrisk_value_52_w_lag is None:  # noqa: E501
            raise ValueError("Invalid value for `overallrisk_value_52_w_lag`, must not be `None`")  # noqa: E501

        self._overallrisk_value_52_w_lag = overallrisk_value_52_w_lag

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
        if not isinstance(other, InlineResponse20016Company1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20016Company1):
            return True

        return self.to_dict() != other.to_dict()
