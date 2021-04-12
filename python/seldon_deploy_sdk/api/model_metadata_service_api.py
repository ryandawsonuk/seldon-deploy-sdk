# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seldon_deploy_sdk.api_client import ApiClient


class ModelMetadataServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def model_metadata_service_create_model_metadata(self, body, **kwargs):  # noqa: E501
        """Create a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_create_model_metadata(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1Model body: (required)
        :return: V1ModelMetadataCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.model_metadata_service_create_model_metadata_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.model_metadata_service_create_model_metadata_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def model_metadata_service_create_model_metadata_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_create_model_metadata_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1Model body: (required)
        :return: V1ModelMetadataCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_metadata_service_create_model_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `model_metadata_service_create_model_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/seldon-deploy/api/v1alpha1/model/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ModelMetadataCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def model_metadata_service_delete_model_metadata(self, uri, **kwargs):  # noqa: E501
        """Delete a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_delete_model_metadata(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters. (required)
        :return: V1ModelMetadataDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.model_metadata_service_delete_model_metadata_with_http_info(uri, **kwargs)  # noqa: E501
        else:
            (data) = self.model_metadata_service_delete_model_metadata_with_http_info(uri, **kwargs)  # noqa: E501
            return data

    def model_metadata_service_delete_model_metadata_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Delete a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_delete_model_metadata_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: The URI for the storage bucket containing the model, or the URI to the docker image for custom models. It must be a valid URI as defined in RFC 3986, and must not exceed 200 characters. (required)
        :return: V1ModelMetadataDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_metadata_service_delete_model_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `model_metadata_service_delete_model_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uri' in params:
            query_params.append(('URI', params['uri']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/seldon-deploy/api/v1alpha1/model/metadata', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ModelMetadataDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def model_metadata_service_list_model_metadata(self, **kwargs):  # noqa: E501
        """List Model Metadata entries.  # noqa: E501

        List takes several parameters that are present in the Model Metadata and tries to list all metadata entries that match all supplied fields. For more complex queries where other logical operators like OR, NOT, etc. are needed you can use the `query` parameter. The `query` parameter takes precedence if present.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_list_model_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri:
        :param str name:
        :param str version:
        :param str implementation:
        :param str task_type:
        :param str model_type:
        :param dict tags:
        :param dict metrics:
        :param str query:
        :param int page_size: Optional. The maximum number of Folders to return in the response.
        :param str page_token: Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from.
        :param str list_mask: Optional. Can be used to specify which fields of Model you wish to return in the response. If left empty all fields will be returned.
        :return: V1ModelMetadataListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.model_metadata_service_list_model_metadata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.model_metadata_service_list_model_metadata_with_http_info(**kwargs)  # noqa: E501
            return data

    def model_metadata_service_list_model_metadata_with_http_info(self, **kwargs):  # noqa: E501
        """List Model Metadata entries.  # noqa: E501

        List takes several parameters that are present in the Model Metadata and tries to list all metadata entries that match all supplied fields. For more complex queries where other logical operators like OR, NOT, etc. are needed you can use the `query` parameter. The `query` parameter takes precedence if present.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_list_model_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri:
        :param str name:
        :param str version:
        :param str implementation:
        :param str task_type:
        :param str model_type:
        :param dict tags:
        :param dict metrics:
        :param str query:
        :param int page_size: Optional. The maximum number of Folders to return in the response.
        :param str page_token: Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from.
        :param str list_mask: Optional. Can be used to specify which fields of Model you wish to return in the response. If left empty all fields will be returned.
        :return: V1ModelMetadataListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', 'name', 'version', 'implementation', 'task_type', 'model_type', 'query', 'page_size', 'page_token', 'list_mask', "tags", "metrics"]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_metadata_service_list_model_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uri' in params:
            query_params.append(('URI', params['uri']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'implementation' in params:
            query_params.append(('implementation', params['implementation']))  # noqa: E501
        if 'task_type' in params:
            query_params.append(('taskType', params['task_type']))  # noqa: E501
        if 'model_type' in params:
            query_params.append(('modelType', params['model_type']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'list_mask' in params:
            query_params.append(('listMask', params['list_mask']))  # noqa: E501
        if 'tags' in params:
            for key, val in params["tags"].items():
                query_params.append((f"tags[{key}]", val))
        if 'metrics' in params:
            for key, val in params["metrics"].items():
                query_params.append((f"metrics[{key}]", val))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/seldon-deploy/api/v1alpha1/model/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ModelMetadataListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def model_metadata_service_list_runtime_metadata_for_model(self, **kwargs):  # noqa: E501
        """List Runtime Metadata for all deployments associated with a model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_list_runtime_metadata_for_model(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_uri:
        :param str deployment_uid:
        :param str deployment_name:
        :param str deployment_namespace:
        :param str deployment_status:
        :param str predictor_name:
        :param str node_name:
        :param int page_size: Optional. The maximum number of Folders to return in the response.
        :param str page_token: Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from.
        :param str list_mask: Optional. Can be used to specify which fields of RuntimeMetadata you wish to return in the response. If left empty all fields will be returned.
        :return: V1RuntimeMetadataListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.model_metadata_service_list_runtime_metadata_for_model_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.model_metadata_service_list_runtime_metadata_for_model_with_http_info(**kwargs)  # noqa: E501
            return data

    def model_metadata_service_list_runtime_metadata_for_model_with_http_info(self, **kwargs):  # noqa: E501
        """List Runtime Metadata for all deployments associated with a model.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_list_runtime_metadata_for_model_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_uri:
        :param str deployment_uid:
        :param str deployment_name:
        :param str deployment_namespace:
        :param str deployment_status:
        :param str predictor_name:
        :param str node_name:
        :param int page_size: Optional. The maximum number of Folders to return in the response.
        :param str page_token: Optional. A pagination token returned from a previous call to `List` that indicates where this listing should continue from.
        :param str list_mask: Optional. Can be used to specify which fields of RuntimeMetadata you wish to return in the response. If left empty all fields will be returned.
        :return: V1RuntimeMetadataListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_uri', 'deployment_uid', 'deployment_name', 'deployment_namespace', 'deployment_status', 'predictor_name', 'node_name', 'page_size', 'page_token', 'list_mask']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_metadata_service_list_runtime_metadata_for_model" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_uri' in params:
            query_params.append(('ModelURI', params['model_uri']))  # noqa: E501
        if 'deployment_uid' in params:
            query_params.append(('DeploymentUID', params['deployment_uid']))  # noqa: E501
        if 'deployment_name' in params:
            query_params.append(('DeploymentName', params['deployment_name']))  # noqa: E501
        if 'deployment_namespace' in params:
            query_params.append(('DeploymentNamespace', params['deployment_namespace']))  # noqa: E501
        if 'deployment_status' in params:
            query_params.append(('DeploymentStatus', params['deployment_status']))  # noqa: E501
        if 'predictor_name' in params:
            query_params.append(('PredictorName', params['predictor_name']))  # noqa: E501
        if 'node_name' in params:
            query_params.append(('NodeName', params['node_name']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'list_mask' in params:
            query_params.append(('listMask', params['list_mask']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/seldon-deploy/api/v1alpha1/model/metadata/runtime', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1RuntimeMetadataListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def model_metadata_service_update_model_metadata(self, body, **kwargs):  # noqa: E501
        """Update a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_update_model_metadata(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1Model body: (required)
        :return: V1ModelMetadataUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.model_metadata_service_update_model_metadata_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.model_metadata_service_update_model_metadata_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def model_metadata_service_update_model_metadata_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update a Model Metadata entry.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.model_metadata_service_update_model_metadata_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1Model body: (required)
        :return: V1ModelMetadataUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method model_metadata_service_update_model_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `model_metadata_service_update_model_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/seldon-deploy/api/v1alpha1/model/metadata', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1ModelMetadataUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
