# ip-change-notifier
用于监控IP地址更改和发送通知的Python脚本。A Python script for monitoring IP address changes and sending notifications.

## 使用方法
修改config.json，将`smtp_server`、`smtp_username`、`smtp_password`和`to_mail`替换为对应邮箱的服务器、用户名、密码和收件的邮箱。

注意：邮箱需要开启 POP3 服务，第三方登录可能要使用验证码而非密码
