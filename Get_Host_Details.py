# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import requests
import base64
import json
import urllib3
import os, sys
import xml.etree.ElementTree as ET

'''arg1 =  
'''


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


ksc_server = ""
user = ""
password = ""

tree = ET.parse("C:/Program Files/LogRhythm/SmartResponse Plugins/KasperskyConfigFile.xml")
root = tree.getroot()
for elem in root.iter('item'):
    if(elem.attrib["name"]=="URL"):
        ksc_server=elem.text
    elif(elem.attrib["name"]=="user"):
        user = elem.text
    elif(elem.attrib["name"]=="password"):
        password = elem.text

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
data = {"wstrFilter": "", "vecFieldsToReturn": ['id', 'name'], "lMaxLifeTime": 100}
response = session.post(url=url, headers=common_headers, data=json.dumps(data), verify=False)
strAccessor = json.loads(response.text)['strAccessor']

def get_search_results(strAccessor):
    url = ksc_server + "/api/v1.0/ChunkAccessor.GetItemsCount"
    common_headers = {
        'Content-Type': 'application/json',
    }
    data = {"strAccessor": strAccessor}
    response = session.post(url=url, headers=common_headers, data=json.dumps(data), verify=False)
    items_count = json.loads(response.text)['PxgRetVal']
    start = 0
    step = 100000
    results = list()
    while start < items_count:
        url = ksc_server + "/api/v1.0/ChunkAccessor.GetItemsChunk"
        data = {"strAccessor": strAccessor, "nStart": 0, "nCount": items_count}
        response = session.post(url=url, headers=common_headers, data=json.dumps(data), verify=False)
        results += json.loads(response.text)['pChunk']['KLCSP_ITERATOR_ARRAY']
        start += step
    return (results)

groups  = get_search_results(strAccessor = strAccessor)

hostname      = sys.argv[1]
host_id = ""
url = ksc_server + "/api/v1.0/HostGroup.FindHosts"
common_headers = {
    'Content-Type': 'application/json',
}
data = {"wstrFilter": "",
        "vecFieldsToReturn": ['KLHST_WKS_DN', 'KLHST_WKS_HOSTNAME'], "lMaxLifeTime": 100}
response = session.post(url=url, headers=common_headers, data=json.dumps(data), verify=False)
if 'strAccessor' in json.loads(response.text):
    strAccessor = json.loads(response.text)['strAccessor']
    hosts = get_search_results(strAccessor)
    for host in hosts:

        if str(host['value']['KLHST_WKS_DN']).lower()==hostname.lower():
            host_id=host['value']['KLHST_WKS_HOSTNAME']
        
url = ksc_server + "/api/v1.0/HostGroup.GetHostInfo"
common_headers = {
    'Content-Type': 'application/json',
}

virus_count='KLHST_WKS_UNCURED_COUNT'

last_scan='KLHST_WKS_LAST_FULLSCAN'

device_name ='KLHST_WKS_DN'

last_visible="KLHST_WKS_LAST_VISIBLE"

last_Av_update="KLHST_WKS_LAST_UPDATE"

device_type="KLHST_WKS_CTYPE"

host_os="KLHST_WKS_OS_NAME"

host_os_ver="KLHST_WKS_OS_VER_MAJOR"

Realtime_protection="KLHST_WKS_RTP_STATE"

reboot_required="KLHST_WKS_RBT_REQUIRED"

reboot_reason="KLHST_WKS_RBT_REQUEST_REASON"

group_name="name"





data = {"strHostName": host_id, "pFields2Return": [virus_count, last_scan, device_name, last_visible, last_Av_update,

                                                   device_type, host_os, host_os_ver, Realtime_protection, reboot_required, reboot_reason, group_name]}



response = session.post(url=url, headers=common_headers,

                        data=json.dumps(data), verify=False)



print("Device Name: "+json.loads(response.text)['PxgRetVal'][device_name])

print("Branch: " + str(json.loads(response.text)['PxgRetVal'][group_name]))

print("Active Threats: " + str(json.loads(response.text)

                               ['PxgRetVal'][virus_count]['value']))



try:

    print("Last Full Scan: " + json.loads(response.text)

          ['PxgRetVal'][last_scan]['value'])

except Exception:

    pass





try:

    print("Last Visible: " + json.loads(response.text)

          ['PxgRetVal'][last_visible]['value'])

except Exception:

    pass



try:

    if(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 0:



        print("Realtime_protection: Unknown")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 1:



        print("Realtime_protection: Stopped")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 2:



        print("Realtime_protection: Suspended")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 3:



        print("Realtime_protection: Starting ")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 4:



        print("Realtime_protection: Running (if anti-virus application does not support categories of state Running)")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 5:



        print("Realtime_protection: Running with maximum protection")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 6:



        print("Realtime_protection: Running for maximum speed")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 7:



        print("Realtime_protection: Running with recommended settings")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 8:



        print("Realtime_protection: Running with custom settings")



    elif(json.loads(response.text)['PxgRetVal'][Realtime_protection]) == 9:



        print("Realtime_protection: Failure")



except Exception:

    pass



try:

    print("Host OS: " + json.loads(response.text)['PxgRetVal'][host_os])

except Exception:

    pass



try:

    print("Last_AV Update: " + json.loads(response.text)

          ['PxgRetVal'][last_Av_update]['value'])

except Exception:

    pass



try:



    print("Reboot Required: " +

          str(json.loads(response.text)['PxgRetVal'][reboot_required]))



except Exception:



    pass





try:



    if(json.loads(response.text)['PxgRetVal'][reboot_reason] == 0):



        print("Reboot Reason: Reason is unspecified")



    elif(json.loads(response.text)['PxgRetVal'][reboot_reason] == 1):



        print("Reboot Reason: Application is unusable until reboot")



    elif(json.loads(response.text)['PxgRetVal'][reboot_reason] == 2):



        print("Reboot Reason: Application is usable but reboot is required to complete update process")



    elif(json.loads(response.text)['PxgRetVal'][reboot_reason] == 3):



        print("Reboot Reason: Reboot is required to initiate update process")



    elif(json.loads(response.text)['PxgRetVal'][reboot_reason] == 4):



        print("Reboot Reason: Reboot is required to complete scanning/curing")



    elif(json.loads(response.text)['PxgRetVal'][reboot_reason] == 5):

        print("Reboot Reason: Reboot is required to complete installation/uninstallation ")



except Exception:

    pass


