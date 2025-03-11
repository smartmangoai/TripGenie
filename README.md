# TripGenie
An AI-powered travel planning and guidance agent built with Python, helping users create personalized itineraries, find attractions, and navigate trips efficiently. 🚀✈️

It is built with ReAct framework.

# Environment
AWS EC2 with Amazon Linux 2023

# Flask_app
The Flask app is automatically monitored and managed by gunicorn via systemctl.
1, commands
```
sudo systemctl stop flask_app.service
sudo systemctl daemon-reload
pkill -f gunicorn
ps aux | grep gunicorn
journalctl -u gunicorn
```

2, /etc/systemd/system/flask_app.service
```
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/var/www/html/flask_app
ExecStart=/home/ec2-user/.local/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
```
