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

class STLSaveOption(SaveOptions):
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
        'flip_coordinate_system': 'bool',
        'file_content_type': 'FileContentType'
    }

    attribute_map = {
        'flip_coordinate_system': 'FlipCoordinateSystem',
        'file_content_type': 'FileContentType'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(STLSaveOption.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(STLSaveOption.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, flip_coordinate_system=None, file_content_type=None, **kw):
        super(STLSaveOption, self).__init__(**kw)
		    
        """
        STLSaveOption - a model defined in Swagger
        """

        self.container['flip_coordinate_system'] = None
        self.container['file_content_type'] = None

        if flip_coordinate_system is not None:
          self.flip_coordinate_system = flip_coordinate_system
        if file_content_type is not None:
          self.file_content_type = file_content_type

    @property
    def flip_coordinate_system(self):
        """
        Gets the flip_coordinate_system of this STLSaveOption.
        Gets or sets whether flip coordinate system of control points/normal during exporting.

        :return: The flip_coordinate_system of this STLSaveOption.
        :rtype: bool
        """
        return self.container['flip_coordinate_system']

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, flip_coordinate_system):
        """
        Sets the flip_coordinate_system of this STLSaveOption.
        Gets or sets whether flip coordinate system of control points/normal during exporting.

        :param flip_coordinate_system: The flip_coordinate_system of this STLSaveOption.
        :type: bool
        """

        self.container['flip_coordinate_system'] = flip_coordinate_system

    @property
    def file_content_type(self):
        """
        Gets the file_content_type of this STLSaveOption.
        Gets or sets  of the FileContent Style.

        :return: The file_content_type of this STLSaveOption.
        :rtype: FileContentType
        """
        return self.container['file_content_type']

    @file_content_type.setter
    def file_content_type(self, file_content_type):
        """
        Sets the file_content_type of this STLSaveOption.
        Gets or sets  of the FileContent Style.

        :param file_content_type: The file_content_type of this STLSaveOption.
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
        if not isinstance(other, STLSaveOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other