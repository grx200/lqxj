import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendEmail():
    def __init__(self, file_name):
        self.file_name = file_name
        self.send_user = "1833013613@qq.com" #发送邮箱的帐号
        self.password = "mwcmkhfsfsledhbh"              #发送邮箱的授权码而不是邮箱密码
        self.email_host = "smtp.qq.com"     #发送邮箱的服务器地址 qq邮箱是'smtp.qq.com', 136邮箱是'smtp.136.com'
        # self.receivers = ['grx15528338252@163.com']

    def send_mail(self,user_list,sub,content):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = self.send_user    #发件人
        message['To'] = ";".join(user_list) #收件人
        message['Subject'] = sub  #主题

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件（附件为HTML格式的网页）
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        att = MIMEText(open(self.file_name, 'rb').read(), 'html', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s_MyReport.html"'%now
        message.attach(att)

        #发送
        server = smtplib.SMTP_SSL(self.email_host,465)
        # server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
        server.login(self.send_user,self.password)
        server.sendmail(self.send_user,user_list,message.as_string())
        server.quit()#关闭连接

    def send_main(self):
        # user_list = ['xxx@qq.com','xxx@qq.com']
        user_list = ['grx15528338252@163.com'] #收件人集合
        sub = "测试报告"        #主题
        content = "测试结果:见附件" #正文
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    send =  SendEmail(file_name='..\\reports\\dwbgsq.html')
    send.send_main()