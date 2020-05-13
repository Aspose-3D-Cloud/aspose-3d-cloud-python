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

class AMFSaveOption(SaveOptions):
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
        'enable_compression': 'bool'
    }

    attribute_map = {
        'enable_compression': 'EnableCompression'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(AMFSaveOption.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(AMFSaveOption.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, enable_compression=None, **kw):
        super(AMFSaveOption, self).__init__(**kw)
		    
        """
        AMFSaveOption - a model defined in Swagger
        """

        self.container['enable_compression'] = None

        if enable_compression is not None:
          self.enable_compression = enable_compression

    @property
    def enable_compression(self):
        """
        Gets the enable_compression of this AMFSaveOption.
        Whether to use compression to reduce the final file size, default value is true.

        :return: The enable_compression of this AMFSaveOption.
        :rtype: bool
        """
        return self.container['enable_compression']

    @enable_compression.setter
    def enable_compression(self, enable_compression):
        """
        Sets the enable_compression of this AMFSaveOption.
        Whether to use compression to reduce the final file size, default value is true.

        :param enable_compression: The enable_compression of this AMFSaveOption.
        :type: bool
        """

        self.container['enable_compression'] = enable_compression

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
        if not isinstance(other, AMFSaveOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
