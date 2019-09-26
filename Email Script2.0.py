'''
Author: Ayanna Benjamin and Randall Marsden
Class Project for GreenHouse
'''
import smtplib

def sendemail(from_addr = 'ayanbenj19@gmail.com',
              to_addr_list = 'coolyumi21@gmail.com', 
              cc_addr_list = 'afbenjam@utica.edu',
              subject = 'Test email',
              message = 'please work for the love of god',
              login = 'ayanbenj19', 
              password = '',
              smtpserver = 'smtp.gmail.com:587'):
    header = 'From: %s' % from_addr
    header += 'To: %s' % ','.join(to_addr_list)
    header += 'Cc: %s' % ','.join(cc_addr_list)
    header += 'Subject: %s' % subject 
    message = header + message
    
    server = smtplib.SMTP(smtpserver)
    serever.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
    