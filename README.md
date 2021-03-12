# LogRhythm-SRP-Kaspersky

Developed by Abdul Rahiman Naufal - abdulrahimannaufal@gmail.com

LogRhythm SmartResponse for Kaspersky Security Center

This SRP has 6 actions.

1. Save Configuration
2. Isolate Workstation/Server
3. Remove Workstation/Server from Isolation
4. Notify IT Team
5. Get Host Details
6. Get Host Tasks

# Configuration required at Kaspersky Security Center

1. Create a Group called Isolation in Kaspersky SC
2. Create AV policies for server and workstation and assign to Isolation group.
3. Modify the firewall setting as shown in the attached screenshot.(Refer the attached "Kaspersky Settings.png" screenshot)

# Configuration required at LogRhythm Side

1. Copy the attached configuration file ("KasperskyConfigFile.xml") to "C:\Program Files\LogRhythm\SmartResponse Plugins\" (I had no time to code for auto creation of the file during development, let me know if you guys want me to code it)
2. Import the SmartReponse plugin to LogRhythm using SmartReponse Plugin Manager from LR Console.
3. In LR Webconsole SmartResponse panel, Select "Kaspersky SC" and select "Save configuration" action.
4. Input Kaspersky API URL (default https://servername:13299) and credential.
5. Also, provide SMTP details, this is required for "Notify IT" action, which is used to send notification to IT Team.
6. You can also set "Notify IT Team" action to "Malware activity" AIE rule to send notification.
