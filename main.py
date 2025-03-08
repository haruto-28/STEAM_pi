from datetime import datetime
from Utils.notify import send_mail
import Utils.picture

with open("pass.txt", "r") as file:
    password = file.read()

send_mail("s3cur1t7St3am@gmail.com",password,"fidgetman2008@gmail.com","fidgetman2008@gmail.com","enn.JPG",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))