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


class InlineResponse2002DataQuestionContext(object):
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
        'id': 'int',
        'text': 'str',
        'document_id': 'str',
        'document_section': 'str',
        'document_type': 'str',
        'document_date': 'str',
        'document_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'document_id': 'document_id',
        'document_section': 'document_section',
        'document_type': 'document_type',
        'document_date': 'document_date',
        'document_link': 'document_link'
    }

    def __init__(self, id=None, text=None, document_id=None, document_section=None, document_type=None, document_date=None, document_link=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2002DataQuestionContext - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._text = None
        self._document_id = None
        self._document_section = None
        self._document_type = None
        self._document_date = None
        self._document_link = None
        self.discriminator = None

        self.id = id
        self.text = text
        self.document_id = document_id
        self.document_section = document_section
        self.document_type = document_type
        self.document_date = document_date
        self.document_link = document_link

    @property
    def id(self):
        """Gets the id of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The id of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2002DataQuestionContext.


        :param id: The id of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def text(self):
        """Gets the text of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The text of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InlineResponse2002DataQuestionContext.


        :param text: The text of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def document_id(self):
        """Gets the document_id of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The document_id of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this InlineResponse2002DataQuestionContext.


        :param document_id: The document_id of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def document_section(self):
        """Gets the document_section of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The document_section of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._document_section

    @document_section.setter
    def document_section(self, document_section):
        """Sets the document_section of this InlineResponse2002DataQuestionContext.


        :param document_section: The document_section of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_section is None:  # noqa: E501
            raise ValueError("Invalid value for `document_section`, must not be `None`")  # noqa: E501

        self._document_section = document_section

    @property
    def document_type(self):
        """Gets the document_type of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The document_type of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this InlineResponse2002DataQuestionContext.


        :param document_type: The document_type of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_type is None:  # noqa: E501
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

    @property
    def document_date(self):
        """Gets the document_date of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The document_date of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this InlineResponse2002DataQuestionContext.


        :param document_date: The document_date of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_date is None:  # noqa: E501
            raise ValueError("Invalid value for `document_date`, must not be `None`")  # noqa: E501

        self._document_date = document_date

    @property
    def document_link(self):
        """Gets the document_link of this InlineResponse2002DataQuestionContext.  # noqa: E501


        :return: The document_link of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :rtype: str
        """
        return self._document_link

    @document_link.setter
    def document_link(self, document_link):
        """Sets the document_link of this InlineResponse2002DataQuestionContext.


        :param document_link: The document_link of this InlineResponse2002DataQuestionContext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_link is None:  # noqa: E501
            raise ValueError("Invalid value for `document_link`, must not be `None`")  # noqa: E501

        self._document_link = document_link

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
        if not isinstance(other, InlineResponse2002DataQuestionContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2002DataQuestionContext):
            return True

        return self.to_dict() != other.to_dict()
