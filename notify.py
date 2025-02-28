import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from datetime import datetime

# 送信情報


class email_sender:
    
    def __init__(self,sendAddress,password,fromAddress,toAddress,image_path):

        self.sendAddress = sendAddress  # 自分のアドレス
        self.password = password  # App Passwordを入力
        self.subject = 'Security Alert'
        self.bodyText = f'Too many attempts at logging in at{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        self.fromAddress = fromAddress  # 自分のメールアドレス
        self.toAddress = toAddress  # 送信先のメールアドレス
        self.image_path = image_path  # 埋め込みたい画像のパス
    
    def send_mail(self) -> bool:

        # メール作成
        msg = MIMEMultipart()  # 複数パートを含むメール
        msg['Subject'] = self.subject
        msg['From'] = self.fromAddress
        msg['To'] = self.toAddress
        msg['Date'] = formatdate()

        # HTMLパート
        html = f"""
        <html>
            <body>
                <p>{self.bodyText}</p>
                <p>Here is the embedded image:</p>
                <img src="cid:image1">
            </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))

        # 画像添付
        try:
            with open(self.image_path, 'rb') as img_file:
                img = MIMEImage(img_file.read(), name='schedule.png')
                img.add_header('Content-ID', '<image1>')  # HTML内で参照するためのID
                img.add_header('Content-Disposition', 'inline', filename='schedule.png')
                msg.attach(img)
        except FileNotFoundError:
            print(f"Error: The image file '{self.image_path}' was not found.")
            return False

        # SMTPサーバに接続して送信
        try:
            smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # SMTP_SSLを使用
            smtpobj.login(self.sendAddress, self.password)
            smtpobj.send_message(msg)
            print("Email sent successfully!")
            return True
        finally:
            smtpobj.close()
