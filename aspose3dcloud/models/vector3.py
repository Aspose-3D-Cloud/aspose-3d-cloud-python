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


class Vector3(object):
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
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'length2': 'float',
        'length': 'float'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'length2': 'Length2',
        'length': 'Length'
    }
    
    @staticmethod
    def get_swagger_types():
        return Vector3.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Vector3.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, x=None, y=None, z=None, length2=None, length=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Vector3 - a model defined in Swagger
        """

        self.container['x'] = None
        self.container['y'] = None
        self.container['z'] = None
        self.container['length2'] = None
        self.container['length'] = None

        self.x = x
        self.y = y
        self.z = z
        self.length2 = length2
        self.length = length

    @property
    def x(self):
        """
        Gets the x of this Vector3.
        The x component.

        :return: The x of this Vector3.
        :rtype: float
        """
        return self.container['x']

    @x.setter
    def x(self, x):
        """
        Sets the x of this Vector3.
        The x component.

        :param x: The x of this Vector3.
        :type: float
        """
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")
        """

        self.container['x'] = x

    @property
    def y(self):
        """
        Gets the y of this Vector3.
        The y component.

        :return: The y of this Vector3.
        :rtype: float
        """
        return self.container['y']

    @y.setter
    def y(self, y):
        """
        Sets the y of this Vector3.
        The y component.

        :param y: The y of this Vector3.
        :type: float
        """
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")
        """

        self.container['y'] = y

    @property
    def z(self):
        """
        Gets the z of this Vector3.
        The z component.

        :return: The z of this Vector3.
        :rtype: float
        """
        return self.container['z']

    @z.setter
    def z(self, z):
        """
        Sets the z of this Vector3.
        The z component.

        :param z: The z of this Vector3.
        :type: float
        """
        """
        if z is None:
            raise ValueError("Invalid value for `z`, must not be `None`")
        """

        self.container['z'] = z

    @property
    def length2(self):
        """
        Gets the length2 of this Vector3.
        Gets the square of the length.             

        :return: The length2 of this Vector3.
        :rtype: float
        """
        return self.container['length2']

    @length2.setter
    def length2(self, length2):
        """
        Sets the length2 of this Vector3.
        Gets the square of the length.             

        :param length2: The length2 of this Vector3.
        :type: float
        """
        """
        if length2 is None:
            raise ValueError("Invalid value for `length2`, must not be `None`")
        """

        self.container['length2'] = length2

    @property
    def length(self):
        """
        Gets the length of this Vector3.
        Gets the length of this vector.

        :return: The length of this Vector3.
        :rtype: float
        """
        return self.container['length']

    @length.setter
    def length(self, length):
        """
        Sets the length of this Vector3.
        Gets the length of this vector.

        :param length: The length of this Vector3.
        :type: float
        """
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")
        """

        self.container['length'] = length

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
        if not isinstance(other, Vector3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other