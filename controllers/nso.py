"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from jinja2 import Environment
from jinja2 import FileSystemLoader
from constants import *
import requests
import json
import base64
import os


DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))
requests.packages.urllib3.disable_warnings()

class NsoController:
    url = NSO_URL
    credentials = NSO_USER + ":" + NSO_PASSWORD

    def makeCall(self, p_url, method, data="", headers={}):
        """
        Basic method to make a call. Please this one to all the calls that you want to make
        :param p_url: NSO URL
        :param method: POST/GET/DELETE
        :param data: Payload to send
        :param headers: Headers to send
        :return:
        """
        # Debug
        print("Sending " + method + " request to NSO: " + p_url)
        print(data)
        headers["Authorization"] = "Basic " + base64.b64encode(bytes(self.credentials, "utf-8")).decode("utf-8")

        if method == "POST":
            response = requests.post(self.url + p_url, data=data, headers=headers, verify=False)
        elif method == "GET":
            response = requests.get(self.url + p_url, headers=headers, verify=False)
        elif method == "DELETE":
            response = requests.delete(self.url + p_url, headers=headers, verify=False, data="")
        else:
            raise Exception("Method not supported")
        if 199 > response.status_code > 300:
            errorMessage = json.loads(response.text)["errorDocument"]["message"]
            raise Exception("Error: status code" + str(response.status_code) + " - " + errorMessage)
        return response

    def syncFromDevices(self):
        """
        Sync database from all devices
        :return:
        """
        p_url = "api/running/devices/_operations/sync-from"
        method = "POST"
        headers = {"Content-Type": "application/vnd.yang.operation+json"}
        self.makeCall(p_url=p_url, headers=headers, method=method)


    def deployOCCHCcircuit(self, serviceName, site1, site2, link1, link2):
        """
        Deploy an OCCHC circuit in NSO
        :param serviceName:
        :param site1:
        :param site2:
        :param link1:
        :param link2:
        :return:
        """
        p_url = "api/running/devices/device/" + EPNM_DEVICE_NAME + "/config/epnm:cisco-service-network/"
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "POST"
        template = JSON_TEMPLATES.get_template('create_optical_circuit.j2.json')
        payload = template.render(name=serviceName, start_point=site1, end_point=site2, start_link=link1, end_link=link2)
        self.makeCall(p_url=p_url, headers=headers, method=method, data=payload)


    def deleteOCCHCcircuit(self, serviceName):
        """
        Delete an OCCHC circuit in NSO
        :param serviceName:
        :return:
        """
        p_url = "api/running/devices/device/" + EPNM_DEVICE_NAME + "/config/epnm:cisco-service-network/services/" + serviceName
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "DELETE"
        self.makeCall(p_url=p_url, headers=headers, method=method)


    def createInternalPatch(self,siteName, aEndTp, zEndTp):
        """
        Create an Internal Patch cord for optical circuit in NSO
        :param siteName:
        :param aEndTp:
        :param zEndTp:
        :return:
        """
        p_url = "api/running/devices/device/" + EPNM_DEVICE_NAME + "/config/epnm:cisco-service-network/"
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "POST"
        template = JSON_TEMPLATES.get_template('create_int_patch.j2.json')
        payload = template.render(site_name=siteName, start_point=aEndTp, end_point=zEndTp)
        self.makeCall(p_url=p_url, headers=headers, method=method, data=payload)


    def addDevice(self,deviceName, ipaddress, port):
        """
        Add a device to NSO
        :param deviceName:
        :param ipaddress:
        :param port:
        :return:
        """
        p_url = "api/running/devices"
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "POST"
        template = JSON_TEMPLATES.get_template('create_device.j2.json')
        payload = template.render(name=deviceName, ip_address=ipaddress, port=port)
        self.makeCall(p_url=p_url, headers=headers, method=method, data=payload)

    def deleteInternalPatch(self, siteName, aEndTp, zEndTp):
        """
        Delete an Internal Patch cord for optical circuit in NSO
        :param siteName:
        :param aEndTp:
        :param zEndTp:
        :return:
        """
        p_url = "api/running/devices/device/" + EPNM_DEVICE_NAME + "/config/epnm:cisco-service-network/patch-cord-list/" + siteName + "," + aEndTp + "," + zEndTp
        headers = {"Content-Type": "application/vnd.yang.data+json"}
        method = "DELETE"
        self.makeCall(p_url=p_url, headers=headers, method=method)