import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

to_email_list =['jwjwshinjwjw@gamil.com', '1103560988@qq.com', 'wqmlgb55@163.com']
for email. in to_email_list:
    msg = EmailMessage()
    msg['Subject'] = '합격통지서'
    msg['From'] = 'sshksy@naver.com'
    msg['To'] = email
    msg.set_content('ㅊㅋㅊㅋ')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('sshksy', password)
ssafy.send_message(msg)

print('E-mail sended')