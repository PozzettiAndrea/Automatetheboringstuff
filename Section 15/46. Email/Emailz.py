import os
import smtplib
conn = smtplib.SMTP("smtp.gmail.com",587)
y = conn.ehlo()
print(y)
conn.starttls()
x = conn.login("andrea@pozzetti.it", "")
print(x)
conn.sendmail("andrea@pozzetti.it","andrea@pozzetti.it","Subject: So long and thanks for all the fish"

os.system("pause")