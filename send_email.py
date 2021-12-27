import smtplib
import os
from datetime import date, datetime
from email.message import EmailMessage


def send_email():
    try:
        gmailaddress  = os.environ.get('SMTP_USERNAME')
        gmailpassword = os.environ.get('SMTP_PASSWORD')
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        subject = 'Test Email'
        message = 'This email is a test at: '+str(dt_string)
        thanks = 'Sincerely, Me'
        msg = 'Subject: {}\n\n{}\n\n{}'.format(subject, message, thanks)
        mailto        = 'username@gmail.com'
        mailServer = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        mailServer.quit()
        return 'Email sent successfully!'
    except:
        return 'Email failed to send!'    

print(send_email())