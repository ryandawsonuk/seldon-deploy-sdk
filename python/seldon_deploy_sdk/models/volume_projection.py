# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VolumeProjection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'config_map': 'ConfigMapProjection',
        'downward_api': 'DownwardAPIProjection',
        'secret': 'SecretProjection',
        'service_account_token': 'ServiceAccountTokenProjection'
    }

    attribute_map = {
        'config_map': 'configMap',
        'downward_api': 'downwardAPI',
        'secret': 'secret',
        'service_account_token': 'serviceAccountToken'
    }

    def __init__(self, config_map=None, downward_api=None, secret=None, service_account_token=None):  # noqa: E501
        """VolumeProjection - a model defined in Swagger"""  # noqa: E501

        self._config_map = None
        self._downward_api = None
        self._secret = None
        self._service_account_token = None
        self.discriminator = None

        if config_map is not None:
            self.config_map = config_map
        if downward_api is not None:
            self.downward_api = downward_api
        if secret is not None:
            self.secret = secret
        if service_account_token is not None:
            self.service_account_token = service_account_token

    @property
    def config_map(self):
        """Gets the config_map of this VolumeProjection.  # noqa: E501


        :return: The config_map of this VolumeProjection.  # noqa: E501
        :rtype: ConfigMapProjection
        """
        return self._config_map

    @config_map.setter
    def config_map(self, config_map):
        """Sets the config_map of this VolumeProjection.


        :param config_map: The config_map of this VolumeProjection.  # noqa: E501
        :type: ConfigMapProjection
        """

        self._config_map = config_map

    @property
    def downward_api(self):
        """Gets the downward_api of this VolumeProjection.  # noqa: E501


        :return: The downward_api of this VolumeProjection.  # noqa: E501
        :rtype: DownwardAPIProjection
        """
        return self._downward_api

    @downward_api.setter
    def downward_api(self, downward_api):
        """Sets the downward_api of this VolumeProjection.


        :param downward_api: The downward_api of this VolumeProjection.  # noqa: E501
        :type: DownwardAPIProjection
        """

        self._downward_api = downward_api

    @property
    def secret(self):
        """Gets the secret of this VolumeProjection.  # noqa: E501


        :return: The secret of this VolumeProjection.  # noqa: E501
        :rtype: SecretProjection
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this VolumeProjection.


        :param secret: The secret of this VolumeProjection.  # noqa: E501
        :type: SecretProjection
        """

        self._secret = secret

    @property
    def service_account_token(self):
        """Gets the service_account_token of this VolumeProjection.  # noqa: E501


        :return: The service_account_token of this VolumeProjection.  # noqa: E501
        :rtype: ServiceAccountTokenProjection
        """
        return self._service_account_token

    @service_account_token.setter
    def service_account_token(self, service_account_token):
        """Sets the service_account_token of this VolumeProjection.


        :param service_account_token: The service_account_token of this VolumeProjection.  # noqa: E501
        :type: ServiceAccountTokenProjection
        """

        self._service_account_token = service_account_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(VolumeProjection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VolumeProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other