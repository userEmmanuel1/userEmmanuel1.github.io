import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
from flask import Flask, request
app = Flask(__name__)
import multiprocessing





def send_email(email_sms_value, tracking_stocks, selected_option):
    # Email sender configuration
    smtp_port = 587
    smtp_server = "smtp.gmail.com"
    email_from = "investiwatchers@gmail.com"
    pw = "kjru uvwz idmd cnjt"

    # API KEY FOR INVESTIWATCHERS GMAIL
    api_key = "71959a3173904d4cb215fe33857b2665"

    # Email content
    subject = f"InvestiWatchers tracking {tracking_stocks}"
    body = f"""Stock alert for {tracking_stocks}! 
            You have optioned for {selected_option} to track
            {tracking_stocks}, you will be notified as the selected option 
            changes in price.


            Personal customer services can be found on the home page
    """

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = email_from
    message["To"] = email_sms_value
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(email_from, pw)
        server.sendmail(email_from, email_sms_value, message.as_string())
        print("Email sent successfully! HEREREREERRERE")
    except Exception as e:
        email_error = e 
        print(f"Error sending email: {e}") 
    finally:
        server.quit()

# TEST usage:
#send_email("ecueva003@gmail.com", "AAPL")
