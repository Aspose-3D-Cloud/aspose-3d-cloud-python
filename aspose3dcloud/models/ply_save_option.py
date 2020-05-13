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
from . import SaveOptions

class PlySaveOption(SaveOptions):
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
        'flip_coordinate': 'bool',
        'vertex_element': 'str',
        'position_components': 'list[str]',
        'face_element': 'str',
        'face_property': 'str',
        'file_content_type': 'FileContentType'
    }

    attribute_map = {
        'flip_coordinate': 'FlipCoordinate',
        'vertex_element': 'VertexElement',
        'position_components': 'PositionComponents',
        'face_element': 'FaceElement',
        'face_property': 'FaceProperty',
        'file_content_type': 'FileContentType'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(PlySaveOption.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(PlySaveOption.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, flip_coordinate=None, vertex_element=None, position_components=None, face_element=None, face_property=None, file_content_type=None, **kw):
        super(PlySaveOption, self).__init__(**kw)
		    
        """
        PlySaveOption - a model defined in Swagger
        """

        self.container['flip_coordinate'] = None
        self.container['vertex_element'] = None
        self.container['position_components'] = None
        self.container['face_element'] = None
        self.container['face_property'] = None
        self.container['file_content_type'] = None

        if flip_coordinate is not None:
          self.flip_coordinate = flip_coordinate
        if vertex_element is not None:
          self.vertex_element = vertex_element
        if position_components is not None:
          self.position_components = position_components
        if face_element is not None:
          self.face_element = face_element
        if face_property is not None:
          self.face_property = face_property
        if file_content_type is not None:
          self.file_content_type = file_content_type

    @property
    def flip_coordinate(self):
        """
        Gets the flip_coordinate of this PlySaveOption.
        Flip the coordinate while saving the scene, default value is true.

        :return: The flip_coordinate of this PlySaveOption.
        :rtype: bool
        """
        return self.container['flip_coordinate']

    @flip_coordinate.setter
    def flip_coordinate(self, flip_coordinate):
        """
        Sets the flip_coordinate of this PlySaveOption.
        Flip the coordinate while saving the scene, default value is true.

        :param flip_coordinate: The flip_coordinate of this PlySaveOption.
        :type: bool
        """

        self.container['flip_coordinate'] = flip_coordinate

    @property
    def vertex_element(self):
        """
        Gets the vertex_element of this PlySaveOption.
        The element name for the vertex data, default value is \"vertex\".

        :return: The vertex_element of this PlySaveOption.
        :rtype: str
        """
        return self.container['vertex_element']

    @vertex_element.setter
    def vertex_element(self, vertex_element):
        """
        Sets the vertex_element of this PlySaveOption.
        The element name for the vertex data, default value is \"vertex\".

        :param vertex_element: The vertex_element of this PlySaveOption.
        :type: str
        """

        self.container['vertex_element'] = vertex_element

    @property
    def position_components(self):
        """
        Gets the position_components of this PlySaveOption.
        The component names for position data, default value is (\"x\", \"y\", \"z\")

        :return: The position_components of this PlySaveOption.
        :rtype: list[str]
        """
        return self.container['position_components']

    @position_components.setter
    def position_components(self, position_components):
        """
        Sets the position_components of this PlySaveOption.
        The component names for position data, default value is (\"x\", \"y\", \"z\")

        :param position_components: The position_components of this PlySaveOption.
        :type: list[str]
        """

        self.container['position_components'] = position_components

    @property
    def face_element(self):
        """
        Gets the face_element of this PlySaveOption.
        The element name for the face data, default value is face.

        :return: The face_element of this PlySaveOption.
        :rtype: str
        """
        return self.container['face_element']

    @face_element.setter
    def face_element(self, face_element):
        """
        Sets the face_element of this PlySaveOption.
        The element name for the face data, default value is face.

        :param face_element: The face_element of this PlySaveOption.
        :type: str
        """

        self.container['face_element'] = face_element

    @property
    def face_property(self):
        """
        Gets the face_property of this PlySaveOption.
        The property name for the face data, default value is vertex_index.

        :return: The face_property of this PlySaveOption.
        :rtype: str
        """
        return self.container['face_property']

    @face_property.setter
    def face_property(self, face_property):
        """
        Sets the face_property of this PlySaveOption.
        The property name for the face data, default value is vertex_index.

        :param face_property: The face_property of this PlySaveOption.
        :type: str
        """

        self.container['face_property'] = face_property

    @property
    def file_content_type(self):
        """
        Gets the file_content_type of this PlySaveOption.
        Gets or sets  of the FileContent Style.

        :return: The file_content_type of this PlySaveOption.
        :rtype: FileContentType
        """
        return self.container['file_content_type']

    @file_content_type.setter
    def file_content_type(self, file_content_type):
        """
        Sets the file_content_type of this PlySaveOption.
        Gets or sets  of the FileContent Style.

        :param file_content_type: The file_content_type of this PlySaveOption.
        :type: FileContentType
        """

        self.container['file_content_type'] = file_content_type

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
        if not isinstance(other, PlySaveOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
