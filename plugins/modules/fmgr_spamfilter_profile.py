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
module: fmgr_spamfilter_profile
short_description: Configure AntiSpam profiles.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/spamfilter/profile
    - /pm/config/global/obj/spamfilter/profile
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
        description: 'Configure AntiSpam profiles.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    comment:
                        type: str
                        description: 'Comment.'
                    external:
                        type: str
                        description: 'Enable/disable external Email inspection.'
                        choices:
                            - 'disable'
                            - 'enable'
                    flow-based:
                        type: str
                        description: 'Enable/disable flow-based spam filtering.'
                        choices:
                            - 'disable'
                            - 'enable'
                    name:
                        type: str
                        description: 'Profile name.'
                    options:
                        -
                            type: str
                            choices:
                                - 'bannedword'
                                - 'spamemailbwl'
                                - 'spamfsip'
                                - 'spamfssubmit'
                                - 'spamfschksum'
                                - 'spamfsurl'
                                - 'spamhelodns'
                                - 'spamipbwl'
                                - 'spamraddrdns'
                                - 'spamrbl'
                                - 'spamhdrcheck'
                                - 'spamfsphish'
                                - 'spambwl'
                    replacemsg-group:
                        type: str
                        description: 'Replacement message group.'
                    spam-bwl-table:
                        type: str
                        description: 'Anti-spam black/white list table ID.'
                    spam-bword-table:
                        type: str
                        description: 'Anti-spam banned word table ID.'
                    spam-bword-threshold:
                        type: int
                        description: 'Spam banned word threshold.'
                    spam-filtering:
                        type: str
                        description: 'Enable/disable spam filtering.'
                        choices:
                            - 'disable'
                            - 'enable'
                    spam-iptrust-table:
                        type: str
                        description: 'Anti-spam IP trust table ID.'
                    spam-log:
                        type: str
                        description: 'Enable/disable spam logging for email filtering.'
                        choices:
                            - 'disable'
                            - 'enable'
                    spam-log-fortiguard-response:
                        type: str
                        description: 'Enable/disable logging FortiGuard spam response.'
                        choices:
                            - 'disable'
                            - 'enable'
                    spam-mheader-table:
                        type: str
                        description: 'Anti-spam MIME header table ID.'
                    spam-rbl-table:
                        type: str
                        description: 'Anti-spam DNSBL table ID.'
    schema_object1:
        methods: [get]
        description: 'Configure AntiSpam profiles.'
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
                            - 'comment'
                            - 'external'
                            - 'flow-based'
                            - 'name'
                            - 'options'
                            - 'replacemsg-group'
                            - 'spam-bwl-table'
                            - 'spam-bword-table'
                            - 'spam-bword-threshold'
                            - 'spam-filtering'
                            - 'spam-iptrust-table'
                            - 'spam-log'
                            - 'spam-log-fortiguard-response'
                            - 'spam-mheader-table'
                            - 'spam-rbl-table'
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

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/PROFILE
      fmgr_spamfilter_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     comment: <value of string>
                     external: <value in [disable, enable]>
                     flow-based: <value in [disable, enable]>
                     name: <value of string>
                     options:
                       - <value in [bannedword, spamemailbwl, spamfsip, ...]>
                     replacemsg-group: <value of string>
                     spam-bwl-table: <value of string>
                     spam-bword-table: <value of string>
                     spam-bword-threshold: <value of integer>
                     spam-filtering: <value in [disable, enable]>
                     spam-iptrust-table: <value of string>
                     spam-log: <value in [disable, enable]>
                     spam-log-fortiguard-response: <value in [disable, enable]>
                     spam-mheader-table: <value of string>
                     spam-rbl-table: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/PROFILE
      fmgr_spamfilter_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [comment, external, flow-based, ...]>
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
            example: '/pm/config/adom/{adom}/obj/spamfilter/profile'
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
               comment:
                  type: str
                  description: 'Comment.'
               external:
                  type: str
                  description: 'Enable/disable external Email inspection.'
               flow-based:
                  type: str
                  description: 'Enable/disable flow-based spam filtering.'
               name:
                  type: str
                  description: 'Profile name.'
               options:
                  type: array
                  suboptions:
                     type: str
               replacemsg-group:
                  type: str
                  description: 'Replacement message group.'
               spam-bwl-table:
                  type: str
                  description: 'Anti-spam black/white list table ID.'
               spam-bword-table:
                  type: str
                  description: 'Anti-spam banned word table ID.'
               spam-bword-threshold:
                  type: int
                  description: 'Spam banned word threshold.'
               spam-filtering:
                  type: str
                  description: 'Enable/disable spam filtering.'
               spam-iptrust-table:
                  type: str
                  description: 'Anti-spam IP trust table ID.'
               spam-log:
                  type: str
                  description: 'Enable/disable spam logging for email filtering.'
               spam-log-fortiguard-response:
                  type: str
                  description: 'Enable/disable logging FortiGuard spam response.'
               spam-mheader-table:
                  type: str
                  description: 'Anti-spam MIME header table ID.'
               spam-rbl-table:
                  type: str
                  description: 'Anti-spam DNSBL table ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/spamfilter/profile'

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
        '/pm/config/adom/{adom}/obj/spamfilter/profile',
        '/pm/config/global/obj/spamfilter/profile'
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
                        'comment': {
                            'type': 'string'
                        },
                        'external': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'flow-based': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'options': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'bannedword',
                                    'spamemailbwl',
                                    'spamfsip',
                                    'spamfssubmit',
                                    'spamfschksum',
                                    'spamfsurl',
                                    'spamhelodns',
                                    'spamipbwl',
                                    'spamraddrdns',
                                    'spamrbl',
                                    'spamhdrcheck',
                                    'spamfsphish',
                                    'spambwl'
                                ]
                            }
                        },
                        'replacemsg-group': {
                            'type': 'string'
                        },
                        'spam-bwl-table': {
                            'type': 'string'
                        },
                        'spam-bword-table': {
                            'type': 'string'
                        },
                        'spam-bword-threshold': {
                            'type': 'integer'
                        },
                        'spam-filtering': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spam-iptrust-table': {
                            'type': 'string'
                        },
                        'spam-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spam-log-fortiguard-response': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spam-mheader-table': {
                            'type': 'string'
                        },
                        'spam-rbl-table': {
                            'type': 'string'
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
                                'comment',
                                'external',
                                'flow-based',
                                'name',
                                'options',
                                'replacemsg-group',
                                'spam-bwl-table',
                                'spam-bword-table',
                                'spam-bword-threshold',
                                'spam-filtering',
                                'spam-iptrust-table',
                                'spam-log',
                                'spam-log-fortiguard-response',
                                'spam-mheader-table',
                                'spam-rbl-table'
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
