import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get CPU, memory, and disk usage information
cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
memory_percent = memory.percent
disk = psutil.disk_usage('/')
disk_percent = disk.percent

# Email settings
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_email_password'
from_email = 'your_email@example.com'
to_email = 'recipient_email@example.com'

# Email content
subject = 'System Resource Usage Report'
message = f"""\
CPU usage: {cpu_percent}%
Memory usage: {memory_percent}%
Disk usage: {disk_percent}%
"""

# Send email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
