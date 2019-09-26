'''
Author: Ayanna Benjamin and Randall Marsden
Class Project for GreenHouse
'''

import smtplib

gmail_user = 'ayanbenj19@gmail.com'
gmail_password = ""

sent_from = 'ayanbenj19@gmail.com'
to = ['coolyumi21@gmail.com']
subject = 'SUPER ANNOYING MESSAGE'
body = 'WORKTHING'

email_text = """\
From %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    erver.close()
    
    print("Email sent!")
except:
    print("Something went wrong AGAIN")
