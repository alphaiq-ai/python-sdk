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


class FactorLibraryCompassQuestionsData(object):
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
        'question_id': 'str',
        'question_text': 'str'
    }

    attribute_map = {
        'question_id': 'questionId',
        'question_text': 'questionText'
    }

    def __init__(self, question_id=None, question_text=None, local_vars_configuration=None):  # noqa: E501
        """FactorLibraryCompassQuestionsData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._question_id = None
        self._question_text = None
        self.discriminator = None

        if question_id is not None:
            self.question_id = question_id
        if question_text is not None:
            self.question_text = question_text

    @property
    def question_id(self):
        """Gets the question_id of this FactorLibraryCompassQuestionsData.  # noqa: E501


        :return: The question_id of this FactorLibraryCompassQuestionsData.  # noqa: E501
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this FactorLibraryCompassQuestionsData.


        :param question_id: The question_id of this FactorLibraryCompassQuestionsData.  # noqa: E501
        :type: str
        """

        self._question_id = question_id

    @property
    def question_text(self):
        """Gets the question_text of this FactorLibraryCompassQuestionsData.  # noqa: E501


        :return: The question_text of this FactorLibraryCompassQuestionsData.  # noqa: E501
        :rtype: str
        """
        return self._question_text

    @question_text.setter
    def question_text(self, question_text):
        """Sets the question_text of this FactorLibraryCompassQuestionsData.


        :param question_text: The question_text of this FactorLibraryCompassQuestionsData.  # noqa: E501
        :type: str
        """

        self._question_text = question_text

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
        if not isinstance(other, FactorLibraryCompassQuestionsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FactorLibraryCompassQuestionsData):
            return True

        return self.to_dict() != other.to_dict()
