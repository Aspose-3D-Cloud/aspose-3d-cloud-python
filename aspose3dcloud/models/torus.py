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


class Torus(object):
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
        'radius': 'float',
        'tube': 'float',
        'radial_segments': 'int',
        'tubular_segments': 'int',
        'arc': 'float'
    }

    attribute_map = {
        'name': 'Name',
        'radius': 'Radius',
        'tube': 'Tube',
        'radial_segments': 'RadialSegments',
        'tubular_segments': 'TubularSegments',
        'arc': 'Arc'
    }
    
    @staticmethod
    def get_swagger_types():
        return Torus.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Torus.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, name=None, radius=None, tube=None, radial_segments=None, tubular_segments=None, arc=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Torus - a model defined in Swagger
        """

        self.container['name'] = None
        self.container['radius'] = None
        self.container['tube'] = None
        self.container['radial_segments'] = None
        self.container['tubular_segments'] = None
        self.container['arc'] = None

        if name is not None:
          self.name = name
        self.radius = radius
        self.tube = tube
        self.radial_segments = radial_segments
        self.tubular_segments = tubular_segments
        self.arc = arc

    @property
    def name(self):
        """
        Gets the name of this Torus.
        Gets or sets the Name of the torus.

        :return: The name of this Torus.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Torus.
        Gets or sets the Name of the torus.

        :param name: The name of this Torus.
        :type: str
        """

        self.container['name'] = name

    @property
    def radius(self):
        """
        Gets the radius of this Torus.
        Gets or sets the radius of the torus.             

        :return: The radius of this Torus.
        :rtype: float
        """
        return self.container['radius']

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of this Torus.
        Gets or sets the radius of the torus.             

        :param radius: The radius of this Torus.
        :type: float
        """
        """
        if radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")
        """

        self.container['radius'] = radius

    @property
    def tube(self):
        """
        Gets the tube of this Torus.
        Gets or sets the radius of the tube.

        :return: The tube of this Torus.
        :rtype: float
        """
        return self.container['tube']

    @tube.setter
    def tube(self, tube):
        """
        Sets the tube of this Torus.
        Gets or sets the radius of the tube.

        :param tube: The tube of this Torus.
        :type: float
        """
        """
        if tube is None:
            raise ValueError("Invalid value for `tube`, must not be `None`")
        """

        self.container['tube'] = tube

    @property
    def radial_segments(self):
        """
        Gets the radial_segments of this Torus.
        Gets or sets the radial segments.

        :return: The radial_segments of this Torus.
        :rtype: int
        """
        return self.container['radial_segments']

    @radial_segments.setter
    def radial_segments(self, radial_segments):
        """
        Sets the radial_segments of this Torus.
        Gets or sets the radial segments.

        :param radial_segments: The radial_segments of this Torus.
        :type: int
        """
        """
        if radial_segments is None:
            raise ValueError("Invalid value for `radial_segments`, must not be `None`")
        """

        self.container['radial_segments'] = radial_segments

    @property
    def tubular_segments(self):
        """
        Gets the tubular_segments of this Torus.
        Gets or sets the tubular segments.

        :return: The tubular_segments of this Torus.
        :rtype: int
        """
        return self.container['tubular_segments']

    @tubular_segments.setter
    def tubular_segments(self, tubular_segments):
        """
        Sets the tubular_segments of this Torus.
        Gets or sets the tubular segments.

        :param tubular_segments: The tubular_segments of this Torus.
        :type: int
        """
        """
        if tubular_segments is None:
            raise ValueError("Invalid value for `tubular_segments`, must not be `None`")
        """

        self.container['tubular_segments'] = tubular_segments

    @property
    def arc(self):
        """
        Gets the arc of this Torus.
        Gets or sets the arc.

        :return: The arc of this Torus.
        :rtype: float
        """
        return self.container['arc']

    @arc.setter
    def arc(self, arc):
        """
        Sets the arc of this Torus.
        Gets or sets the arc.

        :param arc: The arc of this Torus.
        :type: float
        """
        """
        if arc is None:
            raise ValueError("Invalid value for `arc`, must not be `None`")
        """

        self.container['arc'] = arc

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
        if not isinstance(other, Torus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
