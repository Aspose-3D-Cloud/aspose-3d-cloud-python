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

class ObjSaveOption(SaveOptions):
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
        'verbose': 'bool',
        'serialize_w': 'bool',
        'enable_materials': 'bool',
        'flip_coordinate_system': 'bool'
    }

    attribute_map = {
        'verbose': 'Verbose',
        'serialize_w': 'SerializeW',
        'enable_materials': 'EnableMaterials',
        'flip_coordinate_system': 'FlipCoordinateSystem'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ObjSaveOption.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ObjSaveOption.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, verbose=None, serialize_w=None, enable_materials=None, flip_coordinate_system=None, **kw):
        super(ObjSaveOption, self).__init__(**kw)
		    
        """
        ObjSaveOption - a model defined in Swagger
        """

        self.container['verbose'] = None
        self.container['serialize_w'] = None
        self.container['enable_materials'] = None
        self.container['flip_coordinate_system'] = None

        if verbose is not None:
          self.verbose = verbose
        if serialize_w is not None:
          self.serialize_w = serialize_w
        if enable_materials is not None:
          self.enable_materials = enable_materials
        if flip_coordinate_system is not None:
          self.flip_coordinate_system = flip_coordinate_system

    @property
    def verbose(self):
        """
        Gets the verbose of this ObjSaveOption.
        Gets or sets whether generate comments for each section.

        :return: The verbose of this ObjSaveOption.
        :rtype: bool
        """
        return self.container['verbose']

    @verbose.setter
    def verbose(self, verbose):
        """
        Sets the verbose of this ObjSaveOption.
        Gets or sets whether generate comments for each section.

        :param verbose: The verbose of this ObjSaveOption.
        :type: bool
        """

        self.container['verbose'] = verbose

    @property
    def serialize_w(self):
        """
        Gets the serialize_w of this ObjSaveOption.
        Gets or sets whether serialize W component in model's vertex position.

        :return: The serialize_w of this ObjSaveOption.
        :rtype: bool
        """
        return self.container['serialize_w']

    @serialize_w.setter
    def serialize_w(self, serialize_w):
        """
        Sets the serialize_w of this ObjSaveOption.
        Gets or sets whether serialize W component in model's vertex position.

        :param serialize_w: The serialize_w of this ObjSaveOption.
        :type: bool
        """

        self.container['serialize_w'] = serialize_w

    @property
    def enable_materials(self):
        """
        Gets the enable_materials of this ObjSaveOption.
        Gets or sets whether import/export materials for each object.

        :return: The enable_materials of this ObjSaveOption.
        :rtype: bool
        """
        return self.container['enable_materials']

    @enable_materials.setter
    def enable_materials(self, enable_materials):
        """
        Sets the enable_materials of this ObjSaveOption.
        Gets or sets whether import/export materials for each object.

        :param enable_materials: The enable_materials of this ObjSaveOption.
        :type: bool
        """

        self.container['enable_materials'] = enable_materials

    @property
    def flip_coordinate_system(self):
        """
        Gets the flip_coordinate_system of this ObjSaveOption.
        Gets or sets whether flip coordinate system of control points/normal during importing/exporting.

        :return: The flip_coordinate_system of this ObjSaveOption.
        :rtype: bool
        """
        return self.container['flip_coordinate_system']

    @flip_coordinate_system.setter
    def flip_coordinate_system(self, flip_coordinate_system):
        """
        Sets the flip_coordinate_system of this ObjSaveOption.
        Gets or sets whether flip coordinate system of control points/normal during importing/exporting.

        :param flip_coordinate_system: The flip_coordinate_system of this ObjSaveOption.
        :type: bool
        """

        self.container['flip_coordinate_system'] = flip_coordinate_system

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
        if not isinstance(other, ObjSaveOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other