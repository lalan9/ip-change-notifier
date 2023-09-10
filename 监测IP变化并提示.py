import smtplib
import socket

# 设置文档路径来保存上次的IP地址
ip_file_path = "previous_ip.txt"

# 定义发送邮件函数
def send_email(new_ip):
    # 邮件配置
    smtp_server = "smtp.mail.com"
    smtp_username = "username@example.com"
    smtp_password = "password"    
    to_mail = "to_mail@example.com"
    
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
