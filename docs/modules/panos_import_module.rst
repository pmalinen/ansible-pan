.. _panos_import:


panos_import - import file on PAN-OS devices
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3


.. contents::
   :local:
   :depth: 1


Synopsis
--------

Import file on PAN-OS device


Requirements (on host that executes module)
-------------------------------------------

  * pan-python
  * requests
  * requests_toolbelt


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
    <td>category<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>software</td>
        <td><ul></ul></td>
        <td><div>Category of file uploaded. The default is software.</div></td></tr>
            <tr>
    <td>file<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>None</td>
        <td><ul></ul></td>
        <td><div>Location of the file to import into device.</div></td></tr>
            <tr>
    <td>ip_address<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>IP address (or hostname) of PAN-OS device.</div></td></tr>
            <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Password for device authentication.</div></td></tr>
            <tr>
    <td>url<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>None</td>
        <td><ul></ul></td>
        <td><div>URL of the file that will be imported to device.</div></td></tr>
            <tr>
    <td>username<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>admin</td>
        <td><ul></ul></td>
        <td><div>Username for device authentication.</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    # import software image PanOS_vm-6.1.1 on 192.168.1.1
    - name: import software image into PAN-OS
      panos_import:
        ip_address: 192.168.1.1
        username: admin
        password: admin
        file: /tmp/PanOS_vm-6.1.1
        category: software



