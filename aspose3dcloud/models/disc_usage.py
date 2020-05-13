# coding: utf-8

"""
    Aspose.ThreeD Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DiscUsage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'used_size': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'used_size': 'UsedSize',
        'total_size': 'TotalSize'
    }
    
    @staticmethod
    def get_swagger_types():
        return DiscUsage.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return DiscUsage.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, used_size=None, total_size=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        DiscUsage - a model defined in Swagger
        """

        self.container['used_size'] = None
        self.container['total_size'] = None

        self.used_size = used_size
        self.total_size = total_size

    @property
    def used_size(self):
        """
        Gets the used_size of this DiscUsage.
        Application used disc space.

        :return: The used_size of this DiscUsage.
        :rtype: int
        """
        return self.container['used_size']

    @used_size.setter
    def used_size(self, used_size):
        """
        Sets the used_size of this DiscUsage.
        Application used disc space.

        :param used_size: The used_size of this DiscUsage.
        :type: int
        """
        """
        if used_size is None:
            raise ValueError("Invalid value for `used_size`, must not be `None`")
        """

        self.container['used_size'] = used_size

    @property
    def total_size(self):
        """
        Gets the total_size of this DiscUsage.
        Total disc space.

        :return: The total_size of this DiscUsage.
        :rtype: int
        """
        return self.container['total_size']

    @total_size.setter
    def total_size(self, total_size):
        """
        Sets the total_size of this DiscUsage.
        Total disc space.

        :param total_size: The total_size of this DiscUsage.
        :type: int
        """
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")
        """

        self.container['total_size'] = total_size

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DiscUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
