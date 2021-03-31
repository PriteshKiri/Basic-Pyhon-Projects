import smtplib #smtp is a protocol to which connects to server to send emails
from email.message import EmailMessage


email = EmailMessage()
email['from'] = ''   #Enter your name
email['to'] = '@gmail.com' #enter email ID to whom you want to mail
email['subject'] = 'Enter your subject' #enter your subject

email.set_content('I am a python master!') # enter the content you want to send


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('@gmail.com','pwd') #enter your email ID and password
	smtp.send_message(email)
	print('all good mah boi!') #just to check the working of code