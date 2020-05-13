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


class Sphere(object):
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
        'name': 'str',
        'width_segments': 'int',
        'height_segments': 'int',
        'phi_start': 'float',
        'phi_length': 'float',
        'theta_start': 'float',
        'theta_length': 'float',
        'radius': 'float'
    }

    attribute_map = {
        'name': 'Name',
        'width_segments': 'WidthSegments',
        'height_segments': 'HeightSegments',
        'phi_start': 'PhiStart',
        'phi_length': 'PhiLength',
        'theta_start': 'ThetaStart',
        'theta_length': 'ThetaLength',
        'radius': 'Radius'
    }
    
    @staticmethod
    def get_swagger_types():
        return Sphere.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Sphere.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, name=None, width_segments=None, height_segments=None, phi_start=None, phi_length=None, theta_start=None, theta_length=None, radius=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Sphere - a model defined in Swagger
        """

        self.container['name'] = None
        self.container['width_segments'] = None
        self.container['height_segments'] = None
        self.container['phi_start'] = None
        self.container['phi_length'] = None
        self.container['theta_start'] = None
        self.container['theta_length'] = None
        self.container['radius'] = None

        if name is not None:
          self.name = name
        self.width_segments = width_segments
        self.height_segments = height_segments
        self.phi_start = phi_start
        self.phi_length = phi_length
        self.theta_start = theta_start
        self.theta_length = theta_length
        self.radius = radius

    @property
    def name(self):
        """
        Gets the name of this Sphere.
        Gets or sets the Name of Sphere.

        :return: The name of this Sphere.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Sphere.
        Gets or sets the Name of Sphere.

        :param name: The name of this Sphere.
        :type: str
        """

        self.container['name'] = name

    @property
    def width_segments(self):
        """
        Gets the width_segments of this Sphere.
        Gets or sets the width segments.

        :return: The width_segments of this Sphere.
        :rtype: int
        """
        return self.container['width_segments']

    @width_segments.setter
    def width_segments(self, width_segments):
        """
        Sets the width_segments of this Sphere.
        Gets or sets the width segments.

        :param width_segments: The width_segments of this Sphere.
        :type: int
        """
        """
        if width_segments is None:
            raise ValueError("Invalid value for `width_segments`, must not be `None`")
        """

        self.container['width_segments'] = width_segments

    @property
    def height_segments(self):
        """
        Gets the height_segments of this Sphere.
        Gets or sets the height segments.             

        :return: The height_segments of this Sphere.
        :rtype: int
        """
        return self.container['height_segments']

    @height_segments.setter
    def height_segments(self, height_segments):
        """
        Sets the height_segments of this Sphere.
        Gets or sets the height segments.             

        :param height_segments: The height_segments of this Sphere.
        :type: int
        """
        """
        if height_segments is None:
            raise ValueError("Invalid value for `height_segments`, must not be `None`")
        """

        self.container['height_segments'] = height_segments

    @property
    def phi_start(self):
        """
        Gets the phi_start of this Sphere.
        Gets or sets the phi start.             

        :return: The phi_start of this Sphere.
        :rtype: float
        """
        return self.container['phi_start']

    @phi_start.setter
    def phi_start(self, phi_start):
        """
        Sets the phi_start of this Sphere.
        Gets or sets the phi start.             

        :param phi_start: The phi_start of this Sphere.
        :type: float
        """
        """
        if phi_start is None:
            raise ValueError("Invalid value for `phi_start`, must not be `None`")
        """

        self.container['phi_start'] = phi_start

    @property
    def phi_length(self):
        """
        Gets the phi_length of this Sphere.
        Gets or sets the length of the phi.

        :return: The phi_length of this Sphere.
        :rtype: float
        """
        return self.container['phi_length']

    @phi_length.setter
    def phi_length(self, phi_length):
        """
        Sets the phi_length of this Sphere.
        Gets or sets the length of the phi.

        :param phi_length: The phi_length of this Sphere.
        :type: float
        """
        """
        if phi_length is None:
            raise ValueError("Invalid value for `phi_length`, must not be `None`")
        """

        self.container['phi_length'] = phi_length

    @property
    def theta_start(self):
        """
        Gets the theta_start of this Sphere.
        Gets or sets the theta start.             

        :return: The theta_start of this Sphere.
        :rtype: float
        """
        return self.container['theta_start']

    @theta_start.setter
    def theta_start(self, theta_start):
        """
        Sets the theta_start of this Sphere.
        Gets or sets the theta start.             

        :param theta_start: The theta_start of this Sphere.
        :type: float
        """
        """
        if theta_start is None:
            raise ValueError("Invalid value for `theta_start`, must not be `None`")
        """

        self.container['theta_start'] = theta_start

    @property
    def theta_length(self):
        """
        Gets the theta_length of this Sphere.
        Gets or sets the length of the theta.

        :return: The theta_length of this Sphere.
        :rtype: float
        """
        return self.container['theta_length']

    @theta_length.setter
    def theta_length(self, theta_length):
        """
        Sets the theta_length of this Sphere.
        Gets or sets the length of the theta.

        :param theta_length: The theta_length of this Sphere.
        :type: float
        """
        """
        if theta_length is None:
            raise ValueError("Invalid value for `theta_length`, must not be `None`")
        """

        self.container['theta_length'] = theta_length

    @property
    def radius(self):
        """
        Gets the radius of this Sphere.
        Gets or sets the radius 

        :return: The radius of this Sphere.
        :rtype: float
        """
        return self.container['radius']

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of this Sphere.
        Gets or sets the radius 

        :param radius: The radius of this Sphere.
        :type: float
        """
        """
        if radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")
        """

        self.container['radius'] = radius

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
        if not isinstance(other, Sphere):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
