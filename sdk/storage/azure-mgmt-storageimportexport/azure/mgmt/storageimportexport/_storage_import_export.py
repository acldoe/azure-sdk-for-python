# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import StorageImportExportConfiguration
from .operations import LocationsOperations
from .operations import JobsOperations
from .operations import BitLockerKeysOperations
from .operations import Operations
from . import models


class StorageImportExport(SDKClient):
    """The Storage Import/Export Resource Provider API.

    :ivar config: Configuration for client.
    :vartype config: StorageImportExportConfiguration

    :ivar locations: Locations operations
    :vartype locations: azure.mgmt.storageimportexport.operations.LocationsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.storageimportexport.operations.JobsOperations
    :ivar bit_locker_keys: BitLockerKeys operations
    :vartype bit_locker_keys: azure.mgmt.storageimportexport.operations.BitLockerKeysOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storageimportexport.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID for the Azure user.
    :type subscription_id: str
    :param accept_language: Specifies the preferred language for the response.
    :type accept_language: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, accept_language=None, base_url=None):

        self.config = StorageImportExportConfiguration(credentials, subscription_id, accept_language, base_url)
        super(StorageImportExport, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.locations = LocationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bit_locker_keys = BitLockerKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)