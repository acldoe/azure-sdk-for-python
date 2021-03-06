# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AuthorizationRule(msrest.serialization.Model):
    """Authorization rule of an entity.

    :param type:
    :type type: str
    :param claim_type:
    :type claim_type: str
    :param claim_value:
    :type claim_value: str
    :param rights: Access rights of the entity. Values are 'Send', 'Listen', or 'Manage'.
    :type rights: list[str]
    :param created_time: The date and time when the authorization rule was created.
    :type created_time: ~datetime.datetime
    :param modified_time: The date and time when the authorization rule was modified.
    :type modified_time: ~datetime.datetime
    :param key_name: The authorization rule key name.
    :type key_name: str
    :param primary_key: The primary key of the authorization rule.
    :type primary_key: str
    :param secondary_key: The primary key of the authorization rule.
    :type secondary_key: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True, 'prefix': 'i', 'ns': 'http://www.w3.org/2001/XMLSchema-instance'}},
        'claim_type': {'key': 'ClaimType', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'claim_value': {'key': 'ClaimValue', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'rights': {'key': 'Rights', 'type': '[str]', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AccessRights', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'created_time': {'key': 'CreatedTime', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'modified_time': {'key': 'ModifiedTime', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'key_name': {'key': 'KeyName', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'primary_key': {'key': 'PrimaryKey', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'secondary_key': {'key': 'SecondaryKey', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
    }
    _xml_map = {
        'name': 'AuthorizationRule', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AuthorizationRule, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.claim_type = kwargs.get('claim_type', None)
        self.claim_value = kwargs.get('claim_value', None)
        self.rights = kwargs.get('rights', None)
        self.created_time = kwargs.get('created_time', None)
        self.modified_time = kwargs.get('modified_time', None)
        self.key_name = kwargs.get('key_name', None)
        self.primary_key = kwargs.get('primary_key', None)
        self.secondary_key = kwargs.get('secondary_key', None)


class CreateQueueBody(msrest.serialization.Model):
    """The request body for creating a queue.

    :param content: QueueDescription for the new queue.
    :type content: ~azure.servicebus.management._generated.models.CreateQueueBodyContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'CreateQueueBodyContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateQueueBody, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)


class CreateQueueBodyContent(msrest.serialization.Model):
    """QueueDescription for the new queue.

    :param type: MIME type of content.
    :type type: str
    :param queue_description: Properties of the new queue.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }
    _xml_map = {
        'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateQueueBodyContent, self).__init__(**kwargs)
        self.type = kwargs.get('type', "application/xml")
        self.queue_description = kwargs.get('queue_description', None)


class CreateTopicBody(msrest.serialization.Model):
    """The request body for creating a topic.

    :param content: TopicDescription for the new topic.
    :type content: ~azure.servicebus.management._generated.models.CreateTopicBodyContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'CreateTopicBodyContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateTopicBody, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)


class CreateTopicBodyContent(msrest.serialization.Model):
    """TopicDescription for the new topic.

    :param type: MIME type of content.
    :type type: str
    :param topic_description: Topic information to create.
    :type topic_description: ~azure.servicebus.management._generated.models.TopicDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'topic_description': {'key': 'TopicDescription', 'type': 'TopicDescription'},
    }
    _xml_map = {
        'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreateTopicBodyContent, self).__init__(**kwargs)
        self.type = kwargs.get('type', "application/xml")
        self.topic_description = kwargs.get('topic_description', None)


class MessageCountDetails(msrest.serialization.Model):
    """Details about the message counts in queue.

    :param active_message_count: Number of active messages in the queue, topic, or subscription.
    :type active_message_count: int
    :param dead_letter_message_count: Number of messages that are dead lettered.
    :type dead_letter_message_count: int
    :param scheduled_message_count: Number of scheduled messages.
    :type scheduled_message_count: int
    :param transfer_dead_letter_message_count: Number of messages transferred into dead letters.
    :type transfer_dead_letter_message_count: int
    :param transfer_message_count: Number of messages transferred to another queue, topic, or
     subscription.
    :type transfer_message_count: int
    """

    _attribute_map = {
        'active_message_count': {'key': 'ActiveMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'dead_letter_message_count': {'key': 'DeadLetterMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'scheduled_message_count': {'key': 'ScheduledMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'transfer_dead_letter_message_count': {'key': 'TransferDeadLetterMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
        'transfer_message_count': {'key': 'TransferMessageCount', 'type': 'int', 'xml': {'prefix': 'd2p1', 'ns': 'http://schemas.microsoft.com/netservices/2011/06/servicebus'}},
    }
    _xml_map = {
        'name': 'CountDetails', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MessageCountDetails, self).__init__(**kwargs)
        self.active_message_count = kwargs.get('active_message_count', None)
        self.dead_letter_message_count = kwargs.get('dead_letter_message_count', None)
        self.scheduled_message_count = kwargs.get('scheduled_message_count', None)
        self.transfer_dead_letter_message_count = kwargs.get('transfer_dead_letter_message_count', None)
        self.transfer_message_count = kwargs.get('transfer_message_count', None)


class QueueDescription(msrest.serialization.Model):
    """Description of a Service Bus queue resource.

    :param authorization_rules: Authorization rules for resource.
    :type authorization_rules:
     list[~azure.servicebus.management._generated.models.AuthorizationRule]
    :param auto_delete_on_idle: ISO 8601 timeSpan idle interval after which the queue is
     automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: ~datetime.timedelta
    :param created_at: The exact time the queue was created.
    :type created_at: ~datetime.datetime
    :param dead_lettering_on_message_expiration: A value that indicates whether this queue has dead
     letter support when a message expires.
    :type dead_lettering_on_message_expiration: bool
    :param default_message_time_to_live: ISO 8601 default message timespan to live value. This is
     the duration after which the message expires, starting from when the message is sent to Service
     Bus. This is the default value used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: ~datetime.timedelta
    :param duplicate_detection_history_time_window: ISO 8601 timeSpan structure that defines the
     duration of the duplicate detection history. The default value is 10 minutes.
    :type duplicate_detection_history_time_window: ~datetime.timedelta
    :param entity_availability_status: Availibility status of the entity. Possible values include:
     "Available", "Limited", "Renaming", "Restoring", "Unknown".
    :type entity_availability_status: str or
     ~azure.servicebus.management._generated.models.EntityAvailabilityStatus
    :param enable_batched_operations: Value that indicates whether server-side batched operations
     are enabled.
    :type enable_batched_operations: bool
    :param enable_express: A value that indicates whether Express Entities are enabled. An express
     queue holds a message in memory temporarily before writing it to persistent storage.
    :type enable_express: bool
    :param enable_partitioning: A value that indicates whether the queue is to be partitioned
     across multiple message brokers.
    :type enable_partitioning: bool
    :param is_anonymous_accessible: A value indicating if the resource can be accessed without
     authorization.
    :type is_anonymous_accessible: bool
    :param lock_duration: ISO 8601 timespan duration of a peek-lock; that is, the amount of time
     that the message is locked for other receivers. The maximum value for LockDuration is 5
     minutes; the default value is 1 minute.
    :type lock_duration: ~datetime.timedelta
    :param max_delivery_count: The maximum delivery count. A message is automatically deadlettered
     after this number of deliveries. Default value is 10.
    :type max_delivery_count: int
    :param max_size_in_megabytes: The maximum size of the queue in megabytes, which is the size of
     memory allocated for the queue.
    :type max_size_in_megabytes: int
    :param requires_duplicate_detection: A value indicating if this queue requires duplicate
     detection.
    :type requires_duplicate_detection: bool
    :param requires_session: A value that indicates whether the queue supports the concept of
     sessions.
    :type requires_session: bool
    :param status: Status of a Service Bus resource. Possible values include: "Active", "Creating",
     "Deleting", "Disabled", "ReceiveDisabled", "Renaming", "Restoring", "SendDisabled", "Unknown".
    :type status: str or ~azure.servicebus.management._generated.models.EntityStatus
    :param support_ordering: A value that indicates whether the queue supports ordering.
    :type support_ordering: bool
    :param accessed_at: Last time a message was sent, or the last time there was a receive request
     to this queue.
    :type accessed_at: ~datetime.datetime
    :param updated_at: The exact time a message was updated in the queue.
    :type updated_at: ~datetime.datetime
    :param size_in_bytes: The size of the queue, in bytes.
    :type size_in_bytes: int
    :param message_count: The number of messages in the queue.
    :type message_count: int
    :param message_count_details: Details about the message counts in queue.
    :type message_count_details: ~azure.servicebus.management._generated.models.MessageCountDetails
    """

    _attribute_map = {
        'authorization_rules': {'key': 'AuthorizationRules', 'type': '[AuthorizationRule]', 'xml': {'name': 'AuthorizationRules', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AuthorizationRule', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'auto_delete_on_idle': {'key': 'AutoDeleteOnIdle', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'created_at': {'key': 'CreatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'dead_lettering_on_message_expiration': {'key': 'DeadLetteringOnMessageExpiration', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'default_message_time_to_live': {'key': 'DefaultMessageTimeToLive', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'duplicate_detection_history_time_window': {'key': 'DuplicateDetectionHistoryTimeWindow', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'entity_availability_status': {'key': 'EntityAvailabilityStatus', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_batched_operations': {'key': 'EnableBatchedOperations', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_express': {'key': 'EnableExpress', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_partitioning': {'key': 'EnablePartitioning', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'is_anonymous_accessible': {'key': 'IsAnonymousAccessible', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'lock_duration': {'key': 'LockDuration', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_delivery_count': {'key': 'MaxDeliveryCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_size_in_megabytes': {'key': 'MaxSizeInMegabytes', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_duplicate_detection': {'key': 'RequiresDuplicateDetection', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'requires_session': {'key': 'RequiresSession', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'status': {'key': 'Status', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'support_ordering': {'key': 'SupportOrdering', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'accessed_at': {'key': 'AccessedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'updated_at': {'key': 'UpdatedAt', 'type': 'iso-8601', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'size_in_bytes': {'key': 'SizeInBytes', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count': {'key': 'MessageCount', 'type': 'int', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'message_count_details': {'key': 'MessageCountDetails', 'type': 'MessageCountDetails'},
    }
    _xml_map = {
        'name': 'QueueDescription', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescription, self).__init__(**kwargs)
        self.authorization_rules = kwargs.get('authorization_rules', None)
        self.auto_delete_on_idle = kwargs.get('auto_delete_on_idle', None)
        self.created_at = kwargs.get('created_at', None)
        self.dead_lettering_on_message_expiration = kwargs.get('dead_lettering_on_message_expiration', None)
        self.default_message_time_to_live = kwargs.get('default_message_time_to_live', None)
        self.duplicate_detection_history_time_window = kwargs.get('duplicate_detection_history_time_window', None)
        self.entity_availability_status = kwargs.get('entity_availability_status', None)
        self.enable_batched_operations = kwargs.get('enable_batched_operations', None)
        self.enable_express = kwargs.get('enable_express', None)
        self.enable_partitioning = kwargs.get('enable_partitioning', None)
        self.is_anonymous_accessible = kwargs.get('is_anonymous_accessible', None)
        self.lock_duration = kwargs.get('lock_duration', None)
        self.max_delivery_count = kwargs.get('max_delivery_count', None)
        self.max_size_in_megabytes = kwargs.get('max_size_in_megabytes', None)
        self.requires_duplicate_detection = kwargs.get('requires_duplicate_detection', None)
        self.requires_session = kwargs.get('requires_session', None)
        self.status = kwargs.get('status', None)
        self.support_ordering = kwargs.get('support_ordering', None)
        self.accessed_at = kwargs.get('accessed_at', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.size_in_bytes = kwargs.get('size_in_bytes', None)
        self.message_count = kwargs.get('message_count', None)
        self.message_count_details = kwargs.get('message_count_details', None)


class QueueDescriptionEntry(msrest.serialization.Model):
    """Represents an entry in the feed when querying queues.

    :param base: Base URL for the query.
    :type base: str
    :param id: The URL of the GET request.
    :type id: str
    :param title: The name of the queue.
    :type title: ~azure.servicebus.management._generated.models.ResponseTitle
    :param published: The timestamp for when this queue was published.
    :type published: ~datetime.datetime
    :param updated: The timestamp for when this queue was last updated.
    :type updated: ~datetime.datetime
    :param author: The author that created this resource.
    :type author: ~azure.servicebus.management._generated.models.ResponseAuthor
    :param link: The URL for the HTTP request.
    :type link: ~azure.servicebus.management._generated.models.ResponseLink
    :param content: The QueueDescription.
    :type content: ~azure.servicebus.management._generated.models.QueueDescriptionEntryContent
    """

    _attribute_map = {
        'base': {'key': 'base', 'type': 'str', 'xml': {'name': 'base', 'attr': True, 'prefix': 'xml'}},
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'ResponseTitle'},
        'published': {'key': 'published', 'type': 'iso-8601'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'author': {'key': 'author', 'type': 'ResponseAuthor'},
        'link': {'key': 'link', 'type': 'ResponseLink'},
        'content': {'key': 'content', 'type': 'QueueDescriptionEntryContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescriptionEntry, self).__init__(**kwargs)
        self.base = kwargs.get('base', None)
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        self.published = kwargs.get('published', None)
        self.updated = kwargs.get('updated', None)
        self.author = kwargs.get('author', None)
        self.link = kwargs.get('link', None)
        self.content = kwargs.get('content', None)


class QueueDescriptionEntryContent(msrest.serialization.Model):
    """The QueueDescription.

    :param type: Type of content in queue response.
    :type type: str
    :param queue_description: Description of a Service Bus queue resource.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescriptionEntryContent, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.queue_description = kwargs.get('queue_description', None)


class QueueDescriptionFeed(msrest.serialization.Model):
    """Response from listing Service Bus queues.

    :param id: URL of the list queues query.
    :type id: str
    :param title: The entity type for the feed.
    :type title: str
    :param updated: Datetime of the query.
    :type updated: ~datetime.datetime
    :param link: Links to paginated response.
    :type link: list[~azure.servicebus.management._generated.models.ResponseLink]
    :param entry: Queue entries.
    :type entry: list[~azure.servicebus.management._generated.models.QueueDescriptionEntry]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'link': {'key': 'link', 'type': '[ResponseLink]'},
        'entry': {'key': 'entry', 'type': '[QueueDescriptionEntry]'},
    }
    _xml_map = {
        'name': 'feed', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescriptionFeed, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        self.updated = kwargs.get('updated', None)
        self.link = kwargs.get('link', None)
        self.entry = kwargs.get('entry', None)


class QueueDescriptionResponse(msrest.serialization.Model):
    """The response from a Queue_Get operation.

    :param id: The URL of the GET request.
    :type id: str
    :param title: The name of the queue.
    :type title: str
    :param published: The timestamp for when this queue was published.
    :type published: str
    :param updated: The timestamp for when this queue was last updated.
    :type updated: str
    :param author: The author that created this resource.
    :type author: ~azure.servicebus.management._generated.models.ResponseAuthor
    :param link: The URL for the HTTP request.
    :type link: ~azure.servicebus.management._generated.models.ResponseLink
    :param content: Contents of a Queue_Get response.
    :type content: ~azure.servicebus.management._generated.models.QueueDescriptionResponseContent
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'published': {'key': 'published', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'str'},
        'author': {'key': 'author', 'type': 'ResponseAuthor'},
        'link': {'key': 'link', 'type': 'ResponseLink'},
        'content': {'key': 'content', 'type': 'QueueDescriptionResponseContent'},
    }
    _xml_map = {
        'name': 'entry', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescriptionResponse, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        self.published = kwargs.get('published', None)
        self.updated = kwargs.get('updated', None)
        self.author = kwargs.get('author', None)
        self.link = kwargs.get('link', None)
        self.content = kwargs.get('content', None)


class QueueDescriptionResponseContent(msrest.serialization.Model):
    """Contents of a Queue_Get response.

    :param type: Type of content in queue response.
    :type type: str
    :param queue_description: Description of a Service Bus queue resource.
    :type queue_description: ~azure.servicebus.management._generated.models.QueueDescription
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'queue_description': {'key': 'QueueDescription', 'type': 'QueueDescription'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueueDescriptionResponseContent, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.queue_description = kwargs.get('queue_description', None)


class ResponseAuthor(msrest.serialization.Model):
    """The author that created this resource.

    :param name: The Service Bus namespace.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResponseAuthor, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class ResponseLink(msrest.serialization.Model):
    """The URL for the HTTP request.

    :param href: The URL of the GET request.
    :type href: str
    :param rel: What the link href is relative to.
    :type rel: str
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str', 'xml': {'attr': True}},
        'rel': {'key': 'rel', 'type': 'str', 'xml': {'attr': True}},
    }
    _xml_map = {
        'name': 'link', 'ns': 'http://www.w3.org/2005/Atom'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResponseLink, self).__init__(**kwargs)
        self.href = kwargs.get('href', None)
        self.rel = kwargs.get('rel', None)


class ResponseTitle(msrest.serialization.Model):
    """The title of the response.

    :param type: Type of value.
    :type type: str
    :param title: Contents of the title.
    :type title: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str', 'xml': {'attr': True}},
        'title': {'key': 'title', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResponseTitle, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.title = kwargs.get('title', None)


class ServiceBusManagementError(msrest.serialization.Model):
    """The error response from Service Bus.

    :param code: The service error code.
    :type code: int
    :param detail: The service error message.
    :type detail: str
    """

    _attribute_map = {
        'code': {'key': 'Code', 'type': 'int'},
        'detail': {'key': 'Detail', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ServiceBusManagementError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.detail = kwargs.get('detail', None)


class TopicDescription(msrest.serialization.Model):
    """Description of a Service Bus topic resource.

    :param topic_name: Name of the topic.
    :type topic_name: str
    :param authorization_rules: Authorization rules for resource.
    :type authorization_rules:
     list[~azure.servicebus.management._generated.models.AuthorizationRule]
    :param auto_delete_on_idle: ISO 8601 timeSpan idle interval after which the topic is
     automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: ~datetime.timedelta
    :param default_message_time_to_live: ISO 8601 default message timespan to live value. This is
     the duration after which the message expires, starting from when the message is sent to Service
     Bus. This is the default value used when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: ~datetime.timedelta
    :param duplicate_detection_history_time_window: ISO 8601 timeSpan structure that defines the
     duration of the duplicate detection history. The default value is 10 minutes.
    :type duplicate_detection_history_time_window: ~datetime.timedelta
    :param enable_batched_operations: Value that indicates whether server-side batched operations
     are enabled.
    :type enable_batched_operations: bool
    :param enable_partitioning: A value that indicates whether the topic is to be partitioned
     across multiple message brokers.
    :type enable_partitioning: bool
    :param max_size_in_megabytes: The maximum size of the topic in megabytes, which is the size of
     memory allocated for the topic.
    :type max_size_in_megabytes: long
    :param requires_duplicate_detection: A value indicating if this topic requires duplicate
     detection.
    :type requires_duplicate_detection: bool
    :param status: Status of a Service Bus resource. Possible values include: "Active", "Creating",
     "Deleting", "Disabled", "ReceiveDisabled", "Renaming", "Restoring", "SendDisabled", "Unknown".
    :type status: str or ~azure.servicebus.management._generated.models.EntityStatus
    :param support_ordering: A value that indicates whether the topic supports ordering.
    :type support_ordering: bool
    :param user_metadata: Metadata associated with the topic.
    :type user_metadata: str
    """

    _attribute_map = {
        'topic_name': {'key': 'TopicName', 'type': 'str'},
        'authorization_rules': {'key': 'AuthorizationRules', 'type': '[AuthorizationRule]', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect', 'wrapped': True, 'itemsName': 'AuthorizationRule', 'itemsNs': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'auto_delete_on_idle': {'key': 'AutoDeleteOnIdle', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'default_message_time_to_live': {'key': 'DefaultMessageTimeToLive', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'duplicate_detection_history_time_window': {'key': 'DuplicateDetectionHistoryTimeWindow', 'type': 'duration', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_batched_operations': {'key': 'EnableBatchedOperations', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'enable_partitioning': {'key': 'EnablePartitioning', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'max_size_in_megabytes': {'key': 'MaxSizeInMegabytes', 'type': 'long'},
        'requires_duplicate_detection': {'key': 'RequiresDuplicateDetection', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'status': {'key': 'Status', 'type': 'str', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'support_ordering': {'key': 'SupportOrdering', 'type': 'bool', 'xml': {'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'}},
        'user_metadata': {'key': 'UserMetadata', 'type': 'str'},
    }
    _xml_map = {
        'name': 'TopicDescription', 'ns': 'http://schemas.microsoft.com/netservices/2010/10/servicebus/connect'
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TopicDescription, self).__init__(**kwargs)
        self.topic_name = kwargs.get('topic_name', None)
        self.authorization_rules = kwargs.get('authorization_rules', None)
        self.auto_delete_on_idle = kwargs.get('auto_delete_on_idle', None)
        self.default_message_time_to_live = kwargs.get('default_message_time_to_live', None)
        self.duplicate_detection_history_time_window = kwargs.get('duplicate_detection_history_time_window', None)
        self.enable_batched_operations = kwargs.get('enable_batched_operations', None)
        self.enable_partitioning = kwargs.get('enable_partitioning', None)
        self.max_size_in_megabytes = kwargs.get('max_size_in_megabytes', None)
        self.requires_duplicate_detection = kwargs.get('requires_duplicate_detection', None)
        self.status = kwargs.get('status', None)
        self.support_ordering = kwargs.get('support_ordering', None)
        self.user_metadata = kwargs.get('user_metadata', None)
