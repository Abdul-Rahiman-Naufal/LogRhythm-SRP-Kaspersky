# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import requests
import base64
import json
import urllib3
import os
import sys
import xml.etree.ElementTree as ET
'''arg1 =  

'''

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ksc_server = ""
user = ""
password = ""
Domain=""

tree = ET.parse("C:/Program Files/LogRhythm/SmartResponse Plugins/KasperskyConfigFile.xml")
root = tree.getroot()

for elem in root.iter('item'):

    if(elem.attrib["name"] == "URL"):

        ksc_server = elem.text

    elif(elem.attrib["name"] == "user"):

        user = elem.text

    elif(elem.attrib["name"] == "password"):

        password = elem.text

    elif(elem.attrib["name"] == "Domain"):

        Domain = elem.text

url = ksc_server + "/api/v1.0/login"


session = requests.Session()


auth_headers = {

    'Authorization': 'KSCBasic user="' + user + '", pass="' + password + '", internal="1"',

    'Content-Type': 'application/json',

}


data = {}


response = session.post(url=url, headers=auth_headers, data=data, verify=False)


url = ksc_server + "/api/v1.0/HostGroup.FindGroups"

common_headers = {

    'Content-Type': 'application/json',

}

data = {"wstrFilter": "", "vecFieldsToReturn": [
    'id', 'name'], "lMaxLifeTime": 100}

response = session.post(url=url, headers=common_headers,
                        data=json.dumps(data), verify=False)

strAccessor = json.loads(response.text)['strAccessor']


def get_search_results(strAccessor):

    url = ksc_server + "/api/v1.0/ChunkAccessor.GetItemsCount"

    common_headers = {

        'Content-Type': 'application/json',

    }

    data = {"strAccessor": strAccessor}

    response = session.post(url=url, headers=common_headers,
                            data=json.dumps(data), verify=False)

    items_count = json.loads(response.text)['PxgRetVal']

    start = 0

    step = 100000

    results = list()

    while start < items_count:

        url = ksc_server + "/api/v1.0/ChunkAccessor.GetItemsChunk"

        data = {"strAccessor": strAccessor, "nStart": 0, "nCount": items_count}

        response = session.post(
            url=url, headers=common_headers, data=json.dumps(data), verify=False)

        results += json.loads(response.text)['pChunk']['KLCSP_ITERATOR_ARRAY']

        start += step

    return (results)

hostname = sys.argv[1]

host_id = ""

url = ksc_server + "/api/v1.0/HostGroup.FindHosts"

common_headers = {

    'Content-Type': 'application/json',

}

data = {"wstrFilter": "",

        "vecFieldsToReturn": ['KLHST_WKS_DN', 'KLHST_WKS_HOSTNAME'], "lMaxLifeTime": 100}

response = session.post(url=url, headers=common_headers,
                        data=json.dumps(data), verify=False)

if 'strAccessor' in json.loads(response.text):

    strAccessor = json.loads(response.text)['strAccessor']

    hosts = get_search_results(strAccessor)

    for host in hosts:

        if str(host['value']['KLHST_WKS_DN']).lower() == hostname.lower():

            host_id = host['value']['KLHST_WKS_HOSTNAME']


url = ksc_server + "/api/v1.0/Tasks.GetAllTasksOfHost"

common_headers = {

    'Content-Type': 'application/json',

}

data = {"strDomainName": Domain, "strHostName": host_id}

response = session.post(url=url, headers=common_headers,
                        data=json.dumps(data), verify=False)

host_tasks = json.loads(response.text)['PxgRetVal']


for task in host_tasks:

    url = ksc_server + "/api/v1.0/Tasks.GetTask"

    common_headers = {

        'Content-Type': 'application/json',

    }

    data = {"strTask": task}

    response = session.post(url=url, headers=common_headers,
                            data=json.dumps(data), verify=False)

    task_name = json.loads(response.text)['PxgRetVal']

    print(task + " : "+task_name["DisplayName"])
