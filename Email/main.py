import base64
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Email:
    def __init__(self,
                 data='测试文本',
                 from_name="何佑希",
                 to_name="何锦晴",
                 connect="smtp.qq.com",
                 email_main="测试",
                 Password="tgktvjzooxdbbdgc",  # 密钥为测试专用 请重新获取.
                 from_email="676105282@qq.com",
                 To_email=None
                 ):
        if To_email is None:
            To_email = ["676105282@qq.com"]
        self.message = MIMEText(data)  # 邮件内容
        self.fromName64 = base64.b64encode(bytes(from_name, 'utf-8'))  # b'xxxx'转为'xxxx'
        self.fromName64str = str(self.fromName64, 'utf-8')  # 尖括号拼接用双引号
        self.fromNamestr = '"=?utf-8?B?' + self.fromName64str + '=?=" <' + "676105282@qq.com" + ">"
        self.to_name = to_name
        self.email_main = email_main
        self.Password = Password
        self.from_email = from_email
        self.To_email = To_email
        self.mail = smtplib.SMTP()
        self.mail.connect(connect)  # 连接 qq 邮箱
        self.message['From'] = Header(self.fromNamestr)
        self.message['To'] = Header(self.to_name)  # 邮件接收者名字
        self.message['Subject'] = Header(self.email_main)  # 邮件主题

    def Email(self):
        try:
            self.mail.login(self.from_email, self.Password)  # 账号和授权码
            self.mail.sendmail(self.from_email, self.To_email, self.message.as_string())  # 发送账号、接收账号和邮件信息
            return "<200>"
        except:
            return "<404>"


if __name__ == '__main__':
    data = Email(data="测试文本",
                 from_name="何佑希",
                 to_name="何锦晴",
                 connect="smtp.qq.com",
                 email_main="测试文本",
                 Password="tgktvjzooxdbbdgc",
                 from_email="676105282@qq.com",
                 To_email=["q.w.e.a.s@icloud.com"]
                 ).Email()
    print(data)
