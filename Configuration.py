# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import requests

import base64

import json

import urllib3

import os, sys

import xml.etree.ElementTree as ET

'''arg1 = 
   arg2 =
   arg3 =  
   arg4 =
   arg5 = 
   arg6 =
   arg7 =
'''


ksc_server = sys.argv[1]

user = sys.argv[2]

password = sys.argv[3]

mail_from=sys.argv[4]

mail_to=sys.argv[5]

SMTP_Server=sys.argv[6]

Domain=sys.argv[7]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user = base64.b64encode(user.encode('utf-8')).decode("utf-8")

password = base64.b64encode(password.encode('utf-8')).decode("utf-8")

url = ksc_server + "/api/v1.0/login"

session = requests.Session()



auth_headers = {

    'Authorization': 'KSCBasic user="' + user + '", pass="' + password + '", internal="1"',

    'Content-Type': 'application/json',

}



data = {}



response = session.post(url=url, headers=auth_headers, data=data, verify=False)


if(response.status_code==200):

    tree = ET.parse("C:/Program Files/LogRhythm/SmartResponse Plugins/KasperskyConfigFile.xml")

    root = tree.getroot()


    for elem in root.iter('item'):
        
        if(elem.attrib["name"]=="URL"):
            elem.text = ksc_server
        elif(elem.attrib["name"]=="user"):
            elem.text = user
        elif(elem.attrib["name"]=="password"):
            elem.text=password
        elif(elem.attrib["name"]=="from"):
            elem.text=mail_from
        elif(elem.attrib["name"]=="to"):
            elem.text=mail_to 
        elif(elem.attrib["name"]=="SMTP"):
            elem.text=SMTP_Server   
        elif(elem.attrib["name"]=="Domain"):
            elem.text=Domain

    tree.write("C:/Program Files/LogRhythm/SmartResponse Plugins/KasperskyConfigFile.xml")

    print("Configuration saved.")
else:
    print("Invalid Username or Password")
