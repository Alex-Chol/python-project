import smtplib
from email.mime.text import MIMEText
from email.header import Header
qqmail = smtplib.SMTP_SSL('smtp.qq.com',465)
# 登录服务器
user = '377730739@qq.com'
pas = 'bvyttafhzamxbjci'
qqmail.login(user,pas)
# 登录邮箱账号
theme = 'Hello'
text = '\n\n'+input('请输入邮件内容：\n')
recipient = '787001245@qq.com'
sender = '德芙丶巧克力'
# 输入内容
message = MIMEText(text,'plain','utf-8')
message['Subject'] = Header(theme,'utf-8')
message['From'] = Header(sender,'utf-8')
try:
    qqmail.sendmail(user,recipient,message.as_string())
except:
    print('发送失败，请重试!')
qqmail.quit()