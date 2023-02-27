Hello,

Thank you for using my spam-bot
version 1.0.3 updated 26 February 2023
https://github.com/r-shand

Installation Requirements:
Python3
Any IDE for Python (recommended VS Code)

SUPPORT / CONTACT: 
email: info@rshand.com
discord rshand#6666
instagram @r.shand

Please read for instructions

1) format 'list.txt' as templated: 1 email address per line, no spaces or extra characters other than the email
address itself. My code is not programmed to filter through unnecessary characters or whitespaces

2) if you don't know how to code in HTML and are using the read from 'message.txt' file please type
the ENTIRE email in the file. if you copy and paste the text from your browser or another file,
the text may not display correctly when you send the email and you may see some weird non-alphanumeric characters

3) ***ENABLING APP PASSWORD***
    1) go to your google account settings. set up 2-Factor Authentication
    2) navigate to settings > security > find or search "app password"
    3) under 'select app' choose 'other' and type 'SMTP' then click generate. copy this app password
    4) on line 79 on my code (or whereever the below statement is), paste your app password where it says 'app password here'
    smtpserver.login('ryan.hotdropapp@gmail.com', 'app password here')

4) IN ALL AREAS OF CODE: replace example@gmail.com with your gmail!

Known Limitation(s)
- HTML embeds of images display as null image icons when sending email, because of this, I have not implemented a signature feature 
- Only works for senders using gmail emails or any domain email that is managed by google domains



