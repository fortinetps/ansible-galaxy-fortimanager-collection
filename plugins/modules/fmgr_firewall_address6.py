#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_firewall_address6
short_description: Configure IPv6 firewall addresses.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/address6
    - /pm/config/global/obj/firewall/address6
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
    schema_object0:
        methods: [add, set, update]
        description: 'Configure IPv6 firewall addresses.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    cache-ttl:
                        type: int
                        description: 'Minimal TTL of individual IPv6 addresses in FQDN cache.'
                    color:
                        type: int
                        description: 'Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1).'
                    comment:
                        type: str
                        description: 'Comment.'
                    dynamic_mapping:
                        -
                            _scope:
                                -
                                    name:
                                        type: str
                                    vdom:
                                        type: str
                            cache-ttl:
                                type: int
                            color:
                                type: int
                            comment:
                                type: str
                            end-ip:
                                type: str
                            fqdn:
                                type: str
                            host:
                                type: str
                            host-type:
                                type: str
                                choices:
                                    - 'any'
                                    - 'specific'
                            ip6:
                                type: str
                            obj-id:
                                type: str
                            sdn:
                                type: str
                                choices:
                                    - 'nsx'
                            start-ip:
                                type: str
                            tags:
                                type: str
                            template:
                                type: str
                            type:
                                type: str
                                choices:
                                    - 'ipprefix'
                                    - 'iprange'
                                    - 'nsx'
                                    - 'dynamic'
                                    - 'fqdn'
                                    - 'template'
                            uuid:
                                type: str
                            visibility:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                    end-ip:
                        type: str
                        description: 'Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
                    fqdn:
                        type: str
                        description: 'Fully qualified domain name.'
                    host:
                        type: str
                        description: 'Host Address.'
                    host-type:
                        type: str
                        description: 'Host type.'
                        choices:
                            - 'any'
                            - 'specific'
                    ip6:
                        type: str
                        description: 'IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).'
                    list:
                        -
                            ip:
                                type: str
                                description: 'IP.'
                    name:
                        type: str
                        description: 'Address name.'
                    obj-id:
                        type: str
                        description: 'Object ID for NSX.'
                    sdn:
                        type: str
                        description: 'SDN.'
                        choices:
                            - 'nsx'
                    start-ip:
                        type: str
                        description: 'First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
                    subnet-segment:
                        -
                            name:
                                type: str
                                description: 'Name.'
                            type:
                                type: str
                                description: 'Subnet segment type.'
                                choices:
                                    - 'any'
                                    - 'specific'
                            value:
                                type: str
                                description: 'Subnet segment value.'
                    tagging:
                        -
                            category:
                                type: str
                                description: 'Tag category.'
                            name:
                                type: str
                                description: 'Tagging entry name.'
                            tags:
                                -
                                    type: str
                    template:
                        type: str
                        description: 'IPv6 address template.'
                    type:
                        type: str
                        description: 'Type of IPv6 address object (default = ipprefix).'
                        choices:
                            - 'ipprefix'
                            - 'iprange'
                            - 'nsx'
                            - 'dynamic'
                            - 'fqdn'
                            - 'template'
                    uuid:
                        type: str
                        description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
                    visibility:
                        type: str
                        description: 'Enable/disable the visibility of the object in the GUI.'
                        choices:
                            - 'disable'
                            - 'enable'
    schema_object1:
        methods: [get]
        description: 'Configure IPv6 firewall addresses.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'cache-ttl'
                            - 'color'
                            - 'comment'
                            - 'end-ip'
                            - 'fqdn'
                            - 'host'
                            - 'host-type'
                            - 'ip6'
                            - 'name'
                            - 'obj-id'
                            - 'sdn'
                            - 'start-ip'
                            - 'template'
                            - 'type'
                            - 'uuid'
                            - 'visibility'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS6
      fmgr_firewall_address6:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     cache-ttl: <value of integer>
                     color: <value of integer>
                     comment: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           cache-ttl: <value of integer>
                           color: <value of integer>
                           comment: <value of string>
                           end-ip: <value of string>
                           fqdn: <value of string>
                           host: <value of string>
                           host-type: <value in [any, specific]>
                           ip6: <value of string>
                           obj-id: <value of string>
                           sdn: <value in [nsx]>
                           start-ip: <value of string>
                           tags: <value of string>
                           template: <value of string>
                           type: <value in [ipprefix, iprange, nsx, ...]>
                           uuid: <value of string>
                           visibility: <value in [disable, enable]>
                     end-ip: <value of string>
                     fqdn: <value of string>
                     host: <value of string>
                     host-type: <value in [any, specific]>
                     ip6: <value of string>
                     list:
                       -
                           ip: <value of string>
                     name: <value of string>
                     obj-id: <value of string>
                     sdn: <value in [nsx]>
                     start-ip: <value of string>
                     subnet-segment:
                       -
                           name: <value of string>
                           type: <value in [any, specific]>
                           value: <value of string>
                     tagging:
                       -
                           category: <value of string>
                           name: <value of string>
                           tags:
                             - <value of string>
                     template: <value of string>
                     type: <value in [ipprefix, iprange, nsx, ...]>
                     uuid: <value of string>
                     visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS6
      fmgr_firewall_address6:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [cache-ttl, color, comment, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/address6'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               cache-ttl:
                  type: int
                  description: 'Minimal TTL of individual IPv6 addresses in FQDN cache.'
               color:
                  type: int
                  description: 'Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1).'
               comment:
                  type: str
                  description: 'Comment.'
               dynamic_mapping:
                  type: array
                  suboptions:
                     _scope:
                        type: array
                        suboptions:
                           name:
                              type: str
                           vdom:
                              type: str
                     cache-ttl:
                        type: int
                     color:
                        type: int
                     comment:
                        type: str
                     end-ip:
                        type: str
                     fqdn:
                        type: str
                     host:
                        type: str
                     host-type:
                        type: str
                     ip6:
                        type: str
                     obj-id:
                        type: str
                     sdn:
                        type: str
                     start-ip:
                        type: str
                     tags:
                        type: str
                     template:
                        type: str
                     type:
                        type: str
                     uuid:
                        type: str
                     visibility:
                        type: str
               end-ip:
                  type: str
                  description: 'Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
               fqdn:
                  type: str
                  description: 'Fully qualified domain name.'
               host:
                  type: str
                  description: 'Host Address.'
               host-type:
                  type: str
                  description: 'Host type.'
               ip6:
                  type: str
                  description: 'IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).'
               list:
                  type: array
                  suboptions:
                     ip:
                        type: str
                        description: 'IP.'
               name:
                  type: str
                  description: 'Address name.'
               obj-id:
                  type: str
                  description: 'Object ID for NSX.'
               sdn:
                  type: str
                  description: 'SDN.'
               start-ip:
                  type: str
                  description: 'First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).'
               subnet-segment:
                  type: array
                  suboptions:
                     name:
                        type: str
                        description: 'Name.'
                     type:
                        type: str
                        description: 'Subnet segment type.'
                     value:
                        type: str
                        description: 'Subnet segment value.'
               tagging:
                  type: array
                  suboptions:
                     category:
                        type: str
                        description: 'Tag category.'
                     name:
                        type: str
                        description: 'Tagging entry name.'
                     tags:
                        type: array
                        suboptions:
                           type: str
               template:
                  type: str
                  description: 'IPv6 address template.'
               type:
                  type: str
                  description: 'Type of IPv6 address object (default = ipprefix).'
               uuid:
                  type: str
                  description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
               visibility:
                  type: str
                  description: 'Enable/disable the visibility of the object in the GUI.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/address6'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/address6',
        '/pm/config/global/obj/firewall/address6'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'cache-ttl': {
                            'type': 'integer'
                        },
                        'color': {
                            'type': 'integer'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'dynamic_mapping': {
                            'type': 'array',
                            'items': {
                                '_scope': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'vdom': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'cache-ttl': {
                                    'type': 'integer'
                                },
                                'color': {
                                    'type': 'integer'
                                },
                                'comment': {
                                    'type': 'string'
                                },
                                'end-ip': {
                                    'type': 'string'
                                },
                                'fqdn': {
                                    'type': 'string'
                                },
                                'host': {
                                    'type': 'string'
                                },
                                'host-type': {
                                    'type': 'string',
                                    'enum': [
                                        'any',
                                        'specific'
                                    ]
                                },
                                'ip6': {
                                    'type': 'string'
                                },
                                'obj-id': {
                                    'type': 'string'
                                },
                                'sdn': {
                                    'type': 'string',
                                    'enum': [
                                        'nsx'
                                    ]
                                },
                                'start-ip': {
                                    'type': 'string'
                                },
                                'tags': {
                                    'type': 'string'
                                },
                                'template': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'ipprefix',
                                        'iprange',
                                        'nsx',
                                        'dynamic',
                                        'fqdn',
                                        'template'
                                    ]
                                },
                                'uuid': {
                                    'type': 'string'
                                },
                                'visibility': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                }
                            }
                        },
                        'end-ip': {
                            'type': 'string'
                        },
                        'fqdn': {
                            'type': 'string'
                        },
                        'host': {
                            'type': 'string'
                        },
                        'host-type': {
                            'type': 'string',
                            'enum': [
                                'any',
                                'specific'
                            ]
                        },
                        'ip6': {
                            'type': 'string'
                        },
                        'list': {
                            'type': 'array',
                            'items': {
                                'ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'obj-id': {
                            'type': 'string'
                        },
                        'sdn': {
                            'type': 'string',
                            'enum': [
                                'nsx'
                            ]
                        },
                        'start-ip': {
                            'type': 'string'
                        },
                        'subnet-segment': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'any',
                                        'specific'
                                    ]
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'tagging': {
                            'type': 'array',
                            'items': {
                                'category': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'tags': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'template': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'ipprefix',
                                'iprange',
                                'nsx',
                                'dynamic',
                                'fqdn',
                                'template'
                            ]
                        },
                        'uuid': {
                            'type': 'string'
                        },
                        'visibility': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'cache-ttl',
                                'color',
                                'comment',
                                'end-ip',
                                'fqdn',
                                'host',
                                'host-type',
                                'ip6',
                                'name',
                                'obj-id',
                                'sdn',
                                'start-ip',
                                'template',
                                'type',
                                'uuid',
                                'visibility'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
                            }
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
        }
    }

    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'add',
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
