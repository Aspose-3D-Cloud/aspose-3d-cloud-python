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


class Transform(object):
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
        'translation': 'Vector3',
        'scale': 'Vector3',
        'pre_rotation': 'Vector3',
        'post_rotation': 'Vector3',
        'euler_angles': 'Vector3'
    }

    attribute_map = {
        'translation': 'Translation',
        'scale': 'Scale',
        'pre_rotation': 'PreRotation',
        'post_rotation': 'PostRotation',
        'euler_angles': 'EulerAngles'
    }
    
    @staticmethod
    def get_swagger_types():
        return Transform.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Transform.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, translation=None, scale=None, pre_rotation=None, post_rotation=None, euler_angles=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Transform - a model defined in Swagger
        """

        self.container['translation'] = None
        self.container['scale'] = None
        self.container['pre_rotation'] = None
        self.container['post_rotation'] = None
        self.container['euler_angles'] = None

        if translation is not None:
          self.translation = translation
        if scale is not None:
          self.scale = scale
        if pre_rotation is not None:
          self.pre_rotation = pre_rotation
        if post_rotation is not None:
          self.post_rotation = post_rotation
        if euler_angles is not None:
          self.euler_angles = euler_angles

    @property
    def translation(self):
        """
        Gets the translation of this Transform.
        Gets or sets the translation

        :return: The translation of this Transform.
        :rtype: Vector3
        """
        return self.container['translation']

    @translation.setter
    def translation(self, translation):
        """
        Sets the translation of this Transform.
        Gets or sets the translation

        :param translation: The translation of this Transform.
        :type: Vector3
        """

        self.container['translation'] = translation

    @property
    def scale(self):
        """
        Gets the scale of this Transform.
        Gets or sets the scale

        :return: The scale of this Transform.
        :rtype: Vector3
        """
        return self.container['scale']

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this Transform.
        Gets or sets the scale

        :param scale: The scale of this Transform.
        :type: Vector3
        """

        self.container['scale'] = scale

    @property
    def pre_rotation(self):
        """
        Gets the pre_rotation of this Transform.
        Gets or sets the pre-rotation represented in degree

        :return: The pre_rotation of this Transform.
        :rtype: Vector3
        """
        return self.container['pre_rotation']

    @pre_rotation.setter
    def pre_rotation(self, pre_rotation):
        """
        Sets the pre_rotation of this Transform.
        Gets or sets the pre-rotation represented in degree

        :param pre_rotation: The pre_rotation of this Transform.
        :type: Vector3
        """

        self.container['pre_rotation'] = pre_rotation

    @property
    def post_rotation(self):
        """
        Gets the post_rotation of this Transform.
        Gets or sets the post-rotation represented in degree

        :return: The post_rotation of this Transform.
        :rtype: Vector3
        """
        return self.container['post_rotation']

    @post_rotation.setter
    def post_rotation(self, post_rotation):
        """
        Sets the post_rotation of this Transform.
        Gets or sets the post-rotation represented in degree

        :param post_rotation: The post_rotation of this Transform.
        :type: Vector3
        """

        self.container['post_rotation'] = post_rotation

    @property
    def euler_angles(self):
        """
        Gets the euler_angles of this Transform.
        Gets or sets the rotation represented in euler angles, measured in degree             

        :return: The euler_angles of this Transform.
        :rtype: Vector3
        """
        return self.container['euler_angles']

    @euler_angles.setter
    def euler_angles(self, euler_angles):
        """
        Sets the euler_angles of this Transform.
        Gets or sets the rotation represented in euler angles, measured in degree             

        :param euler_angles: The euler_angles of this Transform.
        :type: Vector3
        """

        self.container['euler_angles'] = euler_angles

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
        if not isinstance(other, Transform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
