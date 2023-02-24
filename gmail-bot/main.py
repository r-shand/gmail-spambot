#================================================================================================
#
#                           SPAM-BOT version 1.0.2 by Ryan Shand
#
#       THANK YOU FOR USING MY SPAM-BOT. IF YOU HAVE ANY QUESTIONS ON HOW TO OPERATE
#
#    PLEASE CONTACT ME AT info@rshand.com OR DISCORD rshand#6666 OR INSTAGRAM @r.shand
#
#                     I WILL BE HAPPY TO WALK YOU THROUGH AND HELP
#
#================================================================================================

import json
import smtplib
import importlib
from email.message import EmailMessage

def write(data, filename="recipientHistory.json"):
    with open('recipientHistory.json', 'w') as f:
        json.dump(data, f, indent=4)

#email text as string
#BODY = "Hello,\n\nThis is a test message\n\nBest,\nRyan"
#email text as string read from file
message_file = 'message.txt'
with open(message_file, "r") as file:
    BODY = file.read()
#*optional* email text as html
BODY_HTML = """\
<html>
  <body>
    <p>Hello,</p>

    <p>This is an automated email sent from a robot</p>

    <p>Example text in second paragraph</p>

    <p><b>bold example text in html</b> 
    example link: https://www.rshand.com example text example text example text</p>

    <p>Example text here</p>
    
    <p>Kind regards,<br>Ryan</p>
  </body>
</html>
"""
#email subject
SUBJECT = "SUBJECT HERE"
#email of sender
SENDER = 'your_email@gmail.com'
#this is so sender displays name as "Ryan | HotDrop" instead of the email name
FROM = f'"Your Name Here" <your_email@gmail.com>'
#this many emails will be sent to each user. keep this at 1 unless you're feeling a bit malicious
REQUESTS = 1

#list of emails that will receive your message
recipients_file = "list.txt"
with open(recipients_file, "r") as file:
    recipients = [line.strip() for line in file]

history = []
with open('recipientHistory.json') as f:
    data = json.load(f)
for person in data['people']:
    history.append(person['email'])
addNewEmails = []

#smtp server calls
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    #the 'APP PASSWORD' is a app login on gmail. you must enable 2FA then go to gmail settings > security > app password
    #then set up a new app as "SMTP" click generate and you can grab that app password to authorize this program to use your email
    smtpserver.login('your_email@gmail.com', 'APP PASSWORD HERE')
    #counting how many emails we send
    ct = 0
    #looping throigh all recipients in my list initialized earlier
    for r in recipients:
        #initializing and defining out msg object. filling in the attributes before we send our email
        msg = EmailMessage()
        msg['Subject'] = SUBJECT
        msg['From'] = FROM
        msg['To'] = r
        #using string option
        msg.set_content(BODY)
        #using html option. off by default. just uncomment this part out of you would prefer to use html option
        #msg.add_alternative(BODY_HTML, subtype='html')
        #send the email
        if(r not in history):
            addNewEmails.append(r)
            for i in range(REQUESTS):
                ct = ct + 1
                smtpserver.sendmail(SENDER, r, msg.as_string())
            
            if(REQUESTS == 1):
                print("Successfully sent email to:\n", r,"\n")
            elif(REQUESTS > 1):
                print("Successfully spammed ", REQUESTS, " emails to", r, "\n")

if(not addNewEmails):
    print("You have already previously sent out emails to all users on your recipient list. No new emails have been sent out\n")
else:
    print("Successfully sent", str(ct), "emails!")
    
temp = data["people"]
for r in addNewEmails:
    x = {"email": r}
    temp.append(x)

write(data)