# Devleoped by Abdul Rahiman Naufal
# abdulrahimannaufal@gmail.com

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xml.etree.ElementTree as ET

'''arg1 =  
   arg2 = 
   arg3 =  
'''

host=sys.argv[1]
object_name=sys.argv[2]
virus_hash=sys.argv[3]
SMTP_Server=""


tree = ET.parse("C:/Program Files/LogRhythm/SmartResponse Plugins/KasperskyConfigFile.xml")

root = tree.getroot()

for elem in root.iter('item'):
    if(elem.attrib["name"]=="from"):
        mail_From=elem.text
    elif(elem.attrib["name"]=="to"):
        mail_To = elem.text
    elif(elem.attrib["name"]=="SMTP"):
        SMTP_Server = elem.text


mail_To=list(mail_To.split(",")) 

msg = MIMEMultipart()
subject = "Virus found in host."

html = """\
<html>
  <head></head>
  <body>
    <p>Dear Team,<br>
      <br>
      Virus is found in below device.
      <br><br>
     
       <table style="width: 100%;">
        <tr>
            <td style="font-weight: bold; width: 61px;" class="modal-sm">Host:</td>
            <td style="color: #FF0000">"""+host+"""</td>
        </tr>
        <tr>
            <td style="font-weight: bold; width: 61px;" class="modal-sm">Object:</td>
            <td style="color: #FF0000">"""+object_name+"""</td>
        </tr>
         <tr>
            <td style="font-weight: bold; width: 61px;" class="modal-sm">Hash:</td>
            <td style="color: #FF0000">"""+virus_hash+"""</td>
        </tr>
    </table>
    </p>
  </body>
</html>
"""

msg['From'] = mail_From
msg['To'] = ", ".join(mail_To)
msg['Subject'] = subject
msg.attach(MIMEText(html, 'html'))
text=msg.as_string()
s = smtplib.SMTP(SMTP_Server)
s.sendmail(mail_From,mail_To, text)
s.quit()
print("Mail sent successfully.")





