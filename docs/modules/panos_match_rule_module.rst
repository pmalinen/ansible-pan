.. _panos_match_rule:


panos_match_rule - Test for match against a security rule on PAN-OS devices or Panorama management console.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 1


Synopsis
--------

S
e
c
u
r
i
t
y
 
p
o
l
i
c
i
e
s
 
a
l
l
o
w
 
y
o
u
 
t
o
 
e
n
f
o
r
c
e
 
r
u
l
e
s
 
a
n
d
 
t
a
k
e
 
a
c
t
i
o
n
,
 
a
n
d
 
c
a
n
 
b
e
 
a
s
 
g
e
n
e
r
a
l
 
o
r
 
s
p
e
c
i
f
i
c
 
a
s
 
n
e
e
d
e
d
.
 
T
h
e
 
p
o
l
i
c
y
 
r
u
l
e
s
 
a
r
e
 
c
o
m
p
a
r
e
d
 
a
g
a
i
n
s
t
 
t
h
e
 
i
n
c
o
m
i
n
g
 
t
r
a
f
f
i
c
 
i
n
 
s
e
q
u
e
n
c
e
,
 
a
n
d
 
b
e
c
a
u
s
e
 
t
h
e
 
f
i
r
s
t
 
r
u
l
e
 
t
h
a
t
 
m
a
t
c
h
e
s
 
t
h
e
 
t
r
a
f
f
i
c
 
i
s
 
a
p
p
l
i
e
d
,
 
t
h
e
 
m
o
r
e
 
s
p
e
c
i
f
i
c
 
r
u
l
e
s
 
m
u
s
t
 
p
r
e
c
e
d
e
 
t
h
e
 
m
o
r
e
 
g
e
n
e
r
a
l
 
o
n
e
s
.




Requirements (on host that executes module)
-------------------------------------------

  * pan-python can be obtained from PyPi https://pypi.python.org/pypi/pan-python
  * pandevice can be obtained from PyPi https://pypi.python.org/pypi/pandevice


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
            <tr>
    <td>api_key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>API key that can be used instead of <em>username</em>/<em>password</em> credentials.</div></td></tr>
            <tr>
    <td>application<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The application.</div></td></tr>
            <tr>
    <td>destination_ip<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The destination IP address.</div></td></tr>
            <tr>
    <td>destination_port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The destination port.</div></td></tr>
            <tr>
    <td>destination_zone<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The destination zone.</div></td></tr>
            <tr>
    <td>ip_address<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>IP address (or hostname) of PAN-OS device being configured.</div></td></tr>
            <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Password credentials to use for auth unless <em>api_key</em> is set.</div></td></tr>
            <tr>
    <td>protocol<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The IP protocol number [1-255].</div></td></tr>
            <tr>
    <td>rule_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>security</td>
        <td><ul></ul></td>
        <td><div>Type of rule. Valid types are <em>security</em> or <em>nat</em>.</div></td></tr>
            <tr>
    <td>source_ip<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The source IP address.</div></td></tr>
            <tr>
    <td>source_user<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The source user or group.</div></td></tr>
            <tr>
    <td>source_zone<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The source zone.</div></td></tr>
            <tr>
    <td>to_interface<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The inbound interface in a NAT rule.</div></td></tr>
            <tr>
    <td>username<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>admin</td>
        <td><ul></ul></td>
        <td><div>Username credentials to use for auth unless <em>api_key</em> is set.</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    - name: check security rules for Google DNS
      panos_match_rule:
        ip_address: '{{ ip_address }}'
        username: '{{ username }}'
        password: '{{ password }}'
        rule_type: 'security'
        source_ip: '10.0.0.0'
        destination_ip: '8.8.8.8'
        application: 'dns'
        destination_port: '53'
        protocol: '17'
      register: result
    - debug: msg='{{result.stdout_lines}}'
    
    - name: check security rules inbound SSH with user match
      panos_match_rule:
        ip_address: '{{ ip_address }}'
        username: '{{ username }}'
        password: '{{ password }}'
        rule_type: 'security'
        source_ip: '0.0.0.0'
        source_user: 'mydomain\jsmith'
        destination_ip: '192.168.100.115'
        destination_port: '22'
        protocol: '6'
      register: result
    - debug: msg='{{result.stdout_lines}}'
    
    - name: check NAT rules for source NAT
      panos_match_rule:
        ip_address: '{{ ip_address }}'
        username: '{{ username }}'
        password: '{{ password }}'
        rule_type: 'nat'
        source_zone: 'Prod-DMZ'
        source_ip: '10.10.118.50'
        to_interface: 'ethernet1/2'
        destination_zone: 'Internet'
        destination_ip: '0.0.0.0'
        protocol: '6'
      register: result
    - debug: msg='{{result.stdout_lines}}'
    
    - name: check NAT rules for inbound web
      panos_match_rule:
        ip_address: '{{ ip_address }}'
        username: '{{ username }}'
        password: '{{ password }}'
        rule_type: 'nat'
        source_zone: 'Internet'
        source_ip: '0.0.0.0'
        to_interface: 'ethernet1/1'
        destination_zone: 'Prod DMZ'
        destination_ip: '192.168.118.50'
        destination_port: '80'
        protocol: '6'
      register: result
    - debug: msg='{{result.stdout_lines}}'
    
    - name: check security rules for outbound POP3 in vsys4
      panos_match_rule:
        ip_address: '{{ ip_address }}'
        username: '{{ username }}'
        password: '{{ password }}'
        vsys_id: 'vsys4'
        rule_type: 'security'
        source_ip: '10.0.0.0'
        destination_ip: '4.3.2.1'
        application: 'pop3'
        destination_port: '110'
        protocol: '6'
      register: result
    - debug: msg='{{result.stdout_lines}}'


Notes
-----

.. note:: Checkmode is not supported.
.. note:: Panorama NOT is supported.

