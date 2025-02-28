import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from datetime import datetime

# 送信情報

def send_mail(sendAddress,password,fromAddress,toAddress,image_path,bodyText) -> bool:

    # メール作成
    msg = MIMEMultipart()  # 複数パートを含むメール
    msg['Subject'] = 'Security Alert'
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # HTMLパート
    html = f"""
    <html>
        <body>
            <p>{bodyText}</p>
            <p>Here is the embedded image:</p>
            <img src="cid:image1">
        </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    # 画像添付
    try:
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read(), name='schedule.png')
            img.add_header('Content-ID', '<image1>')  # HTML内で参照するためのID
            img.add_header('Content-Disposition', 'inline', filename='schedule.png')
            msg.attach(img)
    except FileNotFoundError:
        print(f"Error: The image file '{image_path}' was not found.")
        return False

    # SMTPサーバに接続して送信
    try:
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # SMTP_SSLを使用
        smtpobj.login(sendAddress, password)
        smtpobj.send_message(msg)
        print("Email sent successfully!")
        return True
    finally:
        smtpobj.close()
