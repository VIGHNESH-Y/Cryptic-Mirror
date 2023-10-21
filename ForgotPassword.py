import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import tkinter.messagebox as Mb

if __name__ == "__main__":
    Mb.showinfo("Wrong File" , "Please start with PlayCrypticMirror.py")

def MailNow(TO, NICKNAME, gmail_passwd , PASSWORD):

 

    gmail_sender = 'crypticmirror8@gmail.com'

 

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Forgot Password"
    msg['From'] = gmail_sender
    msg['To'] = TO
    CURRENT_TIME = time.ctime()

 

    html = f"""\

 

<!DOCTYPE html>
<html>
<head>

 

</head>
<body style="font-family: arial;">
    <p>
    <b style="color: red; font-size: 250%; font-family: Fantasy">Cryptic Mirror</b>
    <br>
    <br>
        Hello {NICKNAME},
    <br>
    <br>
        We have received a request that you've have forgotten your password
    <br>
    <br>
        Here are few details;
    <br>
    <br>
        <b>Time: </b>{CURRENT_TIME}
        <br>
        <b>Email ID: </b>{TO}
        <br>
        <b>Password: </b>{PASSWORD}
    <br>
    <br>
        If your have not made this request, please ignore it, your account is secure.
    <br>

        If you did forget your password, you're good to go!
    <br>
        Try to remember your password in the future. :)
    <br>
    <br>
        <b>Sincerely,</b>
    <br>
        <b>Team Cryptic Mirror</b>
    

 

    <br>
    <br>
    <br>
    <left style="font-family: consolas; font-size: 70%;">This is an automatically generated mail</left>
    <br>
    <left style="font-family: consolas; font-size: 80%;">For any querries or suggestions,  contact us at </left>
    <left style="color: blue; font-family: consolas; font-size: 85%";>crypticmirror8@gmail.com</left>

 

    </p>
</body>
</html>

 

    """

 

    part2 = MIMEText(html, 'html')

 

    msg.attach(part2)
    
    MailServer = smtplib.SMTP('smtp.gmail.com', 587)
    MailServer.ehlo()
    MailServer.starttls()
    MailServer.login(gmail_sender, gmail_passwd)

 

    try:
        MailServer.sendmail(gmail_sender, TO, msg.as_string())
        MailServer.quit()
    except:
        MailServer.quit()
        return False

 
