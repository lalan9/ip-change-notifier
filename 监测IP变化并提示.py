import smtplib
import socket
import json

# 设置文档路径来保存上次的IP地址
ip_file_path = "previous_ip.txt"

# 加载邮件配置信息
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
smtp_username = config['smtp_username']
smtp_password = config['smtp_password']
to_mail = config['to_mail']

# 定义发送邮件函数
def send_email(new_ip):

    # 构建邮件内容
    subject = f"{smtp_username}"
    body = f"New IP: {new_ip}"
    message = f"From: {smtp_username}\nSubject: {subject}\n\n{body}"

    # 连接到SMTP服务器并发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server)
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_mail, message)
        server.quit()
        print("邮件已发送")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

# 获取当前IP地址
current_ip = socket.gethostbyname(socket.gethostname())

# 读取上次保存的IP地址
try:
    with open(ip_file_path, "r") as file:
        old_ips = file.read().splitlines()
except FileNotFoundError:
    old_ips = []

# 如果当前IP地址不在文件中的IP列表中，更新并保存新的IP地址，并发送邮件通知
if current_ip not in old_ips:
    with open(ip_file_path, "a") as file:
        file.write("\n" + current_ip)
    send_email(current_ip)
else:
    print("IP地址未发生变化")
