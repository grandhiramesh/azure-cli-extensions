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

from msrest.serialization import Model


class DomainUpdateParameters(Model):
    """Properties of the Domain update.

    :param tags: Tags of the domains resource
    :type tags: dict[str, str]
    :param allow_traffic_from_all_ips: This determines if IP filtering rules
     ought to be evaluated or not. By default it will not evaluate and will
     allow traffic from all IPs.
    :type allow_traffic_from_all_ips: bool
    :param inbound_ip_rules: This determines the IP filtering rules that ought
     be applied when events are received on this domain.
    :type inbound_ip_rules:
     list[~microsoft.azure.management.eventgrid.models.InboundIpRule]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'allow_traffic_from_all_ips': {'key': 'allowTrafficFromAllIPs', 'type': 'bool'},
        'inbound_ip_rules': {'key': 'inboundIpRules', 'type': '[InboundIpRule]'},
    }

    def __init__(self, *, tags=None, allow_traffic_from_all_ips: bool=None, inbound_ip_rules=None, **kwargs) -> None:
        super(DomainUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.allow_traffic_from_all_ips = allow_traffic_from_all_ips
        self.inbound_ip_rules = inbound_ip_rules
