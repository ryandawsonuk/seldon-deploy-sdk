# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Model(object):
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
        'uri': 'str',
        'name': 'str',
        'version': 'str',
        'artifact_type': 'V1ArtifactType',
        'task_type': 'str',
        'tags': 'dict(str, str)',
        'metrics': 'dict(str, float)',
        'creation_time': 'datetime',
        'prediction_schema': 'V1PredictionSchema'
    }

    attribute_map = {
        'uri': 'URI',
        'name': 'name',
        'version': 'version',
        'artifact_type': 'artifactType',
        'task_type': 'taskType',
        'tags': 'tags',
        'metrics': 'metrics',
        'creation_time': 'creationTime',
        'prediction_schema': 'predictionSchema'
    }

    def __init__(self, uri=None, name=None, version='"v0.0.1"', artifact_type=None, task_type=None, tags=None, metrics=None, creation_time=None, prediction_schema=None):  # noqa: E501
        """V1Model - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._version = None
        self._artifact_type = None
        self._task_type = None
        self._tags = None
        self._metrics = None
        self._creation_time = None
        self._prediction_schema = None
        self.discriminator = None

        self.uri = uri
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if artifact_type is not None:
            self.artifact_type = artifact_type
        if task_type is not None:
            self.task_type = task_type
        if tags is not None:
            self.tags = tags
        if metrics is not None:
            self.metrics = metrics
        if creation_time is not None:
            self.creation_time = creation_time
        if prediction_schema is not None:
            self.prediction_schema = prediction_schema

    @property
    def uri(self):
        """Gets the uri of this V1Model.  # noqa: E501

        The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters.  # noqa: E501

        :return: The uri of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this V1Model.

        The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters.  # noqa: E501

        :param uri: The uri of this V1Model.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this V1Model.  # noqa: E501

        The name of the model. It must not exceed 200 characters.  # noqa: E501

        :return: The name of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Model.

        The name of the model. It must not exceed 200 characters.  # noqa: E501

        :param name: The name of this V1Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this V1Model.  # noqa: E501

        The version of the model. It must not exceed 50 characters.  # noqa: E501

        :return: The version of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1Model.

        The version of the model. It must not exceed 50 characters.  # noqa: E501

        :param version: The version of this V1Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def artifact_type(self):
        """Gets the artifact_type of this V1Model.  # noqa: E501

        The artifact type of the model. This is the library used to develop the model.  # noqa: E501

        :return: The artifact_type of this V1Model.  # noqa: E501
        :rtype: V1ArtifactType
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this V1Model.

        The artifact type of the model. This is the library used to develop the model.  # noqa: E501

        :param artifact_type: The artifact_type of this V1Model.  # noqa: E501
        :type: V1ArtifactType
        """

        self._artifact_type = artifact_type

    @property
    def task_type(self):
        """Gets the task_type of this V1Model.  # noqa: E501

        The task type of the model. It must not exceed 50 characters.  # noqa: E501

        :return: The task_type of this V1Model.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this V1Model.

        The task type of the model. It must not exceed 50 characters.  # noqa: E501

        :param task_type: The task_type of this V1Model.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def tags(self):
        """Gets the tags of this V1Model.  # noqa: E501

        Key-value pairs of arbitrary metadata associated with the model. Each key and value must not exceed 100 and 500 characters respectively.  # noqa: E501

        :return: The tags of this V1Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1Model.

        Key-value pairs of arbitrary metadata associated with the model. Each key and value must not exceed 100 and 500 characters respectively.  # noqa: E501

        :param tags: The tags of this V1Model.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def metrics(self):
        """Gets the metrics of this V1Model.  # noqa: E501

        Key-value pairs of static metrics associated with the model. For dynamic metrics look into metrics https://deploy.seldon.io/docs/getting-started/production-installation/metrics/ . Keys must not exceed 100 characters.  # noqa: E501

        :return: The metrics of this V1Model.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this V1Model.

        Key-value pairs of static metrics associated with the model. For dynamic metrics look into metrics https://deploy.seldon.io/docs/getting-started/production-installation/metrics/ . Keys must not exceed 100 characters.  # noqa: E501

        :param metrics: The metrics of this V1Model.  # noqa: E501
        :type: dict(str, float)
        """

        self._metrics = metrics

    @property
    def creation_time(self):
        """Gets the creation_time of this V1Model.  # noqa: E501

        The creation timestamp for the model metadata entry. It is automatically created by the Metadata service and cannot be modified. The timestamp is using the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format/  # noqa: E501

        :return: The creation_time of this V1Model.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this V1Model.

        The creation timestamp for the model metadata entry. It is automatically created by the Metadata service and cannot be modified. The timestamp is using the [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format/  # noqa: E501

        :param creation_time: The creation_time of this V1Model.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def prediction_schema(self):
        """Gets the prediction_schema of this V1Model.  # noqa: E501

        The schema defining the inputs/outputs for the given model.  # noqa: E501

        :return: The prediction_schema of this V1Model.  # noqa: E501
        :rtype: V1PredictionSchema
        """
        return self._prediction_schema

    @prediction_schema.setter
    def prediction_schema(self, prediction_schema):
        """Sets the prediction_schema of this V1Model.

        The schema defining the inputs/outputs for the given model.  # noqa: E501

        :param prediction_schema: The prediction_schema of this V1Model.  # noqa: E501
        :type: V1PredictionSchema
        """

        self._prediction_schema = prediction_schema

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
        if issubclass(V1Model, dict):
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
        if not isinstance(other, V1Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
