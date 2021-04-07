from .settings import SenderSettings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = SenderSettings

class SendMail:

    def connect(self):
        server = smtplib.SMTP_SSL(s.host, 465)
        server.login(s.mail,s.password)
        return server
    
    def sendmail(self,to,subject,text,html):
        server = self.connect()
        sender = s.mail
        receiver = to   
        msg = MIMEMultipart()
        msg['From'] = s.mail
        msg['To'] = to
        msg['Subject'] = subject
        #msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        part1 = MIMEText(text, "plain", "utf-8")
        part2 = MIMEText(html, "html", "utf-8")
        msg.attach(part1)
        msg.attach(part2)
        try:

            server.sendmail(sender,receiver,msg.as_string())
            print("Succesfull.")
        except EOFError:
            print("Un Succesfull.")
    
        server.quit()