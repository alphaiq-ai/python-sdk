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


class InlineResponse20012ConsumerProductsAndServices(object):
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
        'apparel_and_accessories': 'list[str]',
        'consumer_equipment_and_services': 'list[str]',
        'consumer_transportation_products_and_services': 'list[str]',
        'household_and_personal_care_products': 'list[str]'
    }

    attribute_map = {
        'apparel_and_accessories': 'Apparel and Accessories',
        'consumer_equipment_and_services': 'Consumer Equipment and Services',
        'consumer_transportation_products_and_services': 'Consumer Transportation Products and Services',
        'household_and_personal_care_products': 'Household and Personal Care Products'
    }

    def __init__(self, apparel_and_accessories=None, consumer_equipment_and_services=None, consumer_transportation_products_and_services=None, household_and_personal_care_products=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20012ConsumerProductsAndServices - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._apparel_and_accessories = None
        self._consumer_equipment_and_services = None
        self._consumer_transportation_products_and_services = None
        self._household_and_personal_care_products = None
        self.discriminator = None

        if apparel_and_accessories is not None:
            self.apparel_and_accessories = apparel_and_accessories
        if consumer_equipment_and_services is not None:
            self.consumer_equipment_and_services = consumer_equipment_and_services
        if consumer_transportation_products_and_services is not None:
            self.consumer_transportation_products_and_services = consumer_transportation_products_and_services
        if household_and_personal_care_products is not None:
            self.household_and_personal_care_products = household_and_personal_care_products

    @property
    def apparel_and_accessories(self):
        """Gets the apparel_and_accessories of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501


        :return: The apparel_and_accessories of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._apparel_and_accessories

    @apparel_and_accessories.setter
    def apparel_and_accessories(self, apparel_and_accessories):
        """Sets the apparel_and_accessories of this InlineResponse20012ConsumerProductsAndServices.


        :param apparel_and_accessories: The apparel_and_accessories of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :type: list[str]
        """

        self._apparel_and_accessories = apparel_and_accessories

    @property
    def consumer_equipment_and_services(self):
        """Gets the consumer_equipment_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501


        :return: The consumer_equipment_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._consumer_equipment_and_services

    @consumer_equipment_and_services.setter
    def consumer_equipment_and_services(self, consumer_equipment_and_services):
        """Sets the consumer_equipment_and_services of this InlineResponse20012ConsumerProductsAndServices.


        :param consumer_equipment_and_services: The consumer_equipment_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :type: list[str]
        """

        self._consumer_equipment_and_services = consumer_equipment_and_services

    @property
    def consumer_transportation_products_and_services(self):
        """Gets the consumer_transportation_products_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501


        :return: The consumer_transportation_products_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._consumer_transportation_products_and_services

    @consumer_transportation_products_and_services.setter
    def consumer_transportation_products_and_services(self, consumer_transportation_products_and_services):
        """Sets the consumer_transportation_products_and_services of this InlineResponse20012ConsumerProductsAndServices.


        :param consumer_transportation_products_and_services: The consumer_transportation_products_and_services of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :type: list[str]
        """

        self._consumer_transportation_products_and_services = consumer_transportation_products_and_services

    @property
    def household_and_personal_care_products(self):
        """Gets the household_and_personal_care_products of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501


        :return: The household_and_personal_care_products of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._household_and_personal_care_products

    @household_and_personal_care_products.setter
    def household_and_personal_care_products(self, household_and_personal_care_products):
        """Sets the household_and_personal_care_products of this InlineResponse20012ConsumerProductsAndServices.


        :param household_and_personal_care_products: The household_and_personal_care_products of this InlineResponse20012ConsumerProductsAndServices.  # noqa: E501
        :type: list[str]
        """

        self._household_and_personal_care_products = household_and_personal_care_products

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
        if not isinstance(other, InlineResponse20012ConsumerProductsAndServices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20012ConsumerProductsAndServices):
            return True

        return self.to_dict() != other.to_dict()