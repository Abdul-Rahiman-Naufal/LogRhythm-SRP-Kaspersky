# LogRhythm-SRP-Kaspersky

Developed by Abdul Rahiman Naufal - abdulrahimannaufal@gmail.com

LogRhythm SmartResponse for Kaspersky Security Center

This SRP has 5 actions.

1. Save Configuration
2. Isolate Workstation/Server
3. Remove Workstation/Server from Isolation
4. Notify IT Team
5. Get Host Details
6. Get Host Tasks

# Configuration required at Kaspersky Security Center

Refer the attached Kaspersky Settings.png screenshot

1. Create a Group called Isolation
2. Create AV policy for server and workstation.
3. Modify the firewall setting as shown in the attached screenshot.
4. 

# Configuration required at LogRhythm Side

1. Copy the attached configuration file to c:// (If required I can code to create the file automatically, I had no time during development)
2. Import the SmartReponse plugin to LogRhythm using SmartReponse Plugin Manager from LR Console.
3. In Webconsole's SmartResponse panel, Select "Kaspersky SC" and select "Save configuration" action.
4. Input Kaspersky API URL (default https://servername:13999) and credential.
5. Also, provide SMTP details, this is required for "Notify IT" action, which is used to send notification to IT Team.
6. You can also set "Notify IT Team" action to "Malware activity" AIE rule to send notification.
