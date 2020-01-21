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

from .resource_py3 import Resource


class EventSubscription(Resource):
    """Event Subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource
    :vartype name: str
    :ivar type: Type of the resource
    :vartype type: str
    :ivar topic: Name of the topic of the event subscription.
    :vartype topic: str
    :ivar provisioning_state: Provisioning state of the event subscription.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Canceled', 'Failed', 'AwaitingManualAction'
    :vartype provisioning_state: str or
     ~microsoft.azure.management.eventgrid.models.EventSubscriptionProvisioningState
    :param destination: Information about the destination where events have to
     be delivered for the event subscription.
    :type destination:
     ~microsoft.azure.management.eventgrid.models.EventSubscriptionDestination
    :param filter: Information about the filter for the event subscription.
    :type filter:
     ~microsoft.azure.management.eventgrid.models.EventSubscriptionFilter
    :param labels: List of user defined labels.
    :type labels: list[str]
    :param expiration_time_utc: Expiration time of the event subscription.
    :type expiration_time_utc: datetime
    :param event_delivery_schema: The event delivery schema for the event
     subscription. Possible values include: 'EventGridSchema',
     'CustomInputSchema', 'CloudEventSchemaV1_0'
    :type event_delivery_schema: str or
     ~microsoft.azure.management.eventgrid.models.EventDeliverySchema
    :param retry_policy: The retry policy for events. This can be used to
     configure maximum number of delivery attempts and time to live for events.
    :type retry_policy:
     ~microsoft.azure.management.eventgrid.models.RetryPolicy
    :param dead_letter_destination: The DeadLetter destination of the event
     subscription.
    :type dead_letter_destination:
     ~microsoft.azure.management.eventgrid.models.DeadLetterDestination
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'topic': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'topic': {'key': 'properties.topic', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'destination': {'key': 'properties.destination', 'type': 'EventSubscriptionDestination'},
        'filter': {'key': 'properties.filter', 'type': 'EventSubscriptionFilter'},
        'labels': {'key': 'properties.labels', 'type': '[str]'},
        'expiration_time_utc': {'key': 'properties.expirationTimeUtc', 'type': 'iso-8601'},
        'event_delivery_schema': {'key': 'properties.eventDeliverySchema', 'type': 'str'},
        'retry_policy': {'key': 'properties.retryPolicy', 'type': 'RetryPolicy'},
        'dead_letter_destination': {'key': 'properties.deadLetterDestination', 'type': 'DeadLetterDestination'},
    }

    def __init__(self, *, destination=None, filter=None, labels=None, expiration_time_utc=None, event_delivery_schema=None, retry_policy=None, dead_letter_destination=None, **kwargs) -> None:
        super(EventSubscription, self).__init__(**kwargs)
        self.topic = None
        self.provisioning_state = None
        self.destination = destination
        self.filter = filter
        self.labels = labels
        self.expiration_time_utc = expiration_time_utc
        self.event_delivery_schema = event_delivery_schema
        self.retry_policy = retry_policy
        self.dead_letter_destination = dead_letter_destination
