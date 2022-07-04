#!/bin/sh

cd /root/portfolio-Katherine
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl daemon-reload
systemctl restart myportfolio
