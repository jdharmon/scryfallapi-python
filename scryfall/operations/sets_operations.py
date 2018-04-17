# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class SetsOperations(object):
    """SetsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_all(
            self, custom_headers=None, raw=False, **operation_config):
        """

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SetList or ClientRawResponse if raw=true
        :rtype: ~scryfall.models.SetList or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<scryfall.models.ErrorException>`
        """
        # Construct URL
        url = self.get_all.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SetList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_all.metadata = {'url': '/sets'}

    def get_by_code(
            self, code, custom_headers=None, raw=False, **operation_config):
        """

        :param code:
        :type code: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Set or ClientRawResponse if raw=true
        :rtype: ~scryfall.models.Set or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<scryfall.models.ErrorException>`
        """
        # Construct URL
        url = self.get_by_code.metadata['url']
        path_format_arguments = {
            'code': self._serialize.url("code", code, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Set', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_code.metadata = {'url': '/sets/{code}'}
