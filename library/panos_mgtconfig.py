#!/usr/bin/env python

#  Copyright 2016 Palo Alto Networks, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

DOCUMENTATION = '''
---
module: panos_mgtconfig
short_description: configure management settings of device
description:
    - Configure management settings of device
author: "Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer), Patrik Malinen (@pmalinen)"
version_added: "2.4"
requirements:
    - pan-python
options:
    ip_address:
        description:
            - IP address (or hostname) of PAN-OS device
        required: true
    password:
        description:
            - password for authentication
        required: true
    username:
        description:
            - username for authentication
        required: false
        default: "admin"
    dns_server_primary:
        description:
            - IP address of primary DNS server
        required: false
        default: None
    dns_server_secondary:
        description:
            - IP address of secondary DNS server
        required: false
        default: None
    panorama_primary:
        description:
            - IP address (or hostname) of primary Panorama server
        required: false
        default: None
    panorama_secondary:
        description:
            - IP address (or hostname) of secondary Panorama server
        required: false
        default: None
    ntp_server_primary:
        description:
            - IP address (or hostname) of primary NTP server
        required: false
        default: None
    ntp_server_secondary:
        description:
            - IP address (or hostname) of secondary NTP server
        required: false
        default: None
    commit:
        description:
            - commit if changed
        required: false
        default: true
'''

EXAMPLES = '''
- name: set dns and panorama
  panos_mgtconfig:
    ip_address: "192.168.1.1"
    password: "admin"
    dns_server_primary: "1.1.1.1"
    dns_server_secondary: "1.1.1.2"
    panorama_primary: "1.1.1.3"
    panorama_secondary: "1.1.1.4"
    ntp_server_primary: "1.1.1.5"
    ntp_server_secondary: "1.1.1.6"
'''

RETURN='''
# Default return values
'''

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '1.0'}

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import get_exception

try:
    import pan.xapi
    from pan.xapi import PanXapiError
    HAS_LIB = True
except ImportError:
    HAS_LIB = False

_XPATH_DNS_SERVERS = "/config/devices/entry[@name='localhost.localdomain']" +\
                     "/deviceconfig/system/dns-setting/servers"
_XPATH_PANORAMA_SERVERS = "/config" +\
                          "/devices/entry[@name='localhost.localdomain']" +\
                          "/deviceconfig/system"
_XPATH_NTP_SERVERS = "/config/devices/entry[@name='localhost.localdomain']" +\
                     "/deviceconfig/system/ntp-servers"


def set_dns_server(xapi, new_dns_server, primary=True):
    if primary:
        tag = "primary"
    else:
        tag = "secondary"
    xpath = _XPATH_DNS_SERVERS+"/"+tag

    # check the current element value
    xapi.get(xpath)
    val = xapi.element_root.find(".//"+tag)
    if val is not None:
        # element exists
        val = val.text
    if val == new_dns_server:
        return False

    element = "<%(tag)s>%(value)s</%(tag)s>" %\
              dict(tag=tag, value=new_dns_server)
    xapi.edit(xpath, element)

    return True


def set_panorama_server(xapi, new_panorama_server, primary=True):
    if primary:
        tag = "panorama-server"
    else:
        tag = "panorama-server-2"
    xpath = _XPATH_PANORAMA_SERVERS+"/"+tag

    # check the current element value
    xapi.get(xpath)
    val = xapi.element_root.find(".//"+tag)
    if val is not None:
        # element exists
        val = val.text
    if val == new_panorama_server:
        return False

    element = "<%(tag)s>%(value)s</%(tag)s>" %\
              dict(tag=tag, value=new_panorama_server)
    xapi.edit(xpath, element)

    return True


def set_ntp_server(xapi, new_ntp_server, primary=True):
    if primary:
        tag = "ntp-server-address"
        xpath = _XPATH_NTP_SERVERS + "/primary-ntp-server/" + tag
    else:
        tag = "ntp-server-address"
        xpath = _XPATH_NTP_SERVERS+"/secondary-ntp-server/"+tag

    # check the current element value
    xapi.get(xpath)
    val = xapi.element_root.find(".//"+tag)
    if val is not None:
        # element exists
        val = val.text
    if val == new_ntp_server:
        return False

    element = "<%(tag)s>%(value)s</%(tag)s>" %\
              dict(tag=tag, value=new_ntp_server)
    xapi.edit(xpath, element)

    return True


def main():
    argument_spec = dict(
        ip_address=dict(required=True),
        password=dict(required=True, no_log=True),
        username=dict(default='admin'),
        dns_server_primary=dict(),
        dns_server_secondary=dict(),
        panorama_primary=dict(),
        panorama_secondary=dict(),
        ntp_server_primary=dict(),
        ntp_server_secondary=dict(),
        commit=dict(type='bool', default=True)
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    if not HAS_LIB:
        module.fail_json(msg='pan-python is required for this module')

    ip_address = module.params["ip_address"]
    password = module.params["password"]
    username = module.params['username']
    dns_server_primary = module.params['dns_server_primary']
    dns_server_secondary = module.params['dns_server_secondary']
    ntp_server_primary = module.params['ntp_server_primary']
    ntp_server_secondary = module.params['ntp_server_secondary']
    panorama_primary = module.params['panorama_primary']
    panorama_secondary = module.params['panorama_secondary']
    commit = module.params['commit']

    xapi = pan.xapi.PanXapi(
        hostname=ip_address,
        api_username=username,
        api_password=password
    )

    changed = False
    try:
        if dns_server_primary is not None:
            changed |= set_dns_server(xapi, dns_server_primary, primary=True)
        if dns_server_secondary is not None:
            changed |= set_dns_server(xapi, dns_server_secondary, primary=False)
        if panorama_primary is not None:
            changed |= set_panorama_server(xapi, panorama_primary, primary=True)
        if panorama_secondary is not None:
            changed |= set_panorama_server(xapi, panorama_secondary, primary=False)
        if ntp_server_primary is not None:
            changed |= set_ntp_server(xapi, ntp_server_primary, primary=True)
        if ntp_server_secondary is not None:
            changed |= set_ntp_server(xapi, ntp_server_secondary, primary=False)

        if changed and commit:
            xapi.commit(cmd="<commit></commit>", sync=True, interval=1)
    except PanXapiError:
        exc = get_exception()
        module.fail_json(msg=exc.message)

    module.exit_json(changed=changed, msg="okey dokey")

if __name__ == '__main__':
    main()
